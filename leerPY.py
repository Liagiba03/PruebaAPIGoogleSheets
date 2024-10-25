from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'PruebaAPIGoogleSheets/key.json'
SPREADSHEET_ID = '1vN7XW12gWMcKNLDHygHuPZyyAr8_8EeZPVXJoiXPpUA'

def leer_google_sheets():
    creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Llamada a la API para obtener los valores
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='facial_keypoints!A:AE').execute()
    values = result.get('values', [])

    if not values:
        return "No se encontraron datos."
    else:
        # Convertimos los valores en una cadena de texto para mostrar en HTML
        output = '\n'.join([', '.join(row) for row in values])
        print("Si se leyó")
        return output

if __name__ == "__main__":
    result = leer_google_sheets()
    print(result)  # Esto imprimirá el resultado en la consola