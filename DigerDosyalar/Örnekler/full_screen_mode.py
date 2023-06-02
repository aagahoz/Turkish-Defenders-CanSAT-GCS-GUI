import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        button = QPushButton("Exit Full Screen", self)
        button.clicked.connect(self.exitFullScreen)
        
        self.setCentralWidget(button)
        
    def enterFullScreen(self):
        self.showFullScreen()
        
    def exitFullScreen(self):
        self.showNormal()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.enterFullScreen()
    sys.exit(app.exec_())

