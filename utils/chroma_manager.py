# Directory: utils/chroma_manager.py
import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.Client()
embedding_fn = embedding_functions.DefaultEmbeddingFunction()

def store_version(doc_id, text):
    chroma_client.create_collection(name="chapters")
    chroma_client.get_collection("chapters").add(
        documents=[text],
        ids=[doc_id]
    )

def semantic_search(query):
    results = chroma_client.get_collection("chapters").query(
        query_texts=[query],
        n_results=1
    )
    return results

