from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

def start_step():
    start_options = []
    titles = ["ПІБ","email","Кількість Співробітників","Годовий оберт","КВЕД"]
    codes = ["name","email","n_staff","turnover","kved"]
    for i in range(len(titles)):
        dict_={"name":titles[i],"slug":codes[i]}
        start_options.append(dict_)
    return start_options

def main_step():
    # --------parameters-------
    # Зробити функцію, яка віддає словник
    question_title = ["Аналіз","Стратегія","Продукти","Ресурси","Індикація"]
    question_code = ["a","s","p","r","in"]

    # Структура кнопок АСПІРИн
    main_options = []
    for i in range(len(question_title)):
        dict_={"name":question_title[i],"slug":question_code[i],"childs":None}
        main_options.append(dict_)
    # --------parameters-------
    return main_options


def document_step():
    document_title = ["Отримати документ","Відправити документ"]
    document_code = ["get","send"]
    document_options = []
    for i in range(len(document_code)):
        dict_={"name":document_title[i],"slug":document_code[i],"childs":None}
        document_options.append(dict_)
    return document_options

print((start_step()))
print(main_step())


def get_list(dct):
    lst = []
    for el in dct:
        lst.append(el["slug"])
    return lst

print(get_list(start_step()))
print(get_list(main_step()))



def stage_check(id):
    question_code = get_list(main_step())
    codes = get_list(start_step())
    # перевіряємо, чи виконані умови
    
    f = open('c:/work/python/aspirin/users_data.csv','r')
    string = ''
    question_code_n = []
    reg_code_n = []
    
    for el in range(len(codes)):
        reg_code_n.append(0)
    
    for el in range(len(get_list(main_step()))):
        question_code_n.append(0)

    # Проходимося по файлу
    for line in f:
        elems = line.split(';')
        print(elems)
        for code in range(len(codes)):
            # Якщо 0 елемент відповідає id а 1-й відповідає коду - в список за номером індексу привалснюємо значення 1.
            if int(elems[0])== int(id) and elems[1] == codes[code]:
                reg_code_n[code] = 1

        for code in range(len(get_list(main_step()))):
            # Перевіряємо
            if int(elems[0])== int(id) and elems[1] == get_list(main_step())[code]:
                question_code_n[code] = 1
        
        
        print(reg_code_n)
    
    
    stage_out = 3
    # Якщо є хоч один елемент в блоці реєстрації
    for n in reg_code_n:
        if n == 0:
            stage_out = 1
            break
    
    if stage_out == 3:
        # Якщо є хоч один елемент в блоці питань
        for n in question_code_n:
            if n == 0:
                stage_out = 2
                break
    return stage_out


def getemail(id):
    f = open('c:/work/python/aspirin/users_data.csv','r')
    email_out = ''
    for line in f:
        elems = line.split(";")
        if int(elems[0])== int(id) and elems[1] == 'email':
            email_out = elems[2]
    return email_out

print(stage_check(394735340))


def start_code_check(id):
    f = open('c:/work/python/aspirin/users_data.csv','r')
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



