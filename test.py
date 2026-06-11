import time
import os
from dotenv import load_dotenv
from google import genai
from vector_store import vector_store

# Загружаем ключи
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Инициализируем официальный клиент Google GenAI
client = genai.Client(api_key=api_key)

questions = [
    "На каких платформах работает Jois?",
    "Можно ли пользоваться Jois бесплатно и какие есть ограничения?",
    "Какая задержка у анимации губ (lipsync) в Jois?",
    "Как Jois понимает, какую эмоцию нужно показать на лице во время разговора?",
    "Я еду в поезде, где совсем нет связи. Смогу ли я поговорить с Джойс?",
    "Где я могу переодеть своего аватара?",
    "За счет чего приложение не разряжает батарею телефона мгновенно при рендеринге 3D?",
    "Сливаются ли мои разговоры с Jois в общую сеть для обучения других ИИ?",
    "Как мне заказать доставку одежды из Pinduoduo через приложение Jois?",
    "Какое кодовое имя у Python-скрипта, который запускает базу данных MySQL в Jois?"
]

print("Запуск прямого RAG-теста...\n")

for i, q in enumerate(questions, 1):
    print(f"Вопрос {i}: {q}")
    start = time.time()
    try:
        # Вытаскиваем чанки из нашей новой базы
        docs = vector_store.similarity_search(q, k=3)
        context = "\n\n".join([d.page_content for d in docs])
        
        # Строгий системный промт
        prompt = (
            "Ты — официальный ИИ-помощник для приложения Jois. "
            "Отвечай на вопрос, опираясь ТОЛЬКО на предоставленный контекст. "
            "Если в контексте нет ответа на вопрос (например, про сторонние сервисы вроде Pinduoduo или скрытые скрипты), "
            "честно ответь: 'В моей базе знаний нет этой информации.' Не придумывай ничего от себя.\n\n"
            f"Контекст:\n{context}\n\n"
            f"Вопрос: {q}"
        )
        
        # Прямой вызов модели gemini-2.5-flash
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt,
        )
        print(f"Ответ:\n{response.text}")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        
    print(f"Время: {time.time() - start:.2f} сек.")
    print("-" * 50)