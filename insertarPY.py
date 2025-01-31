from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'PruebaAPIGoogleSheets/key.json'
SPREADSHEET_ID = '1vN7XW12gWMcKNLDHygHuPZyyAr8_8EeZPVXJoiXPpUA'
result = ''

def insertar_google_sheets():
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

    if not values:
        print("No se insertó")
        return "No se encontraron datos."
    else:
        # Convertimos los valores en una cadena de texto para mostrar en HTML
        print("Si se insertó")
    return f"Datos insertados correctamente.\n{(result.get('updates').get('updatedCells'))}"

if __name__ == "__main__":
    # Llama a la función y captura el resultado
    result = insertar_google_sheets()
    print(result)  # Imprime el resultado para verifica