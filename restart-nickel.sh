#!/bin/sh
#sync #in case something goes wrong
#/usr/bin/killall nickel &
#/usr/bin/killall hindenburg &
#/usr/bin/killall dbus-uuidgen &
#/usr/bin/killall dbus-daemon &
#/bin/rm /var/run/dbus/pid
#PLATFORM=freescale

#INTERFACE=wlan0
#WIFI_MODULE=ar6000

#export INTERFACE
#export WIFI_MODULE

export QWS_MOUSE_PROTO="tslib_nocal:/dev/input/event1"
export QWS_KEYBOARD=imx508kbd:/dev/input/event0
export QWS_DISPLAY=Transformed:imx508:Rot90
export NICKEL_HOME=/mnt/onboard/.kobo
export LD_LIBRARY_PATH=/usr/local/Kobo
export WIFI_MODULE_PATH=/drivers/freescale/wifi/ar6000.ko
export LANG=en_US.UTF-8
export UBOOT_MMC=/etc/u-boot/freescale/u-boot.mmc
export UBOOT_RECOVERY=/etc/u-boot/freescale/u-boot.recovery

/bin/dbus-uuidgen > /var/lib/dbus/machine-id
/bin/dbus-daemon --system &
export DBUS_SESSION_BUS_ADDRESS=`/bin/dbus-daemon --session --print-address --fork`

/usr/local/Kobo/hindenburg &
/usr/local/Kobo/nickel -qws &
