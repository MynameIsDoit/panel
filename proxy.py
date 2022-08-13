import os, time, requests, pystyle, random, datetime

from pystyle import *
from console.utils import set_title

def cls():
    os.system('cls')

def pause():
    os.system('pause >nul')

h_h2 = ["Halal", "Haram"]

now = datetime.datetime.now()

cls()
os.system('mode 85, 25')
banner = '''AUTO PROXY SCARPER'''
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))
Write.Print("This program is: ", Colors.purple_to_blue, interval=0)
Write.Print(f"{random.choice(h_h2)}\n", Colors.green_to_white, interval=0)
Write.Print("Started at: " + now.strftime("%Y/%m/%d %H:%M:%S\n"), Colors.purple_to_blue , interval=0)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Scraping Proxies . . .")
Write.Print("[?] Scraping Proxies . . .\n", Colors.red_to_yellow, interval=0)

http = open('proxy.txt','wb')

# HTTP Proxies Sources
h = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt")
h1 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt")
h2 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
h3 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt")
h4 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt")
h5 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt")
h6 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt")
h7 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
h8 = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
h9 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
h10 = requests.get("https://www.proxyscan.io/download?type=http")
h11 = requests.get("https://www.proxyscan.io/download?type=https")
h12 = requests.get("https://api.openproxylist.xyz/http.txt")

set_title(f"Bloody Proxy Scraper V2 | Made By: Bloody | Scraped HTTP Proxies!")
Write.Print("\n[?] Scraped HTTP Proxies!\n", Colors.red_to_yellow, interval=0)

Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
time.sleep(1)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Writing Proxies . . .")
Write.Print("[?] Writing Proxies In Files . . .\n\n", Colors.red_to_yellow, interval=0)
time.sleep(1)

# Writing Proxies In Their Files
# Writing HTTP Proxies
http.write(h.content)
http.write(h1.content)
http.write(h2.content)
http.write(h3.content)
http.write(h4.content)
http.write(h5.content)
http.write(h6.content)
http.write(h7.content)
http.write(h8.content)
http.write(h9.content)
http.write(h10.content)
http.write(h11.content)
http.write(h12.content)
Write.Print("[?] Wrote HTTP Proxies!\n", Colors.red_to_yellow, interval=0)

set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Wrote Proxies!")
Write.Print("[!] Finished Writing Proxies In Files!\n", Colors.green_to_white, interval=0)
Write.Print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n", Colors.rainbow, interval=0)
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Closing Files . . .")
Write.Print("[?] Closing Files . . .\n", Colors.red_to_yellow, interval=0)

# Closing Files
http.close()

# Done!
set_title("Bloody Proxy Scraper V2 | Made By: Bloody | Finished!")
Write.Print("[!] Successfully Scraped And Saved Proxies!\n\n", Colors.green_to_white, interval=0)
Write.Print("Press any key to continue . . .", Colors.green_to_white, interval=0)
pause()
