import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.count = 0  # Sayacın başlangıç değeri
        self.lbl = QLabel(str(self.count), self)
        self.lbl.move(50, 50)

        # Timer'ın oluşturulması
        self.timer = QTimer()
        self.timer.timeout.connect(self.onTimer)
        self.timer.start(1000)  # Her 1000 milisaniyede bir timeout sinyali gönderir

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt5 Timer Örneği')
        self.show()
        
    def onTimer(self):
        self.count += 1
        
        hour = (self.count / 60) / 60
        minute = (self.count / 60) % 60
        second = self.count % 60
        self.lbl.setText(str(self.count))
        print(int(hour), int(minute), second)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


