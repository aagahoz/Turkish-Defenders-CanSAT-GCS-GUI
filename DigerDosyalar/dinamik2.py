import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer


class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 100)
        self.data = [0] * 10

    def setData(self, data):
        self.data = data
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        painter.setBrush(QColor(0, 0, 255, 50))
        width = self.width() / len(self.data)
        for i, value in enumerate(self.data):
            painter.drawRect(i * width, self.height() - value, width, value)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dynamic Chart Example')
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.charts = []
        for i in range(5):
            chart_widget = ChartWidget()
            self.charts.append(chart_widget)
            layout.addWidget(chart_widget)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def update_data(self):
        for chart in self.charts:
            data = chart.data
            for i in range(len(data)):
                data[i] += 1
            chart.setData(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
