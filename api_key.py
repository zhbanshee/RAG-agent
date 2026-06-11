import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

gemini_key = os.getenv("GOOGLE_API_KEY")
if not gemini_key:
    raise ValueError("Ошибка: GOOGLE_API_KEY не найден в файле .env!")

os.environ["GOOGLE_API_KEY"] = gemini_key

model = init_chat_model("google_genai:gemini-3.5-flash")