#!/usr/bin/env python
import getpass
import sys
import telnetlib
import win32api, win32con

HOST = "192.168.0.30"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write("root\n")

tn.write("killall nickel\n")
tn.write("cat /mnt/onboard/screen | /usr/local/Kobo/pickel showpic\n")

tn.write("evtest /dev/input/event1\n")

print tn.read_lazy()
print tn.read_until("Testing ...", 3)

print ('To exit press 60 sec no touchpad or strg+c and then touchpad')
lastx=0
lastp=0
lasty=0
while True:
  x = tn.read_until("------------", 60)
  # TODO: exception handling if incorrect string
  x=x.strip(' ')
  x=x.strip('-')
  x=x.split(':')
  
  print('x y p')
  print x[2].strip(' y') 
  print x[3].strip(' p')
  print x[4].strip(' ')
  
  #if except (socket.error, EOFError):
   # break
