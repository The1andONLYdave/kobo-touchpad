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

tn.write("hexdump  /dev/input/event0\n")

print tn.read_lazy()

print tn.read_until("0000000", 10) #first button press

print ('To exit press 60 sec no button or strg+c and then button')
while True:
  x = tn.read_until("\n", 60)
  # TODO: exception handling if incorrect string
  #char 35,36 should be '6' each, 41 is '1' for click, '0' release click

  xx, yy = win32api.GetCursorPos()
  if x[41] == '1' : win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,xx,yy,0,0) 
  if x[41] == '0' : win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,xx,yy,0,0) 