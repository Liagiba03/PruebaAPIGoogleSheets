from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '1vN7XW12gWMcKNLDHygHuPZyyAr8_8EeZPVXJoiXPpUA'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Debe ser una matriz por eso el doble [[]]
values = [[384,304,482,278,408,306,372,313,455,293,504,280,350,295,364,282,440,262,487,244,431,374,427,423,502,405,454,412,455,416,'image']]
# Llamamos a la api
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
							range='A1',
							valueInputOption='USER_ENTERED',
							body={'values':values}).execute()
print(f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}")