import os
from langchain_chroma import Chroma
from emb_model import embeddings
from load_split_doc import load_and_split_documents

# путь к папке, где chromadb будет хранить векторы на диске
CHROMA_PATH = "./chroma_langchain_db"

# если базы на диске еще нет, создаем ее с нуля
if not os.path.exists(CHROMA_PATH):
    print("Локальная база данных не найдена. Запускаем индексацию документов...")
    
    # берем нарезанные куски документов
    chunks = load_and_split_documents()
    
    # если чанки есть, собираем базу и сохраняем на диск
    if chunks:
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_PATH,
            collection_name="jois_collection"
        )
        print("База данных успешно создана и сохранена на диск!")
    else:
        print("Ошибка: Нет чанков для создания базы данных. Создан пустой объект.")
        vector_store = None
else:
    # если папка уже есть, просто подключаемся к готовой базе
    print("Подключение к существующей локальной базе ChromaDB...")
    vector_store = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_name="jois_collection"
    )