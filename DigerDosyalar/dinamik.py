import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, QRect
from PyQt5 import  QtGui

class MovingBox(QWidget):
    def __init__(self):
        super().__init__()
        
        # Pencere boyutları
        self.width = 300
        self.height = 300
        
        # Kutu özellikleri
        self.box_size = 50
        self.box_pos = QRect(0, 0, self.box_size, self.box_size)
        self.box_speed = 5
        
        # Pencere özellikleri
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('Sürekli Hareket Eden Kutu')
        self.show()
        
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_box)
        self.timer.start(1000)
        
    def move_box(self):
        # Kutu hareketi
        x = self.box_pos.x() + self.box_speed
        y = self.box_pos.y() + self.box_speed
        
        # Pencere kenarlarına çarpma kontrolü
        if x + self.box_size > self.width or x < 0:
            self.box_speed *= -1
        if y + self.box_size > self.height or y < 0:
            self.box_speed *= -1
            
        # Kutu konumunu güncelleme
        self.box_pos.moveTo(x, y)
        self.update()
        
    def paintEvent(self, event):
        # Kutuyu çizme
        painter = QtGui.QPainter(self)
        painter.fillRect(self.box_pos, QtGui.QColor(255, 0, 0))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MovingBox()
    sys.exit(app.exec_())
