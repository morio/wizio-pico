# Raspberry Pi Pico development platform for PlatformIO

**A few words in the beginning**
* **Version: 0.0.7** The project is a work in progress and is very beta version - there may be bugs...
* This project not an official platform and is based on [**pico-sdk**](https://github.com/raspberrypi/pico-sdk)
* Frameworks:
* * Baremetal ( pico-sdk as is, [TinyUSB](https://github.com/raspberrypi/tinyusb/tree/e0aa405d19e35dbf58cf502b8106455c1a3c2a5c) present but is not linked ) 
* * Arduino ( Basic - Serial, GPIO ... in progress, will upload later )
* Windows, Linux, macOS
* Read WIKI
* [Baremetal Examples](https://github.com/raspberrypi/pico-examples)
* Note: _Home office, it's hard for me to test any hardware_

## Install Platform

_Python 2 & 3 compatable in process, if issue - report_

PIO Home > Platforms > Advanced Installation 

paste https://github.com/Wiz-IO/wizio-pico

## INI file
```ini
[env:pico]
platform = wizio-pico
board = pico
framework = baremetal
upload_port   = select PICO-DRIVE:/ or select HARD-DRIVE:/ to save the UF2 file ( example C:/ )
monitor_port  = COMx
monitor_speed = 115200
```


## Thanks to

* [Ivan Kravets ( PlatformIO )](https://platformio.org/)
* [Comet Electronics](https://www.comet.bg/en/)

>If you want to help / support:   
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ESUP9LCZMZTD6)
