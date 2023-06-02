import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QColor


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Exit Button Example'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('Exit', self)
        button.setToolTip('Click to exit the program')
        button.setStyleSheet("color: white; background-color: red;")
        button.move(100, 70)
        button.clicked.connect(self.showDialog)
        self.show()

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setText("Are you sure you want to exit the program?")
        msgBox.setWindowTitle("Exit Confirmation")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
