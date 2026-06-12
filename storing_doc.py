from vector_store import vector_store     
from load_split_doc import load_and_split_documents

# Вызываем функцию и получаем чанки для загрузки
all_splits = load_and_split_documents()

if all_splits:
    print("Начинаю запись документов в Chroma DB...")
    document_ids = vector_store.add_documents(documents=all_splits)
    print("--- Успешно сохранено! ---")
    print(f"ID первых добавленных чанков: {document_ids[:3]}")
else:
    print("Ошибка: чанки не найдены. База данных пуста.")