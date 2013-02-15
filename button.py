#!/usr/bin/env python
import getpass
import sys
import telnetlib
#import win32api, win32con
import time
#version 0.2 with restart to nickel
HOST = "192.168.0.30"

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write("root\n")

tn.write("killall nickel\n")

tn.write("hexdump  /dev/input/event0\n")

print tn.read_lazy()

print tn.read_until("0000000", 10) #first button press

print ('To exit press 1800 sec no button or strg+c and then button')
while True:
  x = tn.read_until("\n", 1800)
  # TODO: exception handling if incorrect string
  #char 35,36 should be '6' each, 41 is '1' for click, '0' release click

  #added check for char 35
  #if (x[41] == '1') and (x[35] == '6'): 
  if x[41] =='1' :
       tn.close() 
       tn = telnetlib.Telnet(HOST)
       tn.read_until("login: ")
       tn.write("root\n")
       tn.write("killall hexdump\n")
       tn.write("killall nickel\n")
       tn.write("killall hindenburg\n")
       tn.write("killall dbus-uuidgen\n")
       tn.write("killall dbus-daemon\n")
       tn.write("rm -f /var/run/dbus/pid\n")
       tn.write("rm -f /var/run/dbus/system_bus_socket\n")
       tn.write("export QWS_MOUSE_PROTO=\"tslib_nocal:/dev/input/event1\"\n")
       tn.write("export QWS_KEYBOARD=imx508kbd:/dev/input/event0\n export QWS_DISPLAY=Transformed:imx508:Rot90\n export NICKEL_HOME=/mnt/onboard/.kobo\n export LD_LIBRARY_PATH=/usr/local/Kobo\n export WIFI_MODULE_PATH=/drivers/freescale/wifi/ar6000.ko\n export LANG=en_US.UTF-8\n export UBOOT_MMC=/etc/u-boot/freescale/u-boot.mmc\n export UBOOT_RECOVERY=/etc/u-boot/freescale/u-boot.recovery\n /bin/dbus-uuidgen > /var/lib/dbus/machine-id\n /bin/dbus-daemon --system &\n export DBUS_SESSION_BUS_ADDRESS=`/bin/dbus-daemon --session --print-address --fork`\n /usr/local/Kobo/hindenburg &\n /usr/local/Kobo/nickel -qws &\n")
       #tn.write("sh /mnt/onboard/restart-nickel.sh\n")
       tn.read_until("bla this read blocks till nickel restarts")
       
#  if x[41] == '0' :  