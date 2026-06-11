import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

docs = []
KNOWLEDGE_BASE_DIR = "knowledge_base"

if not os.path.exists(KNOWLEDGE_BASE_DIR):
    os.makedirs(KNOWLEDGE_BASE_DIR)

for file in os.listdir(KNOWLEDGE_BASE_DIR):
    path = os.path.join(KNOWLEDGE_BASE_DIR, file)
    
    if file.endswith('.txt'):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            docs.append(Document(page_content=text, metadata={"source": file}))
        
        except Exception as e:
             print(f"Ошибка при чтении файла {file}: {e}")

if not docs:
    print(f"В папке '{KNOWLEDGE_BASE_DIR}' пока нет файлов .txt. Добавь туда документы про Jois!")
else:
    print(f"Загружено документов: {len(docs)}")
    print(f"Пример текста из первого файла:\n---\n{docs[0].page_content[:120]}...\n---")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,       
        chunk_overlap=200,   
        add_start_index=True
        )

    all_splits = text_splitter.split_documents(docs)
    print(f"Разбили документы на {len(all_splits)} чанков.")