from __future__ import print_function

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
import logging
import sqlite3


from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

condition = ""

# --------start option-------
# Зробити функцію, яка віддає словник
start_options = []
titles = ["ПІБ","email","Кількість Співробітників","Годовий оберт","КВЕД"]
codes = ["name","email","n_staff","turnover","kved"]
for i in range(len(titles)):
    dict_={"name":titles[i],"slug":codes[i]}
    start_options.append(dict_)
# --------start option-------

# --------parameters-------
# Зробити функцію, яка віддає словник
question_title = ["Аналіз","Стратегія","Продукти","Інтелект","Ресурси","Індикація"]
question_code = ["a","s","p","i","r","in"]

# Структура кнопок АСПІРИн
main_options = []
for i in range(len(question_title)):
    dict_={"name":question_title[i],"slug":question_code[i],"childs":None}
    main_options.append(dict_)
# --------parameters-------


# Структура кнопок в документі
document_title = ["Отримати документ","Відправити документ"]
document_code = ["get","send"]
document_options = []
for i in range(len(document_code)):
    dict_={"name":document_title[i],"slug":document_code[i],"childs":None}
    document_options.append(dict_)
# --------parameters-------


def stage_check(id):
    global question_code
    global codes
    f = open('users_data.csv','r')
    string = ''
    question_code_n = []
    reg_code_n = []
    for el in range(len(codes)):
        reg_code_n.append(0)
    for el in range(len(question_code)):
        question_code_n.append(0)

    for line in f:
        elems = line.split(';')
        print(elems)
        for code in range(len(codes)):
            if int(elems[0])== int(id) and elems[1] == codes[code]:
                reg_code_n[code] = 1

        for code in range(len(question_code)):
            # Перевіряємо
            if int(elems[0])== int(id) and elems[1] == question_code[code]:
                question_code_n[code] = 1
        print(reg_code_n)
    stage_out = 3
    for n in reg_code_n:
        if n == 0:
            stage_out = 1
            break
    if stage_out == 3:
        for n in question_code_n:
            if n == 0:
                stage_out = 2
                break
    return stage_out



def aspirin_description(step):
    out_text = ''
    if step == 'a':
        out_text = 'Який стан аналізу: чи спираєатесь ви свої сильні сторони, чи бачите ви можливості, чи проаналізували аналогічні пропозиції?'
    if step == 's':
        out_text = 'Який стан стратегії: чи розумієте ви для чого працюєте, яким буде ваш бізнес за 10 років, яка поточна мета та плани?'
    if step == 'p':
        out_text = 'Який продукт: яка цільова аудиторія, які йх болі та бажані вигоди, як їх закриваї ваш продукт, що він з себе має?'
    if step == 'i':
        out_text = 'Чи опрацювали ви продукт інтелектуально: порахували Юніт-економіку, знаєте вартість ліда, конверсії та розходи?'
    if step == 'r':
        out_text = 'Як ви працюєте із ресурсами: чи є структура штату та  посадові інструкції, процес фінансового планування, чи вкладаєетесь ви в технології?'
    if step == 'in':
        out_text = 'Як у вас з індикацією процесі? Чи є дашборд? Чи заплановані зустрічі із командами та 1 на 1 зі співробітниками?'
    return out_text

def getemail(id):
    f = open('users_data.csv','r')
    email_out = ''
    for line in f:
        elems = line.split(";")
        if int(elems[0])== int(id) and elems[1] == 'email':
            email_out = elems[2]
    return email_out

def keyb(id,list_in):
    key_lst = []
    kb = []
    if stage_check(id) == 1:
        s_lst = start_code_check(id)
        for i in range(len(start_options)):
            if s_lst[i]==0:
                key_lst = [(InlineKeyboardButton(start_options[i]["name"], callback_data=start_options[i]["slug"]))]
                kb.append(key_lst)

    if stage_check(id) == 2:
        q_lst = question_code_check(id)
        for i in range(len(main_options)):
            if q_lst[i]==0:
                key_lst = [(InlineKeyboardButton(main_options[i]["name"], callback_data=main_options[i]["slug"]))]
                kb.append(key_lst)
                
    if stage_check(id) == 3:
        for i in range(len(document_options)):
            key_lst = [(InlineKeyboardButton(document_options[i]["name"], callback_data=document_options[i]["slug"]))]
            kb.append(key_lst)

    return kb


def keyb_main(id,list_in):
    key_lst = []
    kb = []
    q_lst = question_code_check(id)
    for i in range(len(list_in)):
        if q_lst[i]==0:
            key_lst = [(InlineKeyboardButton(list_in[i]["name"], callback_data=list_in[i]["slug"]))]
            kb.append(key_lst)
    return kb

def keyb_line(id,list_in):
    key_lst = []
    for i in range(len(list_in)):
        if start_check(id,list_in)[i]==0:
            key_lst.append(InlineKeyboardButton(list_in[i]["name"], callback_data=list_in[i]["slug"]))
    return [key_lst]


def dict2list_slug(dict_in):
    check_list = []
    for d in dict_in:
        check_list.append(d["slug"])
    return check_list


