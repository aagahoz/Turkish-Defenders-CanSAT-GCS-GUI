import socket

# Server'ın IP adresi ve portu
HOST = 'localhost'
PORT = 5555

# TCP/IP soketi oluşturma
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Server'a bağlanma
    s.connect((HOST, PORT))
    # Veri gönderme
    s.sendall(b'Merhaba, server!')
    # Veri alımı
    data = s.recv(1024)

print('Alınan veri:', data.decode())
