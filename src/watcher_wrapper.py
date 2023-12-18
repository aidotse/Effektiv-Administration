from watcher_utils.watcher import start_watcher
from watcher_utils.update_db import cleanse_documents, init_db, check_db

if __name__ == "__main__":
    DIRECTORY = "./documents/"

    """Steg 1, ta bort dokument (Om chroma storage är tom behövs inte detta"""
    cleanse_documents()
    """Steg 2 Stoppa in dokument"""
    init_db(DIRECTORY)
    """Steg 3 kolla vad som finns i db (optional)"""
    check_db()
    
    #start_watcher(DIRECTORY)


    