from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def login():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
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
                'C:/Users/dutta/Desktop/Hackmit/TimManagement/flask stuff/credentials.json', SCOPES)
            creds = flow.run_local_server(host='localhost', port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Current date and time
        #now = datetime.datetime.utcnow().isoformat()+'Z'
        now = datetime.datetime.now()
        #today = datetime.datetime.today()

        # Fetch from Calendar API
        events_result = service.events().list(calendarId='primary', timeMin=now.utcnow().isoformat()+'Z',
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = [x for x in events_result.get('items', []) if 'T' in x['start'].get('dateTime', x['start'].get('date'))]

        if not events:
            print('No upcoming events found.')
            return

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))[:19]
            end = event['end'].get('dateTime', event['end'].get('date'))
            print(datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S').utcnow(), now, event['summary'], "Tim until:",datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')-now)

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    login()

#def event_detector():
  #  print("Hello")
  #  return

#def time_difference():
  #  print("Hello")
  #  return