def start_check(id,check_dict):
    f = open('users_data.csv','r')
    reg_status = []
    check_list = dict2list_slug(check_dict)

    for i in range(len(check_list)):
        reg_status.append(0)
    for line in f:
        elements = line.split(";")
        if elements[0] == str(id):
            for i in range(len(check_list)):
                if elements[1]==check_list[i]:
                    reg_status[i] = 1
    f.close()
    return reg_status

def button(update: Update, context: CallbackContext) -> None:
    global condition
    query = update.callback_query
    query.answer()
    chat = update.effective_chat
    print(query.data)
    if (query.data in dict2list_slug(start_options)) or (query.data in dict2list_slug(main_options)):
        # print(start_check(chat.id,start_options))
        query.edit_message_text(text=f"Введите {aspirin_description(query.data)}")
        condition = query.data
    if query.data == 'get':


        CREDENTIALS_FILE = 'creds.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

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

        driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
        access = driveService.permissions().create(
            fileId = new_sheet_id,
            body = {'type': 'user', 'role': 'writer', 'emailAddress': f'{getemail(chat.id)}'},  # Открываем доступ на редактирование
            fields = 'id'
        ).execute()


        spreadsheet_id = new_sheet_id
        f = open('users_data.csv','a')
        file_out = f"{chat.id};id_document;{spreadsheet_id};"
        f.write(file_out+'\n')
        f.close()
        print(spreadsheet_id)


        driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
        access = driveService.permissions().create(
            fileId = spreadsheet_id,
            body = {'type': 'user', 'role': 'writer', 'emailAddress': 'mikhail_maksimov@goit.ua'},  # Открываем доступ на редактирование
            fields = 'id'
        ).execute()

        print(access)



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


        print(access)


        query.edit_message_text(text=f"Перейдіть до документа: {file_link}")
        condition = query.data


def check(update: Update, context: CallbackContext) -> None:
    global start_options
    chat = update.effective_chat
    keyboard = keyb(chat.id,main_options)
    reply_markup = InlineKeyboardMarkup(keyboard)
    if len(start_check(chat.id,main_options))!=sum(start_check(chat.id,main_options)):
        string = "Оберіть один з варіантів:"
    else:
        string = "Доступні команди: /check"
    update.message.reply_text(string, reply_markup=reply_markup)



def start(update: Update, context: CallbackContext) -> None:

    global start_options
    chat = update.effective_chat
    keyboard = keyb(chat.id,start_options)
    reply_markup = InlineKeyboardMarkup(keyboard)
    string = 'Оберіть варіант'
    # if len(start_check(chat.id,start_options))!=sum(start_check(chat.id,start_options)):
    #     string = "Оберіть один з варіантів:"
    # else:
    #     string = "Доступні команди: /check"
    update.message.reply_text(string, reply_markup=reply_markup)

def status(update, context):
    chat = update.effective_chat
    # print(question_code_check(chat.id))
    string = stage_check(chat.id)

    update.message.reply_text(string)

def start_code_check(id):
    f = open('users_data.csv','r')
    string = ''
    start_code_n = []
    for el in range(len(codes)):
        start_code_n.append(0)
    # print(question_code_n)
    for line in f:
        elems = line.split(';')
        # print(elems[1] in question_code)
        for code in range(len(codes)):
            # Перевіряємо
            if int(elems[0])== int(id) and elems[1] == codes[code]:
                # print(code)
                start_code_n[code] = 1
        string+=line+"\r\n"
    # print(question_code_n)
    return start_code_n

def question_code_check(id):
    f = open('users_data.csv','r')
    string = ''
    question_code_n = []
    for el in range(len(question_code)):
        question_code_n.append(0)
    # print(question_code_n)
    for line in f:
        elems = line.split(';')
        # print(elems[1] in question_code)
        for code in range(len(question_code)):
            # Перевіряємо
            if int(elems[0])== int(id) and elems[1] == question_code[code]:
                # print(code)
                question_code_n[code] = 1
        string+=line+"\r\n"
    # print(question_code_n)
    return question_code_n


def echo(update, context):
    global condition, account
    #Отримаємо повідомлення
    string_in = update.message.text.replace("\n", " | ")
    chat = update.effective_chat

    # Заповнюємо перший етап
    if (condition in dict2list_slug(start_options)) or (condition in dict2list_slug(main_options)):
        f = open('users_data.csv','a')
        file_out = f"{chat.id};{condition};{string_in};"
        print("CSV")
        print(file_out)
        f.write(file_out+'\n')
        f.close()
        condition = ""

    print(start_check(chat.id,start_options))
    if len(start_check(chat.id,start_options))!=sum(start_check(chat.id,start_options)):
        # Якщо незаповнено - просимо заповнити стартові показники
        string = "Выберите один из вариантов:"
        keyboard = keyb(chat.id,start_options)
    else:
        # Якщо перші показники заповнено - виводимо набір кнопок для АСПІРИн-у
        string = "Ваши команды: /check"
        keyboard = keyb(chat.id,main_options)
        print(main_options)


    reply_markup = InlineKeyboardMarkup(keyboard)
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=string,reply_markup=reply_markup)



def main() -> None:
    updater = Updater("5033262547:AAFmJCEFk68OGCZOJbbV4S9Wvr4Zbw9yUcg")

    updater.dispatcher.add_handler(CommandHandler('check', check))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('status', status))

    # updater.dispatcher.add_handler(CommandHandler('drop', drop))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()