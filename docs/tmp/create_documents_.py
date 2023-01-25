
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


CREDENTIALS_FILE = 'c:/work/python/aspirin/creds.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


def newDocument():
    title = 'ASPIRIn - Docs'

    spreadsheet = {
                'properties': {
                'title': title
                }
            }

    spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                fields='spreadsheetId').execute()
    new_sheet_id = format(spreadsheet.get('spreadsheetId'))

    file_link = f"https://docs.google.com/spreadsheets/d/{new_sheet_id}/edit"
    print(file_link)
    
    spreadsheet_id = new_sheet_id


    f = open('c:/work/python/aspirin/users_data.csv','a')
    file_out = f"chat.id;id_document;{spreadsheet_id};"
    f.write(file_out+'\n')
    f.close()
    # print(spreadsheet_id)

    driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
    access = driveService.permissions().create(
                fileId = spreadsheet_id,
                body = {'type': 'user', 'role': 'writer', 'emailAddress': 'mikhail_maksimov@goit.ua'},  # Открываем доступ на редактирование
                fields = 'id'
            ).execute()

    # print(access)
    request_body = {
                'requests':[
                    {'addSheet':{
                        'properties':{
                            'title':"Аналіз",
                            'gridProperties':{
                                'rowCount':20,
                                'columnCount':5
                            },
                            'tabColor':{
                                'red': 0.6,
                                'green': 0.1,
                                'blue': 0.1
                            },
                            'hidden': False
                        }
                    }},
                    {'addSheet':{
                        'properties':{
                            'title':"Стратегія",
                            'gridProperties':{
                                'rowCount':20,
                                'columnCount':5
                            },
                            'tabColor':{
                                'red': 0.6,
                                'green': 0.6,
                                'blue': 0.1
                            },
                            'hidden': False
                        }
                    }},
                    {'addSheet':{
                        'properties':{
                            'title':"Продукт",
                            'gridProperties':{
                                'rowCount':20,
                                'columnCount':5
                            },
                            'tabColor':{
                                'red': 0.1,
                                'green': 0.6,
                                'blue': 0.6
                            },
                            'hidden': False
                        }
                    }},
                    {'addSheet':{
                        'properties':{
                            'title':"Інтелектуальна робота",
                            'gridProperties':{
                                'rowCount':20,
                                'columnCount':5
                            },
                            'tabColor':{
                                'red': 0.1,
                                'green': 0.1,
                                'blue': 0.6
                            },
                            'hidden': False
                        }
                    }},
                    {'addSheet':{
                        'properties':{
                            'title':"Ресурси",
                            'gridProperties':{
                                'rowCount':20,
                                'columnCount':5
                            },
                            'tabColor':{
                                'red': 0.1,
                                'green': 0.6,
                                'blue': 0.1
                            },
                            'hidden': False
                        }
                    }},
                    {'addSheet':{
                        'properties':{
                            'title':"Індикація",
                            'gridProperties':{
                                'rowCount':20,
                                'columnCount':5
                            },
                            'tabColor':{
                                'red': 0.6,
                                'green': 0.1,
                                'blue': 0.6
                            },
                            'hidden': False
                        }
                    }}
                ]
            }

    service.spreadsheets().batchUpdate(
                spreadsheetId = spreadsheet_id,
                body = request_body
            ).execute()


    request_body = {
                'requests':[
                    {'deleteSheet':{
                        'sheetId':'0'
                    }}
                ]
                    }

    service.spreadsheets().batchUpdate(
                spreadsheetId = spreadsheet_id,
                body = request_body
            ).execute()

    values = service.spreadsheets().values().batchUpdate(
                spreadsheetId=spreadsheet_id,
                body={
                    "valueInputOption": "USER_ENTERED",
                    "data": [
                        {"range": "Аналіз!A2:A11",
                        "majorDimension": "COLUMNS",
                        "values": [["Що ви хочете від бізнесу?", "Що ви досягли (ваше CV)?","Які ваші сильні сторони?","Які існують можливості?","Ваша сфера?","Ваша цільова аудиторія?","Ключовий запит цілової аудиторії?","Перелік конкурентів","Перелік маркетплейсів","Перелік інформаційних ресурсів"]]},
                        {"range": "Стратегія!A2:A7",
                        "majorDimension": "COLUMNS",
                        "values": [["Міссія", "Візія","Цінності","Етапи реалізації візії","Мета першого етапу","Задачі першого етапу"]]},
                        {"range": "Продукт!A2:A12",
                        "majorDimension": "COLUMNS",
                        "values": [["VPC. Дії користувача", "VPC. Болі користувача","VPC. Вигоди користувача","VPC. Белутолювачі","VPC. Генератори вигід","VPC. Продукти та серівси","Банер","Текст, що продає","Сайт","Презентація-слайди","Відео презентації-виступу"]]},
                        {"range": "Інтелектуальна робота!A2:A14",
                        "majorDimension": "COLUMNS",
                        "values": [["CJM. Поінформованість", "CJM. Вивчення","CJM. Вибір","CJM. Покупка","CJM. Лояльність","CJM. Адвокація бренда","Кількість лідів","CPI (Ціна ліда)","CR (Загальна конверсія в продаж)","CAC","FixedCosts","Variable Costs","Revenue"]]},
                        {"range": "Ресурси!A2:A12",
                        "majorDimension": "COLUMNS",
                        "values": [["BMC. Ключові активності", "BMC. Ключові ресурси","BMC. Ключові партнери","BMC. Структура затрат","BMC. Відношення із користувачами","BMC. Канали комунікації","BMC. Сегменти ЦА","BMC. Потоки доходів","Структура компанії","Посадові інструкції","Фінансове планування"]]},
                        {"range": "Індикація!A2:A11",
                        "majorDimension": "COLUMNS",
                        "values": [["O (OBJECTIVE) (в контексті мети)", "KR (KEY RESULTS)","Основні показники","Цільові значення основних показників","Графік загальних зустрічей","Графік зустрічей 1 на 1"]]},
                ]
                }
            ).execute()
    return new_sheet_id

print(newDocument())
