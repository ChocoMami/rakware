from subprocess import Popen
import re
import os

folders = ["routes", "logs", "config", "accounts", "logs//Phoenix", "logs//Tucson", "logs//Scottdale", "logs//Chandler", "logs//Brainburg", "logs//Saint-Rose", "logs//Mesa", "logs//Red-Rock", "logs//Yuma", "logs//Surprise", "logs//Prescott", "logs//Glendale", "logs//Kingman", "logs//Winslow", "logs//Payson", "logs//Gilbert", "logs//Show-Low", "logs//Page", "logs//Casa-Grande", "logs//Queen-Creek", "logs//Sun-City", "logs//Sedona", "logs//Holiday", "logs//Wednesday"]

while True:
    print('0 - Выйти')
    print('1 - Папки')
    print('2 - Кфг')
    cmd = input("Выберите тип восстановления: ")
    if cmd == '1':
        for folder in folders:
            if not os.path.exists(folder):
                os.mkdir(folder)
    elif cmd == '2':
        if not os.path.exists('config'):
            os.mkdir('config')
            file = open("config//RakWare Settings.ini", "w")
            file.write("[settings]\npass=PASSWORD\nfinishaction=0\nrandomexit=1\nslapfix=1\nworkmode=1\nrandomnick=1\nrandompass=0\nlauncher=1\nlvlprokachki=5\ndemorganlimit=120\nroutedelay=60\nlogchat=1\n\n[telegram]\ntokenbot=TOKEN https://t.me/BotFather\nchatid=CHAT ID https://t.me/getmyid_bot\nadmsobesuveda=0\nadmspawnuveda=0\nadmtpuveda=0\nadmcoordtpuveda=0\nadminkpzuveda=0\njailuveda=1\nloginuveda=1\nreguveda=1\nnoipbanuveda=1\nipbanuveda=1\nkickuveda=1\nssakkuveda=1\nlevelupuveda=1\n\n[sampstore]\nvilagivat=0\nsampstoretoken=TOKEN SAMP STORE\nprice=10\ninfopokupo=\ninfoakk=6 лвл | 1кк | Для любых целей\n\n[proxy]\nzahodsproxy=0\nproxyip=PROXY IP\nproxyuser=PROXY USERNAME\nproxypass=PROXY PASSWORD\n\n[promo]\nphoenix=babetape\ntucson=берлога\nscottdale=steve\nchandler=richilox\nbrainburg=bobylew\nsaintrose=dante\nmesa=romero\nredrock=bratok\nyuma=revazz\nsurprise=ettore\nprescott=aher1337\nglendale=РИНЖИ\nkingman=aher\nwinslow=seller\npayson=isynory\ngilbert=babetape\nshowlow=морти\ncasagrande=Венни\npage=лудоман\nsuncity=сига\nqueencreek=covalli\nsedona=jeezly\nholiday=seller\nwednesday=mason\n\n[referal]\nphoenix=Farmila_Referal\ntucson=Farmila_Referal\nscottdale=Farmila_Referal\nchandler=Farmila_Referal\nbrainburg=Farmila_Referal\nsaintrose=Farmila_Referal\nmesa=Farmila_Referal\nredrock=Farmila_Referal\nyuma=Farmila_Referal\nsurprise=Farmila_Referal\nprescott=Farmila_Referal\nglendale=Farmila_Referal\nkingman=Farmila_Referal\nwinslow=Farmila_Referal\npayson=Farmila_Referal\ngilbert=Farmila_Referal\nshowlow=Farmila_Referal\ncasagrande=Farmila_Referal\npage=Farmila_Referal\nsuncity=Farmila_Referal\nqueencreek=Farmila_Referal\nsedona=Farmila_Referal\nholiday=Farmila_Referal\nwednesday=Farmila_Referal")
            file.close()
        else:
            file = open("config//RakWare Settings.ini", "w")
            file.write("[settings]\npass=PASSWORD\nfinishaction=0\nrandomexit=1\nslapfix=1\nworkmode=1\nrandomnick=1\nrandompass=0\nlauncher=1\nlvlprokachki=5\ndemorganlimit=120\nroutedelay=60\nlogchat=1\n\n[telegram]\ntokenbot=TOKEN https://t.me/BotFather\nchatid=CHAT ID https://t.me/getmyid_bot\nadmsobesuveda=0\nadmspawnuveda=0\nadmtpuveda=0\nadmcoordtpuveda=0\nadminkpzuveda=0\njailuveda=1\nloginuveda=1\nreguveda=1\nnoipbanuveda=1\nipbanuveda=1\nkickuveda=1\nssakkuveda=1\nlevelupuveda=1\n\n[sampstore]\nvilagivat=0\nsampstoretoken=TOKEN SAMP STORE\nprice=10\ninfopokupo=\ninfoakk=6 лвл | 1кк | Для любых целей\n\n[proxy]\nzahodsproxy=0\nproxyip=PROXY IP\nproxyuser=PROXY USERNAME\nproxypass=PROXY PASSWORD\n\n[promo]\nphoenix=babetape\ntucson=берлога\nscottdale=steve\nchandler=richilox\nbrainburg=bobylew\nsaintrose=dante\nmesa=romero\nredrock=bratok\nyuma=revazz\nsurprise=ettore\nprescott=aher1337\nglendale=РИНЖИ\nkingman=aher\nwinslow=seller\npayson=isynory\ngilbert=babetape\nshowlow=морти\ncasagrande=Венни\npage=лудоман\nsuncity=сига\nqueencreek=covalli\nsedona=jeezly\nholiday=seller\nwednesday=mason\n\n[referal]\nphoenix=Farmila_Referal\ntucson=Farmila_Referal\nscottdale=Farmila_Referal\nchandler=Farmila_Referal\nbrainburg=Farmila_Referal\nsaintrose=Farmila_Referal\nmesa=Farmila_Referal\nredrock=Farmila_Referal\nyuma=Farmila_Referal\nsurprise=Farmila_Referal\nprescott=Farmila_Referal\nglendale=Farmila_Referal\nkingman=Farmila_Referal\nwinslow=Farmila_Referal\npayson=Farmila_Referal\ngilbert=Farmila_Referal\nshowlow=Farmila_Referal\ncasagrande=Farmila_Referal\npage=Farmila_Referal\nsuncity=Farmila_Referal\nqueencreek=Farmila_Referal\nsedona=Farmila_Referal\nholiday=Farmila_Referal\nwednesday=Farmila_Referal")
            file.close()
    elif cmd == '0':
        break
