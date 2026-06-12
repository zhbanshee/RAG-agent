import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

gemini_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise ValueError("Ошибка: GOOGLE_API_KEY не найден в файле .env")

os.environ["GOOGLE_API_KEY"] = gemini_key

# Используем стандартный метод ядра LangChain, который у тебя работал.
# Модель 'gemini-2.5-flash' идеально подходит для агентов.
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")