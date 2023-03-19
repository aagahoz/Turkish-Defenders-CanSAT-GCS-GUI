import serial
import time
import random

ser = serial.Serial('/dev/ttyUSB2', 9600, timeout=1) # Sanal portu açın, port numarası ve baud hızı belirleyin

while True:
    data = random.randint(0, 255) # Rastgele bir veri oluşturun
    ser.write(bytes([data])) # Veriyi seri porta gönderin
    time.sleep(0.1) # 0.1 saniye bekle
