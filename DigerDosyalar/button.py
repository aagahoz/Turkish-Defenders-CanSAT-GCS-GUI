# create gui and input from console and change color gui us pyqt6

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog, QInputDialog, QLineEdit, QComboBox, QVBoxLayout, QLabel, QMainWindow, QLayout, QProxyStyle, QStyle, QProgressBar
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5 import QtGui

class Example(QMainWindow):
    
        def __init__(self):
            super().__init__()

            self.setFixedHeight(900)
            self.setFixedWidth(1500)
    
            self.initUI()
    
        def initUI(self):            
            # add simulation button
            self.simulationButton = QPushButton('Simulation', self)
            self.simulationButton.setGeometry(QtCore.QRect(20, 20, 100, 30))
            self.simulationButton.clicked.connect(self.simulationButtonFunction)
            # add connect button
            self.connectButton = QPushButton('Connect', self)
            self.connectButton.setGeometry(QtCore.QRect(120, 20, 100, 30))
            self.connectButton.clicked.connect(self.connectButtonFunction)

            # add com selector
            self.comSelector = QComboBox(self)
            self.comSelector.setGeometry(QtCore.QRect(220, 20, 100, 35))    
            self.comSelector.addItem('COM1')
            self.comSelector.addItem('COM2')
            self.comSelector.addItem('COM3')
            self.comSelector.addItem('COM4')
            self.comSelector.currentTextChanged.connect(self.currentComChanged)
            # add com label
            self.comLabel = QLabel(self)
            self.comLabel.setText("COM")
            self.comLabel.setGeometry(QtCore.QRect(260, 3, 100, 20))
            # add baud rate selector
            self.baudrateSelector = QComboBox(self)
            self.baudrateSelector.setGeometry(QtCore.QRect(320, 20, 100, 35))
            self.baudrateSelector.addItem('9600')
            self.baudrateSelector.addItem('115200')
            self.baudrateSelector.addItem('230400')
            self.baudrateSelector.addItem('460800')
            self.baudrateSelector.addItem('921600')
            self.baudrateSelector.currentTextChanged.connect(self.currentBaudrateChanged)
            # add baud rate label
            self.baudrateLabel = QLabel(self)
            self.baudrateLabel.setText("Baudrate")
            self.baudrateLabel.setGeometry(QtCore.QRect(340, 3, 100, 20))

            #add progress bar
            self.progressBar = QtWidgets.QProgressBar(self)
            self.progressBar.setGeometry(QtCore.QRect(420, 20, 200, 30))
            self.progressBar.setProperty("value", 24)
            self.progressBar.setObjectName("progressBar")
            self.progressBar.setValue(50)
            self.progressBar.setMaximum(100)
            self.progressBar.setMinimum(0)
            #change color progress bar

            palette = self.progressBar.palette()
            palette.setColor(QtGui.QPalette.Highlight, QtCore.Qt.green)
            self.progressBar.setPalette(palette)





            # add progress bar label
            self.progressBarLabel = QLabel(self)
            self.progressBarLabel.setText("Progress")
            self.progressBarLabel.setGeometry(QtCore.QRect(490, 3, 100, 20))

            
            




            





        
            self.show()
        

        def currentBaudrateChanged(self):
            print(self.baudrateSelector.currentText())
            print(self.baudrateSelector.currentIndex())
        
        def currentComChanged(self):
            print(self.comSelector.currentText())
            print(self.comSelector.currentIndex())

        def connectButtonFunction(self):
            print("connectButtonFunction")

        def simulationButtonFunction(self):
            print("simulationButtonFunction")


  


if __name__ == '__main__':
        
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec())
