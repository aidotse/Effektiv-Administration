import os
import argparse
import pypandoc
from watcher_utils.file_reader import get_chunks
from tqdm import tqdm

import chromadb
COLLECTION_NAME = "documents_collection"
PERSIST_DIR :str= "chroma_storage"

def load_file(filepath):
    documents = []
    metadatas = []

    chunks = get_chunks(filepath)
    for i, chunk in enumerate(chunks):
        documents.append(chunk)
        metadatas.append({"filepath": filepath, "chunk": i})


    client = chromadb.PersistentClient(path=PERSIST_DIR)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    count = collection.count()
    print(f"Collection already contains {count} documents")
    ids = [str(i) for i in range(count, count + len(documents))]

    # Load the documents in batches of 100
    for i in tqdm(
        range(0, len(documents), 100), desc="Adding documents", unit_scale=100
    ):
        collection.add(
            ids=ids[i : i + 100],
            documents=documents[i : i + 100],
            metadatas=metadatas[i : i + 100],  # type: ignore
        )

    # new_count = collection.count()
    # print(f"Added {new_count - count} documents")
    results = collection.get(where= {"filepath": filepath})


def remove_file(filepath):
    client = chromadb.PersistentClient(path=PERSIST_DIR)
    collection: chromadb.Collection = client.get_collection(name=COLLECTION_NAME)
    if collection is None:
        print(f"No collection found with name {COLLECTION_NAME}")
        return
    

    collection.delete(where= {"filepath": filepath})


import shutil
def remove_chroma_storage_files():
    """
    Removes all the folders in the specified directory.

    :param directory_path: The path to the directory where folders will be removed.
    """
    # Check if the directory exists
    directory_path = "chroma_storage"
    if not os.path.exists(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return

    # Iterate over all files and folders in the specified directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        # Check if it is a folder
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Removed folder: {item_path}")

def cleanse_documents():
    input("You are deleting everything in the db, do you want to continue?")
    input("fr?")
    input("frfr?")
    client = chromadb.PersistentClient(path=PERSIST_DIR)
    client.delete_collection(name=COLLECTION_NAME)
    remove_chroma_storage_files()
    
    print("DB deleted")

def update_file(filepath):
    remove_file(filepath)
    load_file(filepath)

def check_db():
    client = chromadb.PersistentClient(path="chroma_storage")

    # If the collection already exists, we just return it. This allows us to add more
    # data to an existing collection.
    collection = client.get_or_create_collection(name="documents_collection")
    result = collection.get()
    print(result)



def init_db(directory):
    # Read all files in the data directory
    #skappar list för documents och metadatas
    documents = []
    metadatas = []
    #läser documentes directory
    files = os.listdir(directory)
    #läser alla rader i dokumenten och sparar det i document och metadata list
    for filepath in files:
        chunks = get_chunks(directory+filepath)
        for i, chunk in enumerate(chunks):
            documents.append(chunk)
            metadatas.append({"filepath": directory+filepath, "chunk": i})

    # Instantiate a persistent chroma client in the persist_directory.
    client = chromadb.PersistentClient(path="chroma_storage")

    # If the collection already exists, we just return it. This allows us to add more
    # data to an existing collection.
    collection = client.get_or_create_collection(name="documents_collection")

    # Create ids from the current count
    count = collection.count()
    print(f"Collection already contains {count} documents")
    ids = [str(i) for i in range(count, count + len(documents))]

    # Load the documents in batches of 100
    for i in tqdm(
        range(0, len(documents), 100), desc="Adding documents", unit_scale=100
    ):
        collection.add(
            ids=ids[i : i + 100],
            documents=documents[i : i + 100],
            metadatas=metadatas[i : i + 100],  # type: ignore
        )

    new_count = collection.count()
    print(f"Added {new_count - count} documents")



if __name__ == "__main__":
    cleanse_documents()
    init_db("./documents2/")
