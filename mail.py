from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
import pdfkit

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_messages(creds):
    # Modify the code below to get the responses to the email titled
    # "[URGENT]: Confirm your Enrollment in NUST High Impact Training Program"
    service = build('gmail', 'v1', credentials=creds)
    user_id = 'me'
    subject_query = '[URGENT]: Confirm your Enrollment in NUST High Impact Training Program'

    messages = service.users().messages().list(userId=user_id, q=f'subject:{subject_query}').execute()
    # print(threads)
    for message_data in messages['messages']:
        message = service.users().messages().get(userId=user_id, id=message_data['id']).execute()
        try:
            for part in message['payload']['parts']:
                text = part['body']['data']
        except:
            print("No body found")
            continue
        html_text = base64.urlsafe_b64decode(text).decode('utf-8')
        print("HTML Text: ", html_text)
        pdfkit.from_string(html_text,'GfG.pdf')
        break


def authenticate():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'mail_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds



if __name__ == '__main__':
    creds = authenticate()
    get_messages(creds)
