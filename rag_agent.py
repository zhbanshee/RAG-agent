from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from vector_store import vector_store

# запуска модели gemini 2.5 flash через встроенный инициализатор
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# настраиваем поиск строго по топ-3 чанкам из базы знаний
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# промпт, чтобы джойс не галлюцинировала
prompt_template = ChatPromptTemplate.from_template("""
Ты — официальный AI-ассистент Jois. 
Отвечай на вопрос пользователя, строго опираясь ТОЛЬКО на предоставленный ниже контекст. 
Если в контексте нет точного ответа на этот вопрос, честно ответь: 'Я не знаю'. 
Не придумывай информацию от себя и не используй внешние знания.

Контекст:
{context}

Вопрос: {input}
Ответ:
""")

def format_docs(docs):
    # собираем текст из найденных кусков документов в одну строчку
    return "\n\n".join(doc.page_content for doc in docs)

# собираем финальную rag-цепочку 
agent = (
    # готовим данные для промпта
    {
        # берем вопрос пользователя, отправляем в базу знаний, находим 3 куска текста и склеиваем их
        "context": retriever | format_docs, 
        # пропускаем сам вопрос пользователя дальше без изменений, чтобы подставить его в {input}
        "input": RunnablePassthrough()       
    }
    # передаем собранные context и input в наш шаблон промпта
    | prompt_template                       
    # отправляем готовый заполненный текст в модель gemini flash для генерации ответа
    | model                                 
    # вытаскиваем из сырого ответа модели только чистую строку с текстом, убирая метаданные
    | StrOutputParser()                     
)