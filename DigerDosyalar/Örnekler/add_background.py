from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt
import sys

class BlackWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(40, 30, 200, 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QBrush(QColor(0, 0, 0)))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Siyah Arka Plan Örneği")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.black_widget = BlackWidget(self.central_widget)
        self.black_widget.setGeometry(10,10,200,200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(500, 250, 400, 300)
    window.show()
    sys.exit(app.exec_())
