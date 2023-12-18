import base64
import os
import re
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from utils.api.prompt_request import prompt_request
from rich.markdown import Markdown
import markdown
from markdown_it import MarkdownIt
import markdown2



def get_unread_emails(service, user_id="me"):
    """
    Checks the mailbox for unread messages

    args:
        service: see get_service()
        user_id: should ALWAYS be "me"

    return:
        list of dictionaries with the following structure:
        [
            {
            'id': (str),
            'name': (str),
            'address': (str),
            'subject': (str),
            'body': (str)
            }
        ]
    """
    try:
        response = (
            service.users().messages().list(userId=user_id, q="is:unread").execute()
        )
        messages = response.get("messages", [])
        emails = []

        for message in messages:
            msg_id = message["id"]
            msg = (
                service.users()
                .messages()
                .get(userId=user_id, id=msg_id, format="full")
                .execute()
            )

            # Extract the sender's email address and name using regex
            sender_info = next(
                header["value"]
                for header in msg["payload"]["headers"]
                if header["name"] == "From"
            )
            email_match = re.search(r"<(.+?)>", sender_info)
            sender_email = email_match.group(1) if email_match else sender_info
            sender_name = re.search(r"(.+?) <", sender_info)
            sender_name = sender_name.group(1) if sender_name else ""

            # Extract the subject
            subject = next(
                header["value"]
                for header in msg["payload"]["headers"]
                if header["name"] == "Subject"
            )

            # Extract the message body
            parts = msg["payload"].get("parts", [])
            body = ""
            for part in parts:
                if part["mimeType"] == "text/plain":
                    body_data = part["body"]["data"]
                    body = base64.urlsafe_b64decode(body_data).decode("utf-8")
                    break

            email_info = {
                "id": msg_id,
                "name": sender_name,
                "address": sender_email,
                "subject": subject,
                "body": body,
            }
            emails.append(email_info)

        return emails
    except Exception as error:
        print(f"An error occurred: {error}")
        return []


def mark_as_read(service, user_id, msg_id):
    """
    Marks a specified email as read.

    Args:
        service: The Gmail API service instance.
        user_id (str): The user's email ID. Usually 'me'.
        msg_id (str): The unique ID of the email to be marked as read.
    return:
        True if successfully marked as read else false
    """

    try:
        service.users().messages().modify(
            userId=user_id, id=msg_id, body={"removeLabelIds": ["UNREAD"]}
        ).execute()
        print(f"Marked message {msg_id} as read.")
        return True
    except Exception as error:
        print(f"An error occurred: {error}")
        return False


def get_service(scopes):
    """
    Creates a Gmail API service client.

    Args:
        scopes (list): A list of strings representing the API scopes.

    Returns:
        An authorized Gmail API service client.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes)
            creds = flow.run_local_server(port=5000)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)
    return service


def create_message(sender, to, subject, message_text):
    """
    Creates a message

    params:

    sender (str): The e-mail adress of the sender
    to (str): The e-mail adress of the receiver
    subject (str): The subject of the mail
    message_text (str): The message text

    return: A raw encoded message ready to be sent using send_message()
    """
    message = MIMEText(message_text, "html")
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    print(
        f"Created message from {sender} to {to}\nSubject: {subject}\nContent: {message_text}"
    )
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service: build, user_id, message):
    """
    Sends an email message.

    Args:
        service: The Gmail API service instance.
        user_id (str): The user's email ID. Usually 'me'.
        message (dict): The message to be sent. Should be created using create_message.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    try:
        message = (
            service.users().messages().send(userId=user_id, body=message).execute()
        )
        print(f"Sent {message['id']} successfully")
        return True
    except Exception as error:
        print(f"An error occurred sending the message: {error}")
        return False


def respond_to_mails(service, sender_adress, user_id):
    """
    Responds to unread emails with a specific subject.

    Args:
        service: The Gmail API service instance.
        sender_address (str): The email address of the sender (response sender).
        user_id (str): The user's email ID. Usually 'me'.

    This function scans for unread emails with the subject 'info',
    creates a response, sends it, and marks the original email as read.
    """
    unread_emails = get_unread_emails(service)

    for email in unread_emails:
        if email["subject"].lower() == "info":
            print("\nMAIL FOUND\n==================================")
            print(
                f'Sender: {email["name"]}\nAddress: {email["address"]}\nContent: {email["body"]}'
            )


            prompt = email["body"].rstrip()
            prompt_res = prompt_request(prompt)

            md = MarkdownIt()
            # formatted_answer = markdown.markdown(prompt_res['answer'])
            # formatted_answer = md.render(prompt_res['answer'])
            formatted_answer = markdown2.markdown(prompt_res['answer'], extras=['tables'])

            

            response_text = f"""
Hej {email["name"]}!

Här kommer svaret på frågan "{prompt}":
{formatted_answer}

De här dokumenten har använts:
{", ".join(prompt_res['doc_names'])}


Hälsningar,
Effektiv Administration
            """
            

            message = create_message(
                sender=sender_adress,
                to=email["address"],
                subject=f'Svar till frågan {email["body"][:50]}',
                message_text=response_text,
            )

            send_message(service, user_id, message)
            mark_as_read(service, user_id, email["id"])
