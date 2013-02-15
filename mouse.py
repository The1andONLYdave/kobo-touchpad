#!/usr/bin/env python
import getpass
import sys
import telnetlib
import win32api, win32con

def move(x,y):
    win32api.SetCursorPos((x,y))
move(10,10)

def click(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,xx,yy,0,0) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,xx,yy,0,0)

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
  
  newx = x[2].strip(' y') 
  newy = x[3].strip(' p')
  #newp = x[4].strip(' ')

  # get cursor position on desktop
  xx, yy = win32api.GetCursorPos()

  if lastx < newx : xx=xx+10
  if lastx > newx : xx=xx-10
  #if lastx == newx : print ('x =')
  
  if lasty < newy : yy=yy+10
  if lasty > newy : yy=yy-10
  #if lasty == newy : print ('y =')
  
  #if lastp < newp : 
  #if lastp > newp : click(xx,yy)
  #if lastp == newp : print ('p =')
  
  #move(xx,yy)
  win32api.SetCursorPos((xx,yy)) 
  
  lastx = newx
  lasty = newy
  #lastp = newp
  
  #if except (socket.error, EOFError):
   # break
