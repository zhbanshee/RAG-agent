import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING", "true")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

if not os.environ["LANGSMITH_API_KEY"]:
    print("Предупреждение: LANGSMITH_API_KEY не задан в файле .env")