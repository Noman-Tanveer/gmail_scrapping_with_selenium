from __future__ import print_function

import os.path


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
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

    try:
        # Modify the code below to get the responses to the email titled
        # "[URGENT]: Confirm your Enrollment in NUST High Impact Training Program"
        service = build('gmail', 'v1', credentials=creds)
        thread_id = "18a4bc2bb683a951"
        threads = service.users().threads().list(userId='me').execute()
        threads.get('threads', [])
        for t in threads:
            print(t)
        # print(f'Subject: {message_text["subject"]}')
        # print(f'From: {message_text["from"]}')
        # print(f'Date: {message_text["date"]}')
        # print(f'Snippet: {message_text["snippet"]}')
        # print(f'Body: {message_text["body"]["data"]}')

        if not message_list:
            print('No messages found.')

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()