# импорт api_key чтобы включился ключ API из .env файла
import api_key
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# создание эммбединговой модели для векторного поиска
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
