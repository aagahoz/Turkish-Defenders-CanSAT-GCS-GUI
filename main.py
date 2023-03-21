import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog, QInputDialog, QLineEdit, QComboBox, QProgressBar
from PyQt5.QtWidgets import QColorDialog, QInputDialog, QLineEdit, QComboBox, QProgressBar
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QMainWindow, QLayout, QAbstractItemView , QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QProxyStyle, QStyle, QProgressBar, QSizePolicy, QTableWidget, QTableWidgetItem, QAbstractScrollArea
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor, QPalette, QBrush, QPixmap, QIcon, QFont, QCursor, QStandardItemModel, QStandardItem, QIntValidator
from PyQt5 import  QtGui
from PyQt5.QtCore import Qt, QTime, QTimer, QThread, pyqtSignal

# import Qcharts
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis, QBarSet, QBarSeries, QBarCategoryAxis, QHorizontalBarSeries
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
#import QGraphicsView
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsSimpleTextItem
from PyQt5.QtCore import QRectF, QPointF, Qt, QTime, QTimer, QThread, pyqtSignal
#import QListWidget
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
import numpy as np
from pyqtgraph import PlotWidget
from PyQt5 import QtWidgets
import pyqtgraph as pg
from random import randint

import telemetryClass as tc
import helperFunctions as hf

telemetryDataS = tc.TelemetryData()
testTelemetryDatas = list()

class Example(QMainWindow):
    
        def __init__(self):
            super().__init__()

            self.setFixedHeight(900)
            self.setFixedWidth(1500)
            self.setWindowTitle('Turkish Defenders Ground Station')
            
            #change background color
            self.setAutoFillBackground(True)
            p = self.palette()
            # set mat brown color
           # p.setColor(self.backgroundRole(), QColor(179, 206, 229))
            p.setColor(self.backgroundRole(), QColor(50, 61, 65))
            self.setPalette(p)

            # add logo
            self.logo = QLabel(self)
            self.logo.setPixmap(QPixmap('./Main/Images/teamLogoView.png'))
            self.logo.setGeometry(QtCore.QRect(695, 10, 150, 150))
            self.logo.setScaledContents(True)
            self.logo.setAlignment(Qt.AlignCenter)
            # change border of logo using rgb
            self.logo.setStyleSheet("border: 2px solid rgb(179, 226, 229);")
            #change shape of logo
            self.logo.setMask(self.logo.pixmap().mask())

            

            self.initUI()
    
        def initUI(self):

            self.count = 0
            self.connectButtonActivated = False
            self.testDataCounter = 0
            self.instanceAltitude = 0

            # add connect button
            self.connectButton = QPushButton('Connect', self)
            #set style sheet
            self.connectButton.setGeometry(QtCore.QRect(100, 75, 100, 30))
            self.connectButton.clicked.connect(self.connectButtonFunction)
            # add disconnect button
            self.disconnectButton = QPushButton('Disconnect', self)
            self.disconnectButton.setGeometry(QtCore.QRect(200, 75, 100, 30))
            self.disconnectButton.clicked.connect(self.disconnectButtonFunction)

           
            # add telemetry table widget
            self.telemetryTable = QtWidgets.QTableWidget(self)
            self.telemetryTable.setGeometry(QtCore.QRect(20, 680, 1159, 200))
            self.telemetryTable.setObjectName("telemetryTable")
            self.telemetryTable.setColumnCount(17)
            self.telemetryTable.setRowCount(10)
            self.telemetryTable.setHorizontalHeaderLabels(["Team ID", "Mission Time", "Packet Count", "Altitude", "Pressure", "Temp", "Volt", "GPS TIME", "GPS Latitude", "GPS Longtitude", "GPS Altitude", "GPS SATs", "Air Speed", "Particle Count", "Pitch", "Roll", "Yaw"])
            # print(self.telemetryTable.rowCount())
            self.telemetryTable.setSortingEnabled(True)
            self.telemetryTable.setCornerButtonEnabled(False)
            self.telemetryTable.setGridStyle(QtCore.Qt.SolidLine)
            self.telemetryTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.telemetryTable.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.telemetryTable.setSelectionMode(QAbstractItemView.SingleSelection)
            self.telemetryTable.setAlternatingRowColors(True)
            self.telemetryTable.setShowGrid(True)
            self.telemetryTable.setWordWrap(False)
            self.telemetryTable.setCornerButtonEnabled(False)
            #select one row
            # self.telemetryTable.setCurrentCell(8, 0)
            
            #set table column width
            self.telemetryTable.setColumnWidth(0, 50)  # team id
            self.telemetryTable.setColumnWidth(1, 90) # mission time
            self.telemetryTable.setColumnWidth(2, 90)  # packet count
            self.telemetryTable.setColumnWidth(3, 50)  # altitude
            self.telemetryTable.setColumnWidth(4, 60)  # pressure
            self.telemetryTable.setColumnWidth(5, 50)  # temp
            self.telemetryTable.setColumnWidth(6, 50)  # volt
            self.telemetryTable.setColumnWidth(7, 70)  # gps Time
            self.telemetryTable.setColumnWidth(8, 80)  # gps latitude
            self.telemetryTable.setColumnWidth(9, 90)  # gps longtitude
            self.telemetryTable.setColumnWidth(10, 80) # gps altitude
            self.telemetryTable.setColumnWidth(11, 70) # gps sats
            self.telemetryTable.setColumnWidth(12, 70) # air speed
            self.telemetryTable.setColumnWidth(13, 85) # particle count
            self.telemetryTable.setColumnWidth(14, 45) # pitch
            self.telemetryTable.setColumnWidth(15, 45) # roll
            self.telemetryTable.setColumnWidth(16, 45) # yaw
            # set table row height
            for i in range(0, self.telemetryTable.rowCount()):
                self.telemetryTable.setRowHeight(i, 20)
    
            #!!!!!!!!!!!
            # self.telemetryTable.setRowCount(10)
            
            


            #chose a row to highlight green
            self.telemetryTable.selectRow(16)
            self.telemetryTable.setStyleSheet("QTableWidget::item:selected {background-color: YellowGreen;}")
            self.telemetryTable.setFrameStyle(QFrame.Panel | QFrame.Sunken)


            
            # axis view
            self.imageLabel = QLabel(self)
            self.imageLabel.setGeometry(1189, 180, 300, 300)
            self.imageLabel.setPixmap(QPixmap("./Main/Images/mapView.png"))
            self.imageLabel.setScaledContents(True)
            self.imageLabel.setAlignment(Qt.AlignCenter)
            self.imageLabel.setStyleSheet("background-color: white")
            self.imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
            self.imageLabel.show()
            
            # map view
            self.imageLabel = QLabel(self)
            self.imageLabel.setGeometry(1189, 524, 300, 300)
            self.imageLabel.setPixmap(QPixmap("./Main/Images/3DModelView.png"))
            self.imageLabel.setScaledContents(True)
            self.imageLabel.setAlignment(Qt.AlignCenter)
            self.imageLabel.setStyleSheet("background-color: white")
            self.imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
            self.imageLabel.show()

            # add time label
            timeString = "Mission Time: "
            self.timeText = QLabel(self)        
            self.timeText.setGeometry(460, 45, 180, 30)
            self.time = QTime.currentTime()
            self.timeText.setFont(QFont('Arial', 15))
            self.timeText.setText(timeString + "00:00:00")
            self.timeText.setAlignment(Qt.AlignCenter)
            self.timeText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
            self.timeText.setStyleSheet("background-color: white")

            # Timer'ın oluşturulması
            self.generalTimer = QTimer()
            self.generalTimer.timeout.connect(self.timerForOneSecond)
            self.generalTimer.start(1000)  # Her 1000 milisaniyede bir timeout sinyali gönderir

            # Plot 1
            self.AltiudePlot = pg.PlotWidget(self)
            self.AltiudePlot.setGeometry(50, 180, 280, 200)
            self.x = list(range(10))  # 100 time points
            self.y = [randint(0,0) for _ in range(10)]  # 100 data points
            self.AltiudePlot.setBackground('w')
            self.AltiudePlot.showGrid(x=True, y=True)
            pen = pg.mkPen(color=(255, 0, 0))
            self.data_line =  self.AltiudePlot.plot(self.x, self.y, pen=pen)
            # Plot 1 Timer
            self.timer = QtCore.QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.update_plot_data)
            self.timer.start()

            
        
            self.show()

        def connectButtonFunction(self):
            self.connectButtonActivated = True
            print("connectButtonFunction")

        def disconnectButtonFunction(self):
            self.connectButtonActivated = False
            print("disconnectButtonFunction")

        def timerForOneSecond(self):
             if self.connectButtonActivated == True:
                self.count += 1
                self.testDataCounter += 1
                newTime = hf.timeParser(self.count)

                telemetryDataS = hf.createRandomTestTelemetryObject()
                telemetryDataS.set_mission_time(newTime)
                testTelemetryDatas.append(telemetryDataS)
                # print(self.count, len(testTelemetryDatas))
                # print(testTelemetryDatas[self.count-1])
                self.updaterInterface()

        def update_plot_data(self):
            self.x = self.x[1:]  # Remove the first y element.
            self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

            self.y = self.y[1:]  # Remove the first 
            self.y.append(self.instanceAltitude)  # Add a new random value.

            self.data_line.setData(self.x, self.y)  # Update the data.

        def updaterInterface(self):
            self.timeText.setText("Mission Time: " + testTelemetryDatas[self.count - 1].mission_time)
            self.telemetryTable.setRowCount(len(testTelemetryDatas))
            for i in range(0, len(testTelemetryDatas)):
                tempList = testTelemetryDatas[i]
                for j in range(0, len(testTelemetryDatas[i].getDataAsList())):
                    #  print(i,j, tempList.getDataAsList())
                     tabloya_eklenecek_veri = tempList.getDataAsList()
                     tabloya_eklenecek_veri = tabloya_eklenecek_veri[j]
                     tabloya_eklenecek_veri = QTableWidgetItem(str(tabloya_eklenecek_veri))
                    #  print("tabloya eklenecek >> ", tabloya_eklenecek_veri)
                     self.telemetryTable.setItem(i, j, tabloya_eklenecek_veri)
            
            self.telemetryTable.setCurrentCell(len(testTelemetryDatas) - 1, 0)
            self.instanceAltitude = testTelemetryDatas[i].altitude
            print(self.instanceAltitude)



if __name__ == '__main__':
        
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec())