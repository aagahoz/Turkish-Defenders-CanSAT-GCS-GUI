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
            self.instanceTemprature = 0
            self.instancePressure = 0
            self.instanceAirSpeed = 0
            self.instanceVoltage = 0
            self.instanceParticleCount = 0
            self.instanceLatitude = 0
            self.instanceLongtitude = 0
            self.instanceGpsAltitude = 0
            self.instanceSatS = 0
            self.instancePitch = 0
            self.instanceRoll = 0
            self.instanceYaw = 0

            self.progressBarCounter = 0
            self.stateTableCounter = 0

            # add connect button
            self.connectButton = QPushButton('Connect', self)
            #set style sheet
            self.connectButton.setGeometry(QtCore.QRect(100, 75, 100, 30))
            self.connectButton.clicked.connect(self.connectButtonFunction)
            # add disconnect button
            self.disconnectButton = QPushButton('Disconnect', self)
            self.disconnectButton.setGeometry(QtCore.QRect(200, 75, 100, 30))
            self.disconnectButton.clicked.connect(self.disconnectButtonFunction)
            # add enable button
            self.enableButton = QPushButton('Enable', self)
            self.enableButton.setGeometry(QtCore.QRect(315, 45, 100, 30))
            self.enableButton.clicked.connect(self.enableButtonFunction)
            # add disable button
            self.disableButton = QPushButton('Disable', self)
            self.disableButton.setGeometry(QtCore.QRect(315, 75, 100, 30))
            self.disableButton.clicked.connect(self.disableButtonFunction)
            # add disconnect button
            self.simulationButton = QPushButton('Simulation', self)
            self.simulationButton.setGeometry(QtCore.QRect(315, 105, 100, 30))
            self.simulationButton.clicked.connect(self.simulationButtonFunction)

            # add com selector
            self.comSelector = QComboBox(self)
            self.comSelector.setGeometry(QtCore.QRect(100, 45, 100, 35))    
            self.comSelector.addItem('COM1')
            self.comSelector.addItem('COM2')
            self.comSelector.addItem('COM3')
            self.comSelector.addItem('COM4')
            self.comSelector.currentTextChanged.connect(self.currentComChanged)
            # add baud rate selector
            self.baudrateSelector = QComboBox(self)
            self.baudrateSelector.setGeometry(QtCore.QRect(200, 45, 100, 35))
            self.baudrateSelector.addItem('9600')
            self.baudrateSelector.addItem('115200')
            self.baudrateSelector.addItem('230400')
            self.baudrateSelector.addItem('460800')
            self.baudrateSelector.addItem('921600')
            self.baudrateSelector.currentTextChanged.connect(self.currentBaudrateChanged)

            #add progress bar
            self.progressBar = QtWidgets.QProgressBar(self)
            self.progressBar.setGeometry(QtCore.QRect(870, 50, 250, 30))
            self.progressBar.setProperty("value", 24)
            self.progressBar.setObjectName("progressBar")
            self.progressBar.setValue(0)
            self.progressBar.setMaximum(100)
            self.progressBar.setMinimum(0)
            # add progress bar label
            self.progressBarLabel = QLabel(self)
            self.progressBarLabel.setText("Mission Progress ")
            self.progressBarLabel.setFont(QFont('Arial', 15))
            self.progressBarLabel.setGeometry(QtCore.QRect(920, 27, 140, 20))
            self.progressBarLabel.setStyleSheet("color: rgb(179, 226, 229);")
            # add progress percent label
            self.progressPercentLabel = QLabel(self)
            self.progressPercentLabel.setFont(QFont('Arial', 15))
            self.progressPercentLabel.setText("0%")
            self.progressPercentLabel.setGeometry(QtCore.QRect(1050, 27, 100, 20))
            self.progressPercentLabel.setStyleSheet("color: rgb(179, 226, 229);")

           
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

            # add altitude label
            altitudeString = "Altitude: 0 m"
            self.altitudeText = QLabel(self)
            self.altitudeText.setGeometry(910, 88, 100, 20)
            self.altitudeText.setFont(QFont('Arial', 13))
            self.altitudeText.setText(altitudeString)
            self.altitudeText.setAlignment(Qt.AlignCenter)
            # self.altitudeText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
            self.altitudeText.setStyleSheet("background-color: white")
            self.altitudeText.show()

            # create table
            self.stateTable = QTableWidget(self)
            self.stateTable.setGeometry(1150, 20, 147, 90)
            self.stateTable.setColumnCount(2)
            self.stateTable.setRowCount(4)
            # not show index
            self.stateTable.verticalHeader().setVisible(False)
            self.stateTable.horizontalHeader().setVisible(False)
            self.stateTable.setItem(0, 1, QTableWidgetItem("Started"))
            self.stateTable.setItem(1, 1, QTableWidgetItem("Not Started"))
            self.stateTable.setItem(2, 1, QTableWidgetItem("Not Started"))
            self.stateTable.setItem(3, 1, QTableWidgetItem("Not Started"))
            self.stateTable.setItem(0, 0, QTableWidgetItem("Launch"))
            self.stateTable.setItem(1, 0, QTableWidgetItem("Ascent"))
            self.stateTable.setItem(2, 0, QTableWidgetItem("Descent"))
            self.stateTable.setItem(3, 0, QTableWidgetItem("Landing"))
            self.stateTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.stateTable.setShowGrid(False)
            #chose a row to highlight green
            self.stateTable.selectRow(0)
            self.stateTable.setStyleSheet("QTableWidget::item:selected {background-color: YellowGreen;}")
            self.stateTable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
            self.stateTable.resizeColumnsToContents()
            self.stateTable.resizeRowsToContents()
            self.stateTable.show()

            # add table widget button
            self.telemetryTableButton = QPushButton(self)
            self.telemetryTableButton.setText("Clear Table")
            self.telemetryTableButton.setGeometry(QtCore.QRect(1180, 855, 100, 30))
            self.telemetryTableButton.clicked.connect(self.cleanTelemetryTableButtonFunction)

            # add latitude longitude altitude sats label
            latitudeLongitudeAltitudeSatsString = "Lat: 00.000000  Long: 00.000000  Alt: 000.0m  Sats: 0"
            self.latitudeLongitudeAltitudeSatsText = QLabel(self)
            self.latitudeLongitudeAltitudeSatsText.setGeometry(1189, 485, 300, 20)
            self.latitudeLongitudeAltitudeSatsText.setFont(QFont('Arial', 11))
            self.latitudeLongitudeAltitudeSatsText.setText(latitudeLongitudeAltitudeSatsString)
            self.latitudeLongitudeAltitudeSatsText.setAlignment(Qt.AlignCenter)
            self.latitudeLongitudeAltitudeSatsText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
            self.latitudeLongitudeAltitudeSatsText.setStyleSheet("background-color: white")
            self.latitudeLongitudeAltitudeSatsText.show()

            # add pitch roll yaw label
            pitchRollYawString = "Pitch: 3°              Roll: 6°              Yaw: 20°"
            self.pitchRollYawText = QLabel(self)
            self.pitchRollYawText.setGeometry(1189, 830, 300, 20)
            self.pitchRollYawText.setFont(QFont('Arial', 12))
            self.pitchRollYawText.setText(pitchRollYawString)
            self.pitchRollYawText.setAlignment(Qt.AlignCenter)
            self.pitchRollYawText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
            self.pitchRollYawText.setStyleSheet("background-color: white")
            self.pitchRollYawText.show()

            # Plot Altitude
            self.AltiudePlot = pg.PlotWidget(self)
            self.AltiudePlot.setGeometry(50, 180, 280, 200)
            self.xAltitude = list(range(10))  # 100 time points
            self.yAltitude = [randint(0,0) for _ in range(10)]  # 100 data points
            self.AltiudePlot.setBackground('w')
            self.AltiudePlot.showGrid(x=True, y=True)
            self.AltiudePlot.setLabel('left', 'Altitude', units='m')
            self.AltiudePlot.setLabel('bottom', 'Time', units='s')
            pen = pg.mkPen(color=(255, 0, 0))
            self.data_line_altitude =  self.AltiudePlot.plot(self.xAltitude, self.yAltitude, pen=pen)

            # Plot Temprature
            self.TempraturePlot = pg.PlotWidget(self)
            self.TempraturePlot.setGeometry(400, 180, 280, 200)
            self.xTemprature = list(range(10))  # 100 time points
            self.yTemprature = [randint(0,0) for _ in range(10)]  # 100 data points
            self.TempraturePlot.setBackground('w')
            self.TempraturePlot.showGrid(x=True, y=True)
            self.TempraturePlot.setLabel('left', 'Temprature', units='C')
            self.TempraturePlot.setLabel('bottom', 'Time', units='s')
            pen = pg.mkPen(color=(255, 0, 0))
            self.data_line_temprature =  self.TempraturePlot.plot(self.xTemprature, self.yTemprature, pen=pen)

            # Plot Pressure
            self.PressurePlot = pg.PlotWidget(self)
            self.PressurePlot.setGeometry(750, 180, 280, 200)
            self.xPressure = list(range(10))  # 100 time points
            self.yPressure = [randint(0,0) for _ in range(10)]  # 100 data points
            self.PressurePlot.setBackground('w')
            self.PressurePlot.showGrid(x=True, y=True)
            self.PressurePlot.setLabel('left', 'Pressure', units='Pa')
            self.PressurePlot.setLabel('bottom', 'Time', units='s')
            pen = pg.mkPen(color=(255, 0, 0))
            self.data_line_pressure =  self.PressurePlot.plot(self.xPressure, self.yPressure, pen=pen)

            # Plot AirSpeed
            self.AirSpeedPlot = pg.PlotWidget(self)
            self.AirSpeedPlot.setGeometry(50, 430, 280, 200)
            self.xAirSpeed = list(range(10))  # 100 time points
            self.yAirSpeed = [randint(0,0) for _ in range(10)]  # 100 data points
            self.AirSpeedPlot.setBackground('w')
            self.AirSpeedPlot.showGrid(x=True, y=True)
            self.AirSpeedPlot.setLabel('left', 'Air Speed', units='m/s')
            self.AirSpeedPlot.setLabel('bottom', 'Time', units='s')
            pen = pg.mkPen(color=(255, 0, 0))
            self.data_line_airspeed =  self.AirSpeedPlot.plot(self.xAirSpeed, self.yAirSpeed, pen=pen)

            # Plot Voltage
            self.VoltagePlot = pg.PlotWidget(self)
            self.VoltagePlot.setGeometry(400, 430, 280, 200)
            self.xVoltage = list(range(10))  # 100 time points
            self.yVoltage = [randint(0,0) for _ in range(10)]  # 100 data points
            self.VoltagePlot.setBackground('w')
            self.VoltagePlot.showGrid(x=True, y=True)
            self.VoltagePlot.setLabel('left', 'Voltage', units='V')
            self.VoltagePlot.setLabel('bottom', 'Time', units='s')
            pen = pg.mkPen(color=(255, 0, 0))
            self.data_line_voltage =  self.VoltagePlot.plot(self.xVoltage, self.yVoltage, pen=pen)

            # Plot ParticleCount
            self.ParticleCountPlot = pg.PlotWidget(self)
            self.ParticleCountPlot.setGeometry(750, 430, 280, 200)
            self.xParticleCount = list(range(10))  # 100 time points
            self.yParticleCount = [randint(0,0) for _ in range(10)]  # 100 data points
            self.ParticleCountPlot.setBackground('w')
            self.ParticleCountPlot.showGrid(x=True, y=True)
            self.ParticleCountPlot.setLabel('left', 'Particle Count', units='m')
            self.ParticleCountPlot.setLabel('bottom', 'Time', units='s')
            pen = pg.mkPen(color=(255, 0, 0))
            self.data_line_particlecount =  self.ParticleCountPlot.plot(self.xParticleCount, self.yParticleCount, pen=pen)
            
            # Plot Timer
            self.timerPlot = QtCore.QTimer()
            self.timerPlot.setInterval(1000)
            self.timerPlot.timeout.connect(self.update_plots_data)
            self.timerPlot.start()
            self.show()

        def connectButtonFunction(self):
            self.connectButtonActivated = True
            print("connectButtonFunction")

        def disconnectButtonFunction(self):
            self.connectButtonActivated = False
            print("disconnectButtonFunction")

        def enableButtonFunction(self):
            print("enableButtonFunction")     

        def disableButtonFunction(self):
            print("disableButtonFunction")

        def currentBaudrateChanged(self):
            print(self.baudrateSelector.currentText())
            print(self.baudrateSelector.currentIndex())
        
        def currentComChanged(self):
            print(self.comSelector.currentText())
            print(self.comSelector.currentIndex())

        def simulationButtonFunction(self):
            print("simulationButtonFunction")
        
        def cleanTelemetryTableButtonFunction(self):
            print("cleanTelemetryTableButtonFunction")
            self.telemetryTable.clearContents()

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

        def update_plots_data(self):
            self.xAltitude = self.xAltitude[1:]  # Remove the first y element.
            self.xAltitude.append(self.xAltitude[-1] + 1)  # Add a new value 1 higher than the last.

            self.yAltitude = self.yAltitude[1:]  # Remove the first 
            self.yAltitude.append(self.instanceAltitude)  # Add a new random value.
            self.instanceAltitude = 0

            self.data_line_altitude.setData(self.xAltitude, self.yAltitude)  # Update the data.

            self.xTemprature = self.xTemprature[1:]  # Remove the first y element.
            self.xTemprature.append(self.xTemprature[-1] + 1)  # Add a new value 1 higher than the last.

            self.yTemprature = self.yTemprature[1:]  # Remove the first 
            self.yTemprature.append(self.instanceTemprature)  # Add a new random value.
            self.instanceTemprature = 0

            self.data_line_temprature.setData(self.xTemprature, self.yTemprature)  # Update the data.

            self.xPressure = self.xPressure[1:]  # Remove the first y element.
            self.xPressure.append(self.xPressure[-1] + 1)  # Add a new value 1 higher than the last.

            self.yPressure = self.yPressure[1:]  # Remove the first 
            self.yPressure.append(self.instancePressure)  # Add a new random value.
            self.instancePressure = 0

            self.data_line_pressure.setData(self.xPressure, self.yPressure)  # Update the data.

            self.xAirSpeed = self.xAirSpeed[1:]  # Remove the first y element.
            self.xAirSpeed.append(self.xAirSpeed[-1] + 1)  # Add a new value 1 higher than the last.

            self.yAirSpeed = self.yAirSpeed[1:]  # Remove the first 
            self.yAirSpeed.append(self.instanceAirSpeed)  # Add a new random value.
            self.instanceAirSpeed = 0

            self.data_line_airspeed.setData(self.xAirSpeed, self.yAirSpeed)  # Update the data.

            self.xVoltage = self.xVoltage[1:]  # Remove the first y element.
            self.xVoltage.append(self.xVoltage[-1] + 1)  # Add a new value 1 higher than the last.

            self.yVoltage = self.yVoltage[1:]  # Remove the first 
            self.yVoltage.append(self.instanceVoltage)  # Add a new random value.
            self.instanceVoltage = 0

            self.data_line_voltage.setData(self.xVoltage, self.yVoltage)  # Update the data.

            self.xParticleCount = self.xParticleCount[1:]  # Remove the first y element.
            self.xParticleCount.append(self.xParticleCount[-1] + 1)  # Add a new value 1 higher than the last.

            self.yParticleCount = self.yParticleCount[1:]  # Remove the first 
            self.yParticleCount.append(self.instanceParticleCount)  # Add a new random value.
            self.instanceParticleCount = 0

            self.data_line_particlecount.setData(self.xParticleCount, self.yParticleCount)  # Update the data.

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
            self.instanceTemprature = testTelemetryDatas[i].temp
            self.instancePressure = testTelemetryDatas[i].pressure
            self.instanceAirSpeed = testTelemetryDatas[i].air_speed
            self.instanceVoltage = testTelemetryDatas[i].volt
            self.instanceParticleCount = testTelemetryDatas[i].particle_count
            self.instanceLatitude = testTelemetryDatas[i].gps_latitude
            self.instanceLongtitude = testTelemetryDatas[i].gps_longitude
            self.instanceGpsAltitude = testTelemetryDatas[i].gps_altitude
            self.instanceSatS = testTelemetryDatas[i].gps_sats
            self.instancePitch = testTelemetryDatas[i].pitch
            self.instanceRoll = testTelemetryDatas[i].roll
            self.instanceYaw = testTelemetryDatas[i].yaw

            print(self.instanceAltitude, self.instanceTemprature, self.instancePressure, self.instanceAirSpeed, self.instanceVoltage, self.instanceParticleCount)
            
            self.altitudeText.setText("Altitude: {} m".format(self.instanceAltitude))
            self.latitudeLongitudeAltitudeSatsText.setText("Lat: {}  Long: {}  Alt: {}m  Sats: {}".format(self.instanceLatitude, self.instanceLongtitude, self.instanceAltitude, self.instanceSatS))
            self.pitchRollYawText.setText("Pitch: {}°              Roll: {}°              Yaw: {}°".format(self.instancePitch, self.instanceRoll, self.instanceYaw))

            

            if self.progressBarCounter >= 100:
                self.progressBarCounter = 0
            self.progressBar.setValue(self.progressBarCounter)
            self.progressPercentLabel.setText("{}%".format(self.progressBarCounter))
            self.progressBarCounter += 1

            
            if self.stateTableCounter > 3:
                self.stateTableCounter = 0
            self.stateTable.selectRow(self.stateTableCounter)
            self.stateTableCounter += 1


        

if __name__ == '__main__':
        
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec())