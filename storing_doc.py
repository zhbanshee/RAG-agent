from vector_store import vector_store     
from load_split_doc import load_and_split_documents

# получаем чанки
all_splits = load_and_split_documents()

if not all_splits:
    print("Ошибка: Документы не найдены или пустые.")
    exit()

# используем метаданные для анализа объема данных.
sources = set(split.metadata.get('source') for split in all_splits if 'source' in split.metadata)
total_chars = sum(len(split.page_content) for split in all_splits)

print(f"--- Статистика базы знаний ---")
print(f"Документов: {len(sources)}")
print(f"Чанков: {len(all_splits)}")
print(f"Символов: {total_chars}")
print("------------------------------")

# проверяем базу
existing_data = vector_store.get()
# если база уже содержит данные, выводим предупреждение и не перезаписываем ее
if existing_data and len(existing_data.get("ids", [])) > 0:
    print(f"База уже содержит {len(existing_data['ids'])} чанков. Запись отменена.")
else:
    # если база пуста, выполняем векторную индексацию
    print("Записываю чанки в ChromaDB...")
    vector_store.add_documents(documents=all_splits)
    print("--- Успешно сохранено! ---")