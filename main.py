import requests
import random
import string
import threading
from itertools import cycle
import json
from colorama import Fore
import os
os.system('color')




with open('config.json') as json_file:
    data = json.load(json_file)



devmode = False


if devmode:
    devmode = True
if data['threads'] >300:
    print(f"{Fore.RED}[WARNING] Threads under 300 is not suggested, for faster generation times please use 300+ threads.{Fore.RESET}")
if data['usernamevar'] == '':
    print(f"{Fore.RED}[WARNING] CRITICAL ERROR: No data was found in the config.json file!  The generation tool will not work, please enter the stated values.")
if data['usernamevar'] == '':
    print(f"{Fore.RED}[WARNING] CRITICAL ERROR: No data was found in the config.json file for the Username config!  The generation tool will not work, please enter the stated values.")
if data['emailvar'] == '':
    print(f"{Fore.RED}[WARNING] CRITICAL ERROR: No data was found in the config.json file for the Email config!  The generation tool will not work, please enter the stated values.")
if data['password'] == '':
    print(f"{Fore.RED}[WARNING] CRITICAL ERROR: No data was found in the config.json file for the Password config!  The generation tool will not work, please enter the stated values.")

threads = data['threads']



print(f"""{Fore.BLUE}
▄ •▄  ▄▄▄·  ▄ .▄            ▄▄▄▄▄     ▄▄▄·  ▄▄·  ▄▄·       ▄• ▄▌ ▐ ▄ ▄▄▄▄▄     ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
█▌▄▌▪▐█ ▀█ ██▪▐█▪     ▪     •██      ▐█ ▀█ ▐█ ▌▪▐█ ▌▪▪     █▪██▌•█▌▐█•██      ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
▐▀▀▄·▄█▀▀█ ██▀▐█ ▄█▀▄  ▄█▀▄  ▐█.▪    ▄█▀▀█ ██ ▄▄██ ▄▄ ▄█▀▄ █▌▐█▌▐█▐▐▌ ▐█.▪    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█.█▌▐█ ▪▐▌██▌▐▀▐█▌.▐▌▐█▌.▐▌ ▐█▌·    ▐█ ▪▐▌▐███▌▐███▌▐█▌.▐▌▐█▄█▌██▐█▌ ▐█▌·    ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
·▀  ▀ ▀  ▀ ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪ ▀▀▀      ▀  ▀ ·▀▀▀ ·▀▀▀  ▀█▄▀▪ ▀▀▀ ▀▀ █▪ ▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
Version 1.3.7


""")


def createaccount():
    while True:
        try:
            with open('config.json') as json_file:
                data = json.load(json_file)

            username = data['usernamevar'] + "_" + ''.join(random.choice(string.ascii_letters) for i in range(5))
            email = data['emailvar']
            password = data['password']

            data = {
                'email': email + '_' + ''.join(random.choice(string.ascii_letters) for i in range(5)),
                'password': password,
                'primary_usage': "teacher",
                'primary_usage_type': "SCHOOL",
                'username': f'{username}',
            }
            createaccount = requests.post('https://create.kahoot.it/rest/users', json=data)
            if createaccount.status_code == 200:
                print(f"{Fore.GREEN}[ + ] Account Generated: {username}{Fore.RESET}")
                open('kahoot_accounts.txt', 'a').write(username + ":" + email + '\n')
            else:
                if devmode:
                    print(f'{Fore.RED}[ - ] Account Generation Failed: {createaccount.status_code}{Fore.RESET}')
                else:
                    x = 'test'
        except Exception as err:
            print(err)
for i in range(threads):
    t1 = threading.Thread(target=createaccount).start()
