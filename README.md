# DSCUSB
Python code to establish connection with DSCUSB sensors

## Requirements

* 32-bit Python 
* [DSCUSB Driver or Toolkit](https://www.mantracourt.com/software/dscusb/dsc-usb-toolkit)
* [MantraASCII2Drv](https://www.mantracourt.com/software/dsc-digital-strain-card/dll-driver-2)


## Set up

Install both drivers before connecting your device. Connect your device and let the drivers update automatically. Go to Device manager and check in which port has your device been connected under the section Ports (COM & LPT), COM4 in this example.

![image](https://user-images.githubusercontent.com/59921026/127021602-fd27aadc-d461-48a8-b467-b5e2f3203ae2.png)

Once the device is configured find the file MantraASCII2Drv.dll in your system and copy it in the directory **"C:\Windows\System32\"**. Now you are ready to clone the github repository in your computer and run the file **main.py** which contains a simple code to check that everythign is running. Feel free to change this file to your requirements!

## Useful links

* [DSCUSB User Manual](https://www.mantracourt.com/userfiles/documents/dscusbadvancedmanual.pdf)
* [Python ctypes](https://docs.python.org/3/library/ctypes.html)
