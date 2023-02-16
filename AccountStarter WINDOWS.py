from subprocess import Popen
import re
import os

while True:
    cmd = input("Выберите лвл аккаунтов: ")
    if cmd != '0':
        if os.path.exists('accounts\\Upgraded_Accounts_lvl' + cmd + '.txt'):
            text = open('accounts\\Upgraded_Accounts_lvl' + cmd + '.txt','r').readlines()
            for line in text:
                match_object = re.match("(.*) \| (.*) \| (.*):7777 \| (.*) \| (.*)", line)
                if match_object:
                      Popen(f'"RakSAMP Lite.exe" -n {match_object.group(1)} -h {match_object.group(3)} -p 7777')
        else:
            print('Аккаунтов с таким уровнем нет')
    else:
        break
