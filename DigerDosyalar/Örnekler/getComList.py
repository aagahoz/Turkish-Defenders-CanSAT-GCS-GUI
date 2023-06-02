# get com list 

import serial.tools.list_ports

def getComList():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    return connected

def getUsbSerialDevices(comList):
    usbSerialDevices = {}
    # /dev/cu.usbserial-A50285BI : A50285BI

    for com in comList:
        # sadece usb seriali al
        if "usbserial" in com:
            # /dev/cu.usbserial-A50285BI
            # A50285BI
            usbSerialDevices[com] = com.split("-")[1]
            usbSerialDevices[com] = "COM - " + usbSerialDevices[com]
    return usbSerialDevices

print(getComList())

