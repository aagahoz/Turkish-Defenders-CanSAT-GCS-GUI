import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Label'ın oluşturulması
        lbl = QLabel('Merhaba Dünya!', self)
        lbl.move(50, 50)  # Label'ın konumunun ayarlanması

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Basit PyQt5 Arayüzü')
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
