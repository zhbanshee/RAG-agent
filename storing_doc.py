from vector_store import vector_store      # <-- Импортируем базу
from load_split_doc import all_splits

print("Начинаю запись документов в Chroma DB...")
document_ids = vector_store.add_documents(documents=all_splits)
print("--- Успешно сохранено! ---")
print(f"ID первых добавленных чанков: {document_ids[:3]}")