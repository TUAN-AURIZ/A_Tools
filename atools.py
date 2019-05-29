from time import sleep
import os
import sys

#AURIZ GANS & TAMVANS TIADA TARA QYMAK
#     ___           ___           ___                       ___
#    /\  \         /\  \         /\  \                     /\__\
#   /::\  \        \:\  \       /::\  \       ___         /::|  |
#  /:/\:\  \        \:\  \     /:/\:\__\     /\__\       /:/:|  |
# /:/ /::\  \   ___  \:\  \   /:/ /:/  /    /:/__/      /:/|:|  |__
#/:/_/:/\:\__\ /\  \  \:\__\ /:/_/:/__/___ /::\  \     /:/ |:| /\__\
#\:\/:/  \/__/ \:\  \ /:/  / \:\/:::::/  / \/\:\  \__  \/__|:|/:/  /
# \::/__/       \:\  /:/  /   \::/~~/~~~~   ~~\:\/\__\     |:/:/  /
#  \:\  \        \:\/:/  /     \:\~~\          \::/  /     |::/  /
#   \:\__\        \::/  /       \:\__\         /:/  /      |:/  /
#    \/__/         \/__/         \/__/         \/__/       |/__/
#JANGAN RECODE YA GOBLOK,GUA 3 HARI BIKIN,LU ENAK RECODE


#wrn
if sys.platform == "linux2" or sys.platform == "linux":
        R = ("\033[31m")
        W = ("\033[0;1m")
        B = ("\033[35m")
        G = ("\033[32m")
        glp = ("\033[2m")
        Y = ("\033[33;1m")
else:
        R = ""
        W = ""
        Y = ""
        B = ""
        G = ""
        glp = ""


os.system("clear")
sleep(0.5)
print (R+'█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█')
sleep(0.5)
print ('█-----╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗-----█')
sleep(0.5)
print ('█-----║║║╠─║─║─║║║║║╠─-----█')
sleep(0.5)
print ('█-----╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝-----█')
sleep(0.5)
print ('█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█')
sleep(1)
nama = input('SIAPA NAMA KAKAK: ')
os.system('clear')
sleep(1)
print (Y+'Loading..........')
sleep(2)
print ('█████████     [LOADING... USER:',nama,']')
sleep(2)
print ('█▄█████▄█     [LOGIN USER',nama,']')
sleep(2)
print ('█▼▼▼▼▼        [LOGIN BERHASIL,WELCOME',nama,']')
sleep (1)
print ('█')
sleep(1)
print (' AURIZ TOOLS')
sleep(1)
print ('█▲▲▲▲▲')
sleep(1)
print ('█████████')
sleep(1)
print (' ██ ██')

text = ('''
╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾
╾SUBSCRIBE CHANNEL: TN AURIZ  ╾
╾LEADER IN GARUDA TEAM COMANDO╾
╾THANKS TO ALL MY FRIEND      ╾
╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾
''')
print (text)
sleep(2)
menu = '''
1.install PHP
2.cmatrix
3.tools SQLmap
4.web vuln deface webdav
5.Tools Webdav

0.exit
'''
def main():
   print (menu)
   pilihan = input('Pilih menu nya: ')

#input ke 1

   if pilihan == '1' or pilihan == '01':
      print (B+'installing php')
      sleep(2)
      os.system('apt update && apt upgrade')
      os.system('pkg install php -y')
      sleep(2)
      print (Y+'Selesai Kakak',nama,'jones:v')

#input ke 2

   elif pilihan == '2' or pilihan == '02':
      print (Y+'Installing cmatrix....')
      sleep(2)
      os.system('pkg install cmatrix')
      sleep(1)
      os.system('clear')
      sleep(1)
      print (Y+'''
SUDAH TERINSTALL
SILAHKAN KETIK:

cmatrix

#note:untuk menghentikannya tekan CTRL + C
''')
#input ke 3

   elif pilihan == '3' or pilihan == '03':
      print (Y+'Installing sqlmap....')
      sleep(2)
      os.system('git clone https://github.com/sqlmapproject/sqlmap')
      sleep(1)
      os.system('clear')
      sleep(2)
      print (Y+'''
SUDAH TERINSTALL
SILAHKAN KETIK:

cd sqlmap
ls
python2 sqlmap.py -u namaweb.com --dbs

#note:pastikan web vuln SQL
''')
#input ke 4

   elif pilihan == '4' or pilihan == '04':
        os.system('clear')
        sleep(1.5)
        print ('╔═══╗╔╗─╔╗╔═══╗╔══╗╔════╗')
        sleep(0.5)
        print ('║╔═╗║║║─║║║╔═╗║╚╣─╝╚══╗═║')
        sleep(0.5)
        print ('║║─║║║║─║║║╚═╝║─║║───╔╝╔╝')
        sleep(0.5)
        print ('║╚═╝║║║─║║║╔╗╔╝─║║──╔╝╔╝─')
        sleep(0.5)
        print ('║╔═╗║║╚═╝║║║║╚╗╔╣─╗╔╝═╚═╗')
        sleep(0.5)
        print ('╚╝─╚╝╚═══╝╚╝╚═╝╚══╝╚════╝')
        sleep(0.5)
        print ('''
KUMPULAN LINK VULN DEFACE WEBDAV

http://colourfactory.co.za
http://whosting.co.za
http://whadiz.com
http://thepremiummakers.com
http://totemafrica.com
http://ospreygroup.co.za
http://trafficam.co.za
http://ittrader.co.za
http://stand66.com
http://ziady.com
http://8x8.co.za
http://megro.co.za
http://kwalitycommodities.co.za
http://lpenterprises.co.za
http://lwrm.co.za
http://handj.co.za
http://allpaint.co.za

''')
   elif pilihan == '5'or pilihan == '05':
      os.system('clear')
      sleep(1)
      print ('loading......')
      sleep(1)
      os.system('sh w.sh')

   elif pilihan == '0':
      print ('Berhasil Keluar Dari Tools..Bye Bye..')
   else:
       print ('ERROR!!...wrong input!!')


main()
