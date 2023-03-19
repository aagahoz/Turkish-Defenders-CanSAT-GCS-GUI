import socket

UDP_IP = "127.0.0.1"  # Sunucunun IP adresi
UDP_PORT = 5005      # Sunucunun kullanacağı port numarası

# UDP soketi oluştur
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP adresi ve port numarası ile soketi bağla
sock.bind((UDP_IP, UDP_PORT))

# Veri alma ve gönderme döngüsü
while True:
    # Gelen veriyi al
    data, addr = sock.recvfrom(1024)
    print("Gelen veri: ", data.decode())

    # Gelen veriye cevap ver
    message = "Mesajınızı aldım!"
    sock.sendto(message.encode(), addr)
