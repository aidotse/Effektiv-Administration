import chromadb



def preform_query(query: str):
    collection_name = "documents_collection"
    persist_directory = "chroma_storage"

    client = chromadb.PersistentClient(path=persist_directory)

    # Get the collection.
    collection = client.get_collection(name=collection_name)

    print("Querying...\n")
    
    results = collection.query(
        query_texts=[query], n_results=5, include=["documents", "metadatas"]
    )
    filepaths = [result["filepath"] for result in results["metadatas"][0]]
    documents = results["documents"][0]
    result = [{"filepath": filepath, "text": document} for filepath, document in zip(filepaths, documents)]
    return result



if __name__ == "__main__":
    preform_query("Budget")