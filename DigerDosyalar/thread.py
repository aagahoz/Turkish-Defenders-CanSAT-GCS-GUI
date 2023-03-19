# Instantiate QThread directly and create two worker

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys
import time


class Worker(QThread):
    # Create a counter thread
    countChanged = pyqtSignal(int)  # int, str

    def run(self):
        count = 0
        while count < 100:
            count += 1
            if count == 50:
                # kill the thread
                self.terminate()    
                print("killeeeeeeeed")

            time.sleep(0.1)
            self.countChanged.emit(count)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QThread"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.button = QPushButton("Start", self)
        self.button.move(200, 200)
        self.button.clicked.connect(self.startThread)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def startThread(self):
        self.thread = Worker()
        self.thread.countChanged.connect(self.onCountChanged)
        self.thread.start()

        # pip install PyQt5==5.15.4

    def onCountChanged(self, value):
        print("Thread 1: ", value)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())