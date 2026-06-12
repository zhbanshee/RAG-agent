import os
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

KNOWLEDGE_BASE_DIR = "knowledge_base"

def load_and_split_documents():
    """Загружает текстовые и PDF документы из папки и разбивает их на чанки."""
    docs = []
    
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
                
        elif file.endswith('.pdf'):
            try:
                reader = PdfReader(path)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                if text.strip():
                    docs.append(Document(page_content=text, metadata={"source": file}))
            except Exception as e:
                print(f"Ошибка при чтении PDF {file}: {e}")

    if not docs:
        print(f"Предупреждение: В папке '{KNOWLEDGE_BASE_DIR}' нет файлов .txt или .pdf!")
        return []

    print(f"Успешно загружено документов: {len(docs)}")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,       
        chunk_overlap=200,   
        add_start_index=True
    )

    all_splits = text_splitter.split_documents(docs)
    print(f"Разбили документы на {len(all_splits)} чанков.")
    return all_splits

if __name__ == "__main__":
    splits = load_and_split_documents()