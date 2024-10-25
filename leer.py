from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#KEY = 'key.json'
    #ID DEL DOCUMENTO
#SPREADSHEET_ID = '1vN7XW12gWMcKNLDHygHuPZyyAr8_8EeZPVXJoiXPpUA'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes= SCOPES)

service = build('sheets', 'v4', credentials = creds)
sheet = service.spreadsheets()

#Llamada a la API
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='facial_keypoints!A:AE').execute()

#Extraemos los valores
values = result.get('values', [])
print(values)