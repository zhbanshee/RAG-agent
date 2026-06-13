from vector_store import vector_store     
from load_split_doc import load_and_split_documents

# проверяем, есть ли уже какие-то чанки в нашей базе chromadb
existing_data = vector_store.get()

# если в базе уже что-то лежит, то ничего заново не записываем
if existing_data and len(existing_data.get("ids", [])) > 0:
    print(f"База данных уже содержит {len(existing_data['ids'])} чанков.")
    print("повторная запись отменена, чтобы тексты не дублировались.")
else:
    # если база пустая, берем нарезанные куски документов
    all_splits = load_and_split_documents()

    if all_splits:
        print("начинаю запись документов в chromadb...")
        # добавляем документы в базу и получаем их id
        document_ids = vector_store.add_documents(documents=all_splits)
        print("--- успешно сохранено! ---")
        print(f"id первых добавленных чанков: {document_ids[:3]}")
    else:
        print("ошибка: чанки не найдены. база данных пуста.")