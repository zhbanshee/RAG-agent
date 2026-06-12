import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Ошибка: GOOGLE_API_KEY не найден в файле .env")

os.environ["GOOGLE_API_KEY"] = api_key

# Инициализируем официальный клиент Google GenAI
client = genai.Client(api_key=api_key)

model = init_chat_model("google_genai:gemini-3.5-flash")