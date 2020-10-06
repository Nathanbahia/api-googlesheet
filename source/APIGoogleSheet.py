from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# ESCOPO DEFINIDO PARA LEITURA E ESCRITA DE DADOS
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# ID DA PLANILHA E INTERVALO DE DADOS
SPREADSHEET_ID = '1nCA5OmZ06AAYzBEuW-yWAEuuDlNb_iTdXdBEwSm3aEA'
RANGE_NAME = 'ponto_form!A:C'


def conn():
    """
    Função interna da API do Google Sheets para autenticação
    de usuário.
    """
    creds = None    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    return service


def escritaGoogleSheets(valores):
    """
    Função para inserir dados na planilha do Google
    """
    service = conn()
    body = {'values': valores}
    
    result = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
        valueInputOption='USER_ENTERED', body=body).execute()
    print('{0} cells appended.'.format(result.get('updates').get('updatedCells')))
    return valores


def leituraGoogleSheets():
    """
    Função para leitura dos dados gravados na planilha
    do Google
    """
    service = conn()
    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        print('FUNCIONÁRIO   DATA   HORA')
        for row in values:            
            print(f"{row[0]} {row[1]} {row[2]}")
