import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# загрузка переменных окружения из файла .env
load_dotenv()

# проверка на наличие ключа, чтобы проект не упал молча
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Ошибка: GOOGLE_API_KEY не найден в файле .env")
