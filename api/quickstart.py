from __future__ import print_function
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

Sample_Spreadsheet_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
Sample_Range_name = 'Class Data!A2:E'
def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json',SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open('token.json','w') as token:
            token.write(creds.to_json())
    service = build('sheets','v4', credentials=creds)

    #Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetID=Sample_Spreadsheet_ID,range=Sample_Range_name).execute()
    values = result.get('values', [])
    if not values:
        print('No data found. ')
    else:
        print('Name, Major:')
        for row in values:
            print("%s %s" %(row[0], row[4]))
if __name__ == '__main__':
    main()
