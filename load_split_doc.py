import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

# название папки, где хранятся файлы базы знаний
KNOWLEDGE_BASE_DIR = "knowledge_base"

def load_and_split_documents():
    # создаем пустой список для документов
    docs = []
    
    # если папки для документов нет, автоматически создаем ее
    if not os.path.exists(KNOWLEDGE_BASE_DIR):
        os.makedirs(KNOWLEDGE_BASE_DIR)

    # перебираем все файлы в папке базы знаний
    for file in os.listdir(KNOWLEDGE_BASE_DIR):
        path = os.path.join(KNOWLEDGE_BASE_DIR, file)
        
        # обработка текстовых файлов
        if file.endswith('.txt'):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    text = f.read()
                # сохраняем текст и записываем имя файла в метаданные   
                docs.append(Document(page_content=text, metadata={"source": file}))
            except Exception as e:
                print(f"Ошибка при чтении файла {file}: {e}")

        # обработка PDF-документов        
        elif file.endswith('.pdf'):
            try:
                reader = PdfReader(path)
                text = ""
                # постранично извлекаем текст из PDF
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                # если файл не пустой, упаковываем в формат LangChain
                if text.strip():
                    docs.append(Document(page_content=text, metadata={"source": file}))
            except Exception as e:
                print(f"Ошибка при чтении PDF {file}: {e}")

    # если файлов не нашлось, выводим предупреждение
    if not docs:
        print(f"Предупреждение: В папке '{KNOWLEDGE_BASE_DIR}' нет файлов .txt или .pdf!")
        return []

    print(f"Успешно загружено документов: {len(docs)}")
    
    # настраиваем параметры разбиения текста на куски
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,      # максимальная длина одного чанка в символах  
        chunk_overlap=200,    # перекрытие между соседними чанками для сохранения контекста
        add_start_index=True  # сохраняем позицию начала чанка в исходном файле
    )

    # нарезаем документы на чанки
    all_splits = text_splitter.split_documents(docs)
    print(f"Разбили документы на {len(all_splits)} чанков.")
    return all_splits

if __name__ == "__main__":
    # запускаем функцию загрузки и нарезки для проверки
    splits = load_and_split_documents()