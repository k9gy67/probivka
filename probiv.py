import webbrowser
import time
import os

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
`:`:::::::`;:::::: ;::::::#/               DOO 
:::`:::::::`;; ;:::::::::##                OO 
::::`:::::::`;::::::::;:::#                OO 
`:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:# 
   ::::::`:::::;'  /  /   `#
      """)
print(r"""
      доступные функции:
      пробив
      бомбер
      """)
func = input("введите функцию: ")
if func == "пробив":
    print(r"""
          доступные соцсети:
          телеграм
          тик ток
          гугл(поиск во всех соцсетях)
          """)
    soc = input("введите соцсеть: ")
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
elif func == "бомбер":
    print("зайдите в чат туда куда нужно отправить бомбер(у вас должен быть скачан space_test.vbs с моего акка в гитхабу в том же посте)")
    time.sleep(5)
    for i in range(500000000):
        os.system('wscript space_test.vbs')