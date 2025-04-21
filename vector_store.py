# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import Qdrant
# from qdrant_client import QdrantClient
# from qdrant_client.http.models import Distance, VectorParams

# def build_vector_store(documents, collection_name="sop_vectors"):
#     # Use local sentence-transformers model
#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     print("#### Document: ", documents)
#     # Create a local Qdrant instance (stored on disk)
#     client = QdrantClient(path="qdrant_data")

#     # Create the collection if not exists (make sure the vectors_config fits your model's output size)
#     client.recreate_collection(
#         collection_name=collection_name,
#         vectors_config=VectorParams(size=384, distance=Distance.COSINE)  # size should match the embedding size
#     )

#     # Build Qdrant vector store
#     vector_db = Qdrant.from_documents(
#         documents,
#         embeddings,
#         client=client,
#         collection_name=collection_name
#     )

#     return vector_db

# def load_vector_store(collection_name="sop_vectors"):
#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     client = QdrantClient(path="qdrant_data")
#     return Qdrant(client=client, collection_name=collection_name, embeddings=embeddings)
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
import os
from sop_loader import load_and_split_sops

def build_vector_store(documents, collection_name="sop_collection", persist_path="qdrant_data"):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print(":: ", documents)
    qdrant = Qdrant.from_documents(
        documents,
        embedding=embedding,
        path=persist_path,
        collection_name=collection_name
    )
    print("::qdrant", qdrant)
    return qdrant

def load_vector_store(collection_name="sop_collection", persist_path="qdrant_data"):
    # embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # client = QdrantClient(location=persist_path)
    # a = Qdrant(client=client, collection_name=collection_name, embedding_function=embedding)
    # print("::a: ", a)
    # return a
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Qdrant.from_existing_collection(
        collection_name=collection_name,
        path=persist_path,
        embedding=embedding
    )

if __name__ == "__main__":
    documents = load_and_split_sops()
    build_vector_store(documents)