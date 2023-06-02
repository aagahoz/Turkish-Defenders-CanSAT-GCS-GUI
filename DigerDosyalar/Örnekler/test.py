import matplotlib.pyplot as plt

def plot_graph(data):
    data_list = data.split(',')
    # None değerlerini boşluk olarak değiştir
    data_list = [float(item) if item.strip() != 'None' and item.strip() != '' else None for item in data_list]

    # X eksenindeki değerlerin uzunluğu
    x = list(range(len(data_list)))

    # Çizgi grafiğini oluştur
    plt.plot(x, data_list)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Vibration Test - AccelZ Graphic')

    # Grafiği göster
    plt.show()

# Dosyadan verileri oku
with open('/Users/agahozdemir/Desktop/test_datas/titresim_test/accelZ.txt', 'r') as file:
    data = file.read()

# Grafiği çiz
plot_graph(data)

