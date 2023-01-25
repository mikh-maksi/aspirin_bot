from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'c:/work/python/aspirin/creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1ei9k8JTPdhwYZN0bZGEuV6JOeKec7UAa-ivmUkJIszk'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# sheet_lst = ['Аналіз','Стратегія','Продукт','Інтелектуальний аналіз продукту','Ресурси','Індікація']

# for sheet in sheet_lst: 
#     values = service.spreadsheets().values().get(
#         spreadsheetId=spreadsheet_id,
#         range=f"'{sheet}'!A2:B12",
#         majorDimension='COLUMNS'
#     ).execute()
#     pprint(values)


sheets = ['Аналіз','Стратегія','Продукт','Ресурси','Індикація']


for sheet in sheets:
    values = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=f"'{sheet}'!B1:B5",
            majorDimension='COLUMNS'
        ).execute()

    pprint(values)
# print(values[0][0])

# pprint(len(values['values'][0][0]))
# for el in values['values'][0]:
#     print(len(el))
# print(values.values[0][0])