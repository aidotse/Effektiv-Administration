from time import sleep

from utils.mail.mail_utils import get_service, respond_to_mails

# If modifying these SCOPES, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
SENDER_ADRESS = "informationhantering@gmail.com"
USER_ID = "me"


def main():
    service = get_service(SCOPES)

    """
    Checks the inbox for mails every 5 seconds for 30 minutes or until keyboard interupt.
    Implement google pub sub later to trigger when new mail is received
    """

    print("Started mailbox watcher")
    for _ in range(360):
        print("Checking...")
        respond_to_mails(service, SENDER_ADRESS, USER_ID)
        sleep(5)


if __name__ == "__main__":
    main()
