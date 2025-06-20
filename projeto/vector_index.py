from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import faiss
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.core.storage import StorageContext 
from llama_index.core import load_index_from_storage
from llama_index.llms.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Configurar LLM do Groq
llm = Groq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

# Configurar embeddings locais (HuggingFace)
embed_model = HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-large")

# Configurar globalmente no Settings
Settings.llm = llm
Settings.embed_model = embed_model

# Caminho para a pasta onde está o index FAISS
INDEX_PATH = "./faiss_index"
FAISS_FILE = f"{INDEX_PATH}/faiss_store.index"

# Carregando o index FAISS
faiss_index = faiss.read_index(FAISS_FILE)
vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(persist_dir=INDEX_PATH, vector_store=vector_store)
index = load_index_from_storage(storage_context)