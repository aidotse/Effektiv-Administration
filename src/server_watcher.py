from utils.watcher.update_db import check_db, cleanse_documents, init_db
from utils.watcher.watcher_utils import start_watcher

choicetext = """
start - Start the watcher
reset - Remove all documents from DB (not directory) and then re-add them
check - Print all documents that are currently in the DB
quit - Quit the CLI

> """

if __name__ == "__main__":
    DIRECTORY = "./documents/"  # Change to path of network folder
    while True:
        choice = input(choicetext)

        if choice.lower() == "start":
            print("Press ctrl+c to stop watcher")
            start_watcher(DIRECTORY)
        elif choice.lower() == "reset":
            cleanse_documents()
            init_db(DIRECTORY)
            print("Reset done")
        elif choice.lower() == "check":
            check_db()
        elif choice.lower() == "quit":
            print("closing CLI")
            break
