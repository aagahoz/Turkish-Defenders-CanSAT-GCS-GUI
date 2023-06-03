import serial
import time
import serial.tools.list_ports

def takeData():
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
            except UnicodeDecodeError:
                print("Hata: Geçersiz karakter kodlaması")
                print("\n" * 5)  # 5 satır boşluk ekle
                continue

def sendData():
    while True:
        data = "!000111010+\n"
        ser.write(b"!000111010+\n")
        print(len(data))
        time.sleep(0.5)

def sendMixData():
    while True:
        ser.write(b"!000asd111010+\n")
        print(len(b"!000asd111010+\n"))

        time.sleep(0.5)

        ser.write(b"xxxxxxxxxxxxxxxx\n")
        print(len(b"xxxxxxxxxxxxxxxx\n"))
        time.sleep(0.5)

        ser.write(b"!000111010+\n")
        print(len(b"!000111010+\n"))
        time.sleep(0.5)

def sendAndTake():
    while True:
        ser.write(b"!000111010+\n")
        print(len(b"!000111010+\n"))
        time.sleep(1)
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
            except UnicodeDecodeError:
                print("Hata: Geçersiz karakter kodlaması")
                print("\n" * 5)  # 5 satır boşluk ekle
                continue

def getComList():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    return connected


def takeInputAndSendCommand(serialPort):

    while True:
        print()
        print(" ** Komutun sürekli olarak gönderilmesi için 0, sürekli yeniden istenmesi için 1 giriniz")

        print()
        surekliIstemeAktifMi = int(input("---->>> MOD giriniz: "))

        if surekliIstemeAktifMi == 1:
            while True:
                print("-- Komutlar --")
                print("Simulasyon Enable Etmek için - 1")
                print("Simulasyon Aktif Etmek için - 2")
                print("Simulasyon Pasif Etmek için - 3")
                print("Normal Mod Aktif Etmek için - 4")
                print("Normal Mod Pasif Etmek için - 5")


                print("Servo Dondurmek için - 6")
                print("DC Motor Dondurmek için - 7")
                print("PARAUST ACMA için -8")
                print("UPRIGHTS ACMA için -9")
                print("BUZZER ACMA için -10")

                print("Servo KAPATMAK için - 11")
                print("DC Motor KAPATMAK için - 12")
                print("PARAUST KAPATMAK için -13")
                print("UPRIGHTS KAPATMAK için -14")
                print("BUZZER KAPATMAK için -15")
                
                


                
                komut = int(input("Komut giriniz: "))

                if komut == 1:
                    print("Seçildi -> Simulasyon Enable")
                    serialPort.write(b"Simulasyon Enable\n")
                    break

                elif komut == 2:
                    print("Seçildi -> Simulasyon Aktif")
                    serialPort.write(b"Simulasyon Aktif\n")
                    break

                elif komut == 3:
                    print("Seçildi -> Simulasyon Pasif")
                    serialPort.write(b"Simulasyon Pasif\n")
                    break

                elif komut == 4:
                    print("Seçildi -> Normal Mod Aktif")
                    serialPort.write(b"Normal Mod Aktif\n")
                    break

                elif komut == 5:
                    print("Seçildi -> Normal Mod Pasif")
                    serialPort.write(b"Normal Mod Pasif\n")
                    break
                

                # SENSOR KOMUT
                elif komut == 6:
                    print("Seçildi -> Servo Dondurme Seçildi\n")
                    serialPort.write(b"SERVO")
                    break

                elif komut == 7:
                    print("Seçildi -> DC Motor Dondurme Secildi\n")
                    serialPort.write(b"DC")
                    break

                elif komut == 8:
                    print("Seçildi -> PARASUT AÇMA Secildi\n")
                    serialPort.write(b"PARASUT")
                    break

                elif komut == 9:
                    print("Seçildi -> UPRAIGHT AÇMA Seçildi\n")
                    serialPort.write(b"UPRIGHT")
                    break

                elif komut == 10:
                    print("Seçildi -> BUZZER AÇMA Seçildi\n")
                    serialPort.write(b"BUZZER")
                    break



                # ! KAPATMA

                elif komut == 11:
                    print("Seçildi -> Servo Dondurme Seçildi\n")
                    serialPort.write(b"SERVOOFF")
                    break

                elif komut == 12:
                    print("Seçildi -> DC Motor Dondurme Secildi\n")
                    serialPort.write(b"DCOFF")
                    break

                elif komut == 13:
                    print("Seçildi -> PARASUT AÇMA Secildi\n")
                    serialPort.write(b"PARASUTOFF")
                    break

                elif komut == 14:
                    print("Seçildi -> UPRAIGHT AÇMA Seçildi\n")
                    serialPort.write(b"UPRIGHTOFF")
                    break

                elif komut == 15:
                    print("Seçildi -> BUZZER AÇMA Seçildi\n")
                    serialPort.write(b"BUZZEROFF")
                    break

             
                


                time.sleep(1)


        elif surekliIstemeAktifMi == 0:
            print("-- Komutlar --")
            print("Simulasyon Enable Etmek için - 1")
            print("Simulasyon Aktif Etmek için - 2")
            print("Simulasyon Pasif Etmek için - 3")
            print("Normal Mod Aktif Etmek için - 4")
            print("Normal Mod Pasif Etmek için - 5")


            print("Servo Dondurmek için - 6")
            print("DC Motor Dondurmek için - 7")
            print("PARAUST ACMA için -8")
            print("UPRIGHTS ACMA için -9")
            print("BUZZER ACMA için -10")

            print("Servo KAPATMAK için - 11")
            print("DC Motor KAPATMAK için - 12")
            print("PARAUST KAPATMAK için -13")
            print("UPRIGHTS KAPATMAK için -14")
            print("BUZZER KAPATMAK için -15")
            
            

            print()

            komut = int(input("Komut giriniz: "))

            while True:


                if komut == 1:
                    print("Seçildi -> Simulasyon Enable")
                    serialPort.write(b"Simulasyon Enable\n")

                elif komut == 2:
                    print("Seçildi -> Simulasyon Aktif")
                    serialPort.write(b"Simulasyon Aktif\n")

                elif komut == 3:
                    print("Seçildi -> Simulasyon Pasif")
                    serialPort.write(b"Simulasyon Pasif\n")

                elif komut == 4:
                    print("Seçildi -> Normal Mod Aktif")
                    serialPort.write(b"Normal Mod Aktif\n")

                elif komut == 5:
                    print("Seçildi -> Normal Mod Pasif")
                    serialPort.write(b"Normal Mod Pasif\n")

                # SENSOR KOMUT
                elif komut == 6:
                    print("Seçildi -> Servo Dondurme Seçildi\n")
                    serialPort.write(b"SERVO")

                elif komut == 7:
                    print("Seçildi -> DC Motor Dondurme Secildi\n")
                    serialPort.write(b"DC")

                elif komut == 8:
                    print("Seçildi -> PARASUT AÇMA Secildi\n")
                    serialPort.write(b"PARASUT")

                elif komut == 9:
                    print("Seçildi -> UPRAIGHT AÇMA Seçildi\n")
                    serialPort.write(b"UPRIGHT")

                elif komut == 10:
                    print("Seçildi -> BUZZER AÇMA Seçildi\n")
                    serialPort.write(b"BUZZER")



                # ! KAPATMA

                elif komut == 11:
                    print("Seçildi -> Servo Dondurme Seçildi")
                    serialPort.write(b"SERVOOFF\n")

                elif komut == 12:
                    print("Seçildi -> DC Motor Dondurme Secildi")
                    serialPort.write(b"DCOFF\n")

                elif komut == 13:
                    print("Seçildi -> PARASUT AÇMA Secildi")
                    serialPort.write(b"PARASUTOFF\n")

                elif komut == 14:
                    print("Seçildi -> UPRAIGHT AÇMA Seçildi")
                    serialPort.write(b"UPRIGHTOFF\n")

                elif komut == 15:
                    print("Seçildi -> BUZZER AÇMA Seçildi")
                    serialPort.write(b"BUZZEROFF\n0")

                time.sleep(1)


        else:
            print("Geçersiz mod seçildi. Lütfen tekrar deneyin.")



















isPortActive = False

com_ports = getComList()
print("Portlar : ")
for i in com_ports:
    print(i)
    
try:
    ser = serial.Serial("/dev/cu.usbserial-AH019V3L", 9600, timeout=1) # ! PORTU GİR
    ser.flush()
    isPortActive = True
    print("Connected Port")

except serial.SerialException as e:
    isPortActive = False
    print("     -->> PORT BAGLANMA SORUNU, PORTU DOĞRU GİR 69. Satırda. Portlar zaten outputta var, kopyala ordan ve 69 da gir")


if isPortActive:

    # sendAndTake()
    # sendMixData()
    # takeData()
    # sendData()

    takeInputAndSendCommand(ser)

