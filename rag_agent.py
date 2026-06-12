from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from api_key import model                
from vector_store import vector_store

@tool
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    # Возвращаем ТОЛЬКО текст документа
    serialized = "\n\n".join(
        (f"{doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized

# Формируем шаблон
prompt_template = ChatPromptTemplate.from_messages([
    ("system", (
        "Ты — официальный AI-ассистент Jois. "
        "Используй предоставленный контекст для ответа на вопрос. "
        "Если ответа нет в контексте — честно скажи, что не знаешь."
    )),
    ("human", "Контекст:\n{context}\n\nВопрос: {input}"),
])

# Функция-связка для цепочки
def search_db(inputs):
    query = inputs["input"]
    return retrieve_context.invoke(query)

# Финальная цепочка (LCEL)
agent = (
    {
        "context": search_db, 
        "input": lambda x: x["input"]
    }
    | prompt_template
    | model
)