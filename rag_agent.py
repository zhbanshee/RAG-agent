from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from api_key import model
from vector_store import vector_store

# 1. Настраиваем поисковик из ChromaDB
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# Функция для склеивания найденных документов в один текст
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 2. Строгий системный промт против галлюцинаций
prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "Ты — официальный ИИ-помощник для приложения Jois. "
        "Отвечай на вопрос пользователя, опираясь ТОЛЬКО на предоставленный ниже контекст. "
        "Если в контексте нет ответа на вопрос (например, про сторонние сервисы вроде Pinduoduo "
        "или скрытые технические скрипты базы данных), честно ответь: 'В моей базе знаний нет этой информации.' "
        "Никогда не выдумывай факты от себя.\n\n"
        "Контекст:\n{context}"
    )),
    ("human", "{input}")
])

# 3. Собираем чистую RAG-цепочку (вместо капризного агента)
rag_chain = (
    {"context": retriever | format_docs, "input": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# Обертка для совместимости со скриптом test.py
class LegacyAgentExecutorCompatibility:
    def invoke(self, inputs):
        # Вызываем цепочку и упаковываем в словарь, который ждет test.py
        output = rag_chain.invoke(inputs["input"])
        return {"output": output}

agent = LegacyAgentExecutorCompatibility()