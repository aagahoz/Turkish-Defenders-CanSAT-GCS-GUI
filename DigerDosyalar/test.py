# create gui and input from console and change color gui us pyqt6

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog, QInputDialog, QLineEdit
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor

class Example(QWidget):
    
        def __init__(self):
            super().__init__()

            self.setFixedHeight(900)
            self.setFixedWidth(1500)
    
            self.initUI()
    
        def initUI(self):            
            self.windowConfiguration()

            self.simulationButton = QtWidgets.QPushButton(QtWidgets.QDialog())
            self.connectButton = QPushButton('Connect', self)

            self.setConnectButtonConfiguration()
            self.setSimulationButtonConfiguration()
    
            self.show()

        def windowConfiguration(self):
            self.setWindowTitle('Turkish Defenders Ground Station')
            self.setStyleSheet("background-color: black;")

        def setConnectButtonConfiguration(self):
            self.connectButton.setStyleSheet("background-color: Steelblue;")
            self.connectButton.clicked.connect(self.connectButtonFunction)
            self.connectButton.setText("Connect")
            # self.simulationButton.move(20, 20)

    
        def setSimulationButtonConfiguration(self):
            # self.simulationButton.setStyleSheet("background-color: Steelblue;")
            self.connectButton.clicked.connect(self.connectButtonFunction)
            # self.connectButton.setText("Simulation")
            self.connectButton.move(220, 20)





        def mapImage(self):
            self.mapImage = QtWidgets.QLabel(self)
            self.mapImage.setGeometry(QtCore.QRect(20, 60, 1461, 821))
            self.mapImage.setStyleSheet("background-color: Steelblue;")
            self.mapImage.setText("")
            self.mapImage.setPixmap(QtGui.QPixmap("map.png"))
            self.mapImage.setScaledContents(True)
            self.mapImage.setObjectName("mapImage") 


        def simulationButtonFunction(self):
            print("clicked Simulation Mode")

        def connectButtonFunction(self):
            print("clicked Connect")

if __name__ == '__main__':
        
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec())
