import chromadb
    # client = chromadb.PersistentClient(path=persist_directory)
import torch
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from transformers import AutoTokenizer, AutoModel

def preprocess_text(text, chunk_size=2000):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def perform_query(query: str):
    collection_name = "documents_collection"
    persist_directory = "chroma_storage"

    # Instantiate the Chroma client or use the appropriate class/method
    client = chromadb.PersistentClient(path=persist_directory)

    # Get the collection.
    collection = client.get_collection(name=collection_name)

    print("Querying...\n")

    # Instantiate a Hugging Face tokenizer and model
    model_name = "bert-base-uncased"  # Replace with your desired Hugging Face model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Preprocess the query into chunks
    query_chunks = preprocess_text(query)

    # Perform similarity checks on each chunk
    results = []
    for chunk in query_chunks:
        # Tokenize and obtain embeddings using the Hugging Face model
        tokens = tokenizer(chunk, return_tensors="pt")
        with torch.no_grad():
            embeddings = model(**tokens).last_hidden_state.mean(dim=1).squeeze().numpy()
        
        # Convert the embeddings to a list of strings for the query_texts argument
        embeddings_str = [str(val) for val in embeddings.tolist()]

        result_chunk = collection.query(
            query_texts=embeddings_str, n_results=4, include=["documents", "metadatas"]
        )

        filepaths = [result["filepath"] for result in result_chunk["metadatas"][0]]
        documents = result_chunk["documents"][0]
        result_chunk = [{"filepath": filepath, "text": document} for filepath, document in zip(filepaths, documents)]
        results.extend(result_chunk)

    return results

# Example usage:
query = "Your query text goes here."
results = perform_query(query)
print(results)
