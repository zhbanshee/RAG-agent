import os
from dotenv import load_dotenv

# загружаем ключи из файла .env
load_dotenv()

# включаем отслеживание шагов (трассировку) по умолчанию
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING", "true")

# если ключа нет, код не упадет, но выйдет предупреждение в консоли
if not os.getenv("LANGSMITH_API_KEY"):
    print("Предупреждение: LANGSMITH_API_KEY не задан в файле .env")