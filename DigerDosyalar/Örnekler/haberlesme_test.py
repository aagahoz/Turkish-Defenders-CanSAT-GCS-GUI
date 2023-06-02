import serial
import time

ser = serial.Serial('/dev/tty.usbserial-A50285BI', 9600, timeout=1)

outgoing_data = "!000100000" # Gönderilecek veri


x = 0
while True:

    if x > 9:
        x = 0
    outgoing_data = "!000100000" # Gönderilecek veri

    if ser.in_waiting > 0:
        incoming_data = ser.readline().rstrip().decode()
        print("incoming_data: ", incoming_data)
        incoming_data = ""
    outgoing_data = outgoing_data + str(x) + '+'
    print("sended data : ", outgoing_data)
    ser.write(outgoing_data.encode())
    ser.write(b'\n')
    print("loop  ", x)
    x = x + 1
    time.sleep(1)

