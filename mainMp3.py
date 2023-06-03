from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QComboBox, QProgressBar, QMessageBox, QLabel, QMainWindow, QAbstractItemView, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor, QBrush, QPixmap, QFont, QPainter, QIcon
from PyQt5.QtCore import Qt, QTime, QTimer, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtGui

import sys
import subprocess
from random import randint
import pyqtgraph as pg

import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


import telemetryClass as tc
import helperFunctions as hf

import serial
import time

telemetryDataS = tc.TelemetryData()
altitudeSilinecek = tc.TelemetryData()
testTelemetryDatas = list()

SELECTED_COM_PORT = '/dev/tty.usbserial-A50285BI'
SELECTED_COM_BAUD_RATE = 9600

TELEMETRY_TYPES_COLUMNS_NAMES = ["Team ID", "Mission Time", "Packet Count", "Mode", "State", "Altitude", "HS Deployed", "PC Deployed",
                                 "Mast Raised", "Temp", "Pressure", "Volt", "GPS Time", "GPS Altitude", "GPS Latitude", "GPS Longitude", "GPS SatS", "Tilt X", "Tilt Y", "CMD Echo"]
PROGRAM_NAME = 'Turkish Defenders Ground Station'
LOGO_PATH = './Main/Images/teamLogoView.png'
BAUD_RATES_LIST = ["9600", "115200", "230400", "460800", "921600"]
REFRESH_LOGO_PATH = "/Users/agahozdemir/Documents/Programming/Turkish-Defenders-CanSAT-GCS-GUI/DigerDosyalar/Örnekler/refresh.png"
START_3D_MODEL_VIEW = "DigerDosyalar/3DMODELYENI.png"


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(995)
        self.setFixedWidth(1620)
        self.setWindowTitle(PROGRAM_NAME)

        # change background color
        self.setAutoFillBackground(True)
        p = self.palette()
        # set mat brown color
       # p.setColor(self.backgroundRole(), QColor(179, 206, 229))
        p.setColor(self.backgroundRole(), QColor(50, 61, 65))
        self.setPalette(p)

        # add logo
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(LOGO_PATH))
        self.logo.setGeometry(QtCore.QRect(687, 10, 150, 150))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)
        # change border of logo using rgb
        self.logo.setStyleSheet("border: 2px solid rgb(179, 226, 229);")
        # change shape of logo
        self.logo.setMask(self.logo.pixmap().mask())

        self.player = QMediaPlayer()
        # self.ser = serial.Serial(SELECTED_COM_PORT, SELECTED_COM_BAUD_RATE, timeout=1)
        # self.ser.flush()

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
        self.COUNTER_FROM_START = 0

        self.packetCount = 1

        self.comList = dict()

        self.isFullScreen = False

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.black_widget = BlackWidget(self.central_widget)
        self.black_widget.setGeometry(40, 180, 1120, 540)

        # add connect button
        self.connectButton = QPushButton('Connect', self)
        self.connectButton.setGeometry(QtCore.QRect(60, 72, 100, 32))
        self.connectButton.clicked.connect(self.connectButtonFunction)
        self.connectButton.setFont(QFont("Calibri", 15))

        # add disconnect button
        self.disconnectButton = QPushButton('Disconnect', self)
        self.disconnectButton.setGeometry(QtCore.QRect(176, 72, 120, 32))
        self.disconnectButton.clicked.connect(self.disconnectButtonFunction)
        self.disconnectButton.setFont(QFont("Calibri", 15))

        # add enable button
        self.simEnableButton = QPushButton('Sim Enable', self)
        self.simEnableButton.setGeometry(QtCore.QRect(325, 55, 120, 32))
        self.simEnableButton.clicked.connect(self.simEnableButtonFunction)
        self.simEnableButton.setFont(QFont("Calibri", 15))

        # add disable button
        self.simDisableButton = QPushButton('Sim Disable', self)
        self.simDisableButton.setGeometry(QtCore.QRect(460, 55, 120, 32))
        self.simDisableButton.clicked.connect(self.disableButtonFunction)
        self.simDisableButton.setFont(QFont("Calibri", 15))

         # add import csv button
        self.importCsvButton = QPushButton('Import CSV', self)
        self.importCsvButton.setGeometry(460, 112, 140, 32)
        self.importCsvButton.setFont(QFont("Calibri", 15))
       

        # add CX On button
        self.telemetryOnButton = QPushButton('Telem On', self)
        self.telemetryOnButton.setGeometry(QtCore.QRect(445, 80, 100, 32))
        self.telemetryOnButton.clicked.connect(self.disableButtonFunction)
        self.telemetryOnButton.setFont(QFont("Calibri", 15))

        # add CX Off button
        self.telemetryOffButton = QPushButton('Telem Off', self)
        self.telemetryOffButton.setGeometry(QtCore.QRect(445, 120, 100, 32))
        self.telemetryOffButton.clicked.connect(self.disableButtonFunction)
        self.telemetryOffButton.setFont(QFont("Calibri", 15))

        # add disconnect button
        self.simulationButton = QPushButton('Simulation', self)
        self.simulationButton.setGeometry(QtCore.QRect(315, 91, 120, 32))
        self.simulationButton.clicked.connect(self.simulationButtonFunction)
        self.simulationButton.setFont(QFont("Calibri", 15))

    

        # add table widget button
        self.telemetryTableButton = QPushButton(self)
        self.telemetryTableButton.setText("Clear Table")
        self.telemetryTableButton.setGeometry(QtCore.QRect(1200, 945, 110, 32))
        # self.telemetryTableButton.clicked.connect(self.cleanTelemetryTableButtonFunction)
        self.telemetryTableButton.setFont(QFont("Calibri", 15))

        # add save csv button
        self.save_button = QPushButton("Save To CSV", self)
        self.save_button.clicked.connect(self.save_to_csv)
        self.save_button.setGeometry(QtCore.QRect(1310, 945, 130, 32))
        # self.telemetryTableButton.clicked.connect(self.save_to_csv)
        self.save_button.setFont(QFont("Calibri", 15))

        # add com selector
        self.comSelector = QComboBox(self)
        self.comSelector.setGeometry(QtCore.QRect(30, 35, 170, 40))
        # self.comSelector.addItem('COM1')
        # self.comSelector.addItem('COM2')
        # self.comSelector.addItem('COM3')
        # self.comSelector.addItem('COM4')
        self.comList = hf.getUsbSerialDevices(hf.getComList())
        for key, value in self.comList.items():
            self.comSelector.addItem(value)
        self.comSelector.currentTextChanged.connect(self.currentComChanged)
        self.comSelector.setFont(QFont("Calibri", 16))

        # add baud rate selector
        self.baudrateSelector = QComboBox(self)
        self.baudrateSelector.setGeometry(QtCore.QRect(200, 35, 100, 40))
        for i in range(len(BAUD_RATES_LIST)):
            self.baudrateSelector.addItem(str(BAUD_RATES_LIST[i]))

        self.baudrateSelector.currentTextChanged.connect(
            self.currentBaudrateChanged)
        self.baudrateSelector.setFont(QFont("Calibri", 16))

        # QIcon nesnesi yükleyin
        refresh_icon = QIcon(REFRESH_LOGO_PATH)
        # QPushButton nesnesi oluşturun
        refresh_button = QPushButton(refresh_icon, "Refresh", self)
        refresh_button.setGeometry(70, 8, 90, 25)
        refresh_button.clicked.connect(self.refresh)

        # add progress bar
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(870, 50, 250, 40))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(0)
        # add progress bar label
        self.progressBarLabel = QLabel(self)
        self.progressBarLabel.setText("Mission Progress ")
        self.progressBarLabel.setFont(QFont('Arial', 18))
        self.progressBarLabel.setGeometry(QtCore.QRect(920, 27, 140, 20))
        self.progressBarLabel.setStyleSheet("color: rgb(179, 226, 229);")
        # add progress percent label
        self.progressPercentLabel = QLabel(self)
        self.progressPercentLabel.setFont(QFont('Arial', 18))
        self.progressPercentLabel.setText("0%")
        self.progressPercentLabel.setGeometry(QtCore.QRect(1067, 27, 100, 20))
        self.progressPercentLabel.setStyleSheet("color: rgb(179, 226, 229);")

        # add telemetry table widget
        self.telemetryTable = QtWidgets.QTableWidget(self)
        self.telemetryTable.setGeometry(QtCore.QRect(25, 740, 1159, 230))
        self.telemetryTable.setObjectName("telemetryTable")

        self.telemetryTable.setColumnCount(20)
        self.telemetryTable.setRowCount(10)
        self.telemetryTable.setHorizontalHeaderLabels(
            TELEMETRY_TYPES_COLUMNS_NAMES)
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
        # select one row
        # self.telemetryTable.setCurrentCell(8, 0)

        # set table column width
        self.telemetryTable.setColumnWidth(0, 50)  # team id
        self.telemetryTable.setColumnWidth(1, 90)  # mission time
        self.telemetryTable.setColumnWidth(2, 90)  # packet count
        self.telemetryTable.setColumnWidth(3, 50)  # altitude
        self.telemetryTable.setColumnWidth(4, 60)  # pressure
        self.telemetryTable.setColumnWidth(5, 50)  # temp
        self.telemetryTable.setColumnWidth(6, 50)  # volt
        self.telemetryTable.setColumnWidth(7, 70)  # gps Time
        self.telemetryTable.setColumnWidth(8, 80)  # gps latitude
        self.telemetryTable.setColumnWidth(9, 90)  # gps longtitude
        self.telemetryTable.setColumnWidth(10, 80)  # gps altitude
        self.telemetryTable.setColumnWidth(11, 70)  # gps sats
        self.telemetryTable.setColumnWidth(12, 70)  # air speed
        self.telemetryTable.setColumnWidth(13, 85)  # particle count
        self.telemetryTable.setColumnWidth(14, 45)  # pitch
        self.telemetryTable.setColumnWidth(15, 45)  # roll
        self.telemetryTable.setColumnWidth(16, 45)  # yaw
        self.telemetryTable.setColumnWidth(17, 45)  #
        self.telemetryTable.setColumnWidth(18, 45)  #
        self.telemetryTable.setColumnWidth(19, 45)  #
        # set table row height
        for i in range(0, self.telemetryTable.rowCount()):
            self.telemetryTable.setRowHeight(i, 20)

        # chose a row to highlight green
        self.telemetryTable.selectRow(16)
        self.telemetryTable.setStyleSheet(
            "QTableWidget::item:selected {background-color: YellowGreen;}")
        self.telemetryTable.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        # map view
        self.mapView = QWebEngineView(self)
        self.mapView.setGeometry(1230, 180, 350, 350)
        self.mapView.load(QUrl("https://www.openstreetmap.org/#map=19/{}/{}".format(
            40.797215, 29.425327)))
        self.mapView.show()

        # 3D view
        self.imageLabel = QLabel(self)
        self.imageLabel.setGeometry(1230, 560, 350, 350)
        self.imageLabel.setPixmap(QPixmap(START_3D_MODEL_VIEW))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setStyleSheet("background-color: white")
        self.imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.imageLabel.show()

        # add time label
        timeString = "Mission Time: "
        self.timeText = QLabel(self)
        self.timeText.setGeometry(460, 15, 180, 30)
        self.timeText.setFont(QFont('Arial', 15))
        self.timeText.setText(timeString + "00:00:00")
        self.timeText.setAlignment(Qt.AlignCenter)
        self.timeText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.timeText.setStyleSheet("background-color: white")

        # Timer'ın oluşturulması
        self.generalTimer = QTimer()
        self.generalTimer.timeout.connect(self.timerForOneSecond)
        # Her 1000 milisaniyede bir timeout sinyali gönderir
        self.generalTimer.start(1000)

        # add altitude label
        altitudeString = "Altitude: 0 m"
        self.altitudeText = QLabel(self)
        self.altitudeText.setGeometry(935, 98, 130, 30)
        self.altitudeText.setFont(QFont('Arial', 15))
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
        # chose a row to highlight green
        self.stateTable.selectRow(0)
        self.stateTable.setStyleSheet(
            "QTableWidget::item:selected {background-color: YellowGreen;}")
        self.stateTable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.stateTable.resizeColumnsToContents()
        self.stateTable.resizeRowsToContents()
        self.stateTable.show()

        # Exit button
        self.exitButton = QPushButton('Exit', self)
        self.exitButton.setToolTip('Click to exit the program')
        self.exitButton.setStyleSheet("color: white; background-color: red;")
        self.exitButton.setGeometry(1530, 10, 60, 25)
        self.exitButton.clicked.connect(self.showExitDialog)
        self.exitButton.setFont(QFont('Comic Sans MS', 15))

        # full screen button
        self.fullScreenButton = QPushButton("Open Full Screen", self)
        self.fullScreenButton.setToolTip('Click to full screen the program')
        self.fullScreenButton.clicked.connect(self.enterFullScreen)
        self.fullScreenButton.setStyleSheet(
            "color: white; background-color: green;")
        self.fullScreenButton.setGeometry(1368, 10, 160, 25)
        self.fullScreenButton.setFont(QFont('Comic Sans MS', 15))

        # QProgressBar Battery Percent
        self.batteryProgressBar = QProgressBar(self)
        self.batteryProgressBar.setGeometry(1390, 80, 160, 15)
        self.batteryProgressBar.setValue(0)
        self.batteryProgressBar.setTextVisible(True)
        # add batteryVoltage label
        batteryString = "Battery Percent: "
        self.batteryText = QLabel(self)
        self.batteryText.setGeometry(1394, 103, 150, 25)
        self.batteryText.setFont(QFont('Arial', 14))
        self.batteryText.setText(batteryString + "%" + "0")
        self.batteryText.setAlignment(Qt.AlignCenter)
        self.batteryText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.batteryText.setStyleSheet("background-color: white")
        # QTimer
        timerBattery = QTimer(self)
        timerBattery.timeout.connect(self.update_battery_percentage)
        timerBattery.start(1000)

        # add instance time label
        self.timeLabel = QLabel(self)
        self.timeLabel.setFont(QFont('Arial', 15))
        self.timeLabel.setGeometry(QtCore.QRect(1440, 50, 140, 20))
        self.timeLabel.setStyleSheet("color: rgb(179, 226, 229);")

        # add latitude longitude altitude sats label
        latitudeLongitudeAltitudeSatsString = "Lat: 00.000000  Long: 00.000000  Alt: 000.0 m  Sats: 0"
        self.latitudeLongitudeAltitudeSatsText = QLabel(self)
        self.latitudeLongitudeAltitudeSatsText.setGeometry(1230, 490, 350, 40)
        self.latitudeLongitudeAltitudeSatsText.setFont(QFont('Arial', 13))
        self.latitudeLongitudeAltitudeSatsText.setText(
            latitudeLongitudeAltitudeSatsString)
        self.latitudeLongitudeAltitudeSatsText.setAlignment(Qt.AlignCenter)
        self.latitudeLongitudeAltitudeSatsText.setFrameStyle(
            QFrame.Panel | QFrame.Sunken)
        self.latitudeLongitudeAltitudeSatsText.setStyleSheet(
            "background-color: white")
        self.latitudeLongitudeAltitudeSatsText.show()

        # add pitch roll yaw label
        pitchRollYawString = "      Pitch: 0°              Roll: 0°"
        self.pitchRollYawText = QLabel(self)
        self.pitchRollYawText.setGeometry(1230, 890, 350, 40)
        self.pitchRollYawText.setFont(QFont('Arial', 13))
        self.pitchRollYawText.setText(pitchRollYawString)
        self.pitchRollYawText.setAlignment(Qt.AlignCenter)
        self.pitchRollYawText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.pitchRollYawText.setStyleSheet("background-color: white")
        self.pitchRollYawText.show()

        # Plot Altitude
        self.AltitudePlot = pg.PlotWidget(self)
        self.AltitudePlot.setGeometry(50, 190, 340, 240)
        self.xAltitude = list(range(10))  # 100 time points
        self.yAltitude = [randint(0, 0) for _ in range(10)]  # 100 data points
        self.AltitudePlot.setBackground(QColor(70, 70, 70))
        self.AltitudePlot.showGrid(x=True, y=True)
        self.AltitudePlot.setLabel('left', 'Altitude', units='m', color='k')
        self.AltitudePlot.setLabel('bottom', 'Time', units='s', color='k')
        pen = pg.mkPen(color=(255, 0, 0), width=3)  # Beyaz çizgi
        self.data_line_altitude = self.AltitudePlot.plot(
            self.xAltitude, self.yAltitude, pen=pen)

        # Plot Temprature
        self.TempraturePlot = pg.PlotWidget(self)
        self.TempraturePlot.setGeometry(430, 190, 340, 240)
        self.xTemprature = list(range(10))  # 100 time points
        self.yTemprature = [randint(0, 0)
                            for _ in range(10)]  # 100 data points
        self.TempraturePlot.setBackground(QColor(70, 70, 70))
        self.TempraturePlot.showGrid(x=True, y=True)
        self.TempraturePlot.setLabel(
            'left', 'Temprature', units='C', color='k')
        self.TempraturePlot.setLabel('bottom', 'Time', units='s', color='k')
        pen = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_temprature = self.TempraturePlot.plot(
            self.xTemprature, self.yTemprature, pen=pen)

        # Plot Pressure
        self.PressurePlot = pg.PlotWidget(self)
        self.PressurePlot.setGeometry(810, 190, 340, 240)
        self.xPressure = list(range(10))  # 100 time points
        self.yPressure = [randint(0, 0) for _ in range(10)]  # 100 data points
        self.PressurePlot.setBackground(QColor(70, 70, 70))
        self.PressurePlot.showGrid(x=True, y=True)
        self.PressurePlot.setLabel('left', 'Pressure', units='Pa', color='k')
        self.PressurePlot.setLabel('bottom', 'Time', units='s', color='k')
        pen = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_pressure = self.PressurePlot.plot(
            self.xPressure, self.yPressure, pen=pen)

        # Plot AirSpeed
        self.AirSpeedPlot = pg.PlotWidget(self)
        self.AirSpeedPlot.setGeometry(50, 470, 340, 240)
        self.xAirSpeed = list(range(10))  # 100 time points
        self.yAirSpeed = [randint(0, 0) for _ in range(10)]  # 100 data points
        self.AirSpeedPlot.setBackground(QColor(70, 70, 70))
        self.AirSpeedPlot.showGrid(x=True, y=True)
        self.AirSpeedPlot.setLabel('left', 'Accel X', units='m/s²', color='k')
        self.AirSpeedPlot.setLabel('bottom', 'Time', units='s', color='k')
        pen = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_airspeed = self.AirSpeedPlot.plot(
            self.xAirSpeed, self.yAirSpeed, pen=pen)

        # Plot Voltage
        self.VoltagePlot = pg.PlotWidget(self)
        self.VoltagePlot.setGeometry(430, 470, 340, 240)
        self.xVoltage = list(range(10))  # 100 time points
        self.yVoltage = [randint(0, 0) for _ in range(10)]  # 100 data points
        self.VoltagePlot.setBackground(QColor(70, 70, 70))
        self.VoltagePlot.showGrid(x=True, y=True)
        self.VoltagePlot.setLabel('left', 'Accel Y', units='m/s²', color='k')
        self.VoltagePlot.setLabel('bottom', 'Time', units='s', color='k')
        pen = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_voltage = self.VoltagePlot.plot(
            self.xVoltage, self.yVoltage, pen=pen)

        # Plot ParticleCount
        self.ParticleCountPlot = pg.PlotWidget(self)
        self.ParticleCountPlot.setGeometry(810, 470, 340, 240)
        self.xParticleCount = list(range(10))  # 100 time points
        self.yParticleCount = [randint(0, 0)
                               for _ in range(10)]  # 100 data points
        self.ParticleCountPlot.setBackground(QColor(70, 70, 70))
        self.ParticleCountPlot.showGrid(x=True, y=True)
        self.ParticleCountPlot.setLabel(
            'left', 'Accel Z', units='m/s²', color='k')
        self.ParticleCountPlot.setLabel('bottom', 'Time', units='s', color='k')
        pen = pg.mkPen(color=(255, 0, 0), width=3)
        self.data_line_particlecount = self.ParticleCountPlot.plot(
            self.xParticleCount, self.yParticleCount, pen=pen)

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

    def simEnableButtonFunction(self):
        print("simEnableButtonFunction")

    def disableButtonFunction(self):
        print("disableButtonFunction")

    def currentBaudrateChanged(self):
        print(self.baudrateSelector.currentText())
        print(self.baudrateSelector.currentIndex())

    def currentComChanged(self):
        print(self.comSelector.currentText())
        print(self.comSelector.currentIndex())

    def refresh(self):
        print("Refresh button clicked")

    def simulationButtonFunction(self):
        print("simulationButtonFunction")

    def cleanTelemetryTableButtonFunction(self):
        print("cleanTelemetryTableButtonFunction")
        self.telemetryTable.clearContents()

    def update_plots_data(self):

        print("SONX: temp, press ", self.instanceTemprature, self.instancePressure)

        self.instanceTemprature = float(self.instanceTemprature)
        self.xTemprature = self.xTemprature[1:]  # Remove the first y element.
        self.xTemprature.append(self.xTemprature[-1] + 1)
        self.yTemprature = self.yTemprature[1:]  # Remove the first
        self.yTemprature.append(self.instanceTemprature)
        self.data_line_temprature.setData(self.xTemprature, self.yTemprature)

        self.instancePressure = float(self.instancePressure)
        self.xPressure = self.xPressure[1:]  # Remove the first y element.
        self.xPressure.append(self.xPressure[-1] + 1)
        self.yPressure = self.yPressure[1:]  # Remove the first
        self.yPressure.append(self.instancePressure)  # Add a new random value.
        self.data_line_pressure.setData(self.xPressure, self.yPressure)

        self.instanceAltitude = float(self.instanceAltitude)
        self.xAltitude = self.xAltitude[1:]  # Remove the first y element.
        self.xAltitude.append(self.xAltitude[-1] + 1)
        self.yAltitude = self.yAltitude[1:]  # Remove the first
        self.yAltitude.append(self.instanceAltitude)  # Add a new random value.
        self.instanceAltitude = 1
        self.data_line_altitude.setData(self.xAltitude, self.yAltitude)

        self.instanceAccelX = float(self.instanceAccelX)
        self.xAirSpeed = self.xAirSpeed[1:]  # Remove the first y element.
        self.xAirSpeed.append(self.xAirSpeed[-1] + 1)
        self.yAirSpeed = self.yAirSpeed[1:]  # Remove the first
        self.yAirSpeed.append(self.instanceAccelX)  # Add a new random value.
        self.instanceAirSpeed = 0
        self.data_line_airspeed.setData(self.xAirSpeed, self.yAirSpeed)
        self.instanceAltitude = float(self.instanceAltitude)

        self.instanceAccelY = float(self.instanceAccelY)
        self.xVoltage = self.xVoltage[1:]  # Remove the first y element.
        self.xVoltage.append(self.xVoltage[-1] + 1)
        self.yVoltage = self.yVoltage[1:]  # Remove the first
        self.yVoltage.append(self.instanceAccelY)  # Add a new random value.
        self.instanceVoltage = 0
        self.data_line_voltage.setData(self.xVoltage, self.yVoltage)

        self.instanceAccelZ = float(self.instanceAccelZ)
        self.xParticleCount = self.xParticleCount[1:]
        self.xParticleCount.append(self.xParticleCount[-1] + 1)
        self.yParticleCount = self.yParticleCount[1:]  # Remove the first
        self.yParticleCount.append(self.instanceAccelZ)
        self.instanceParticleCount = 0
        # Update the data.
        self.data_line_particlecount.setData(
            self.xParticleCount, self.yParticleCount)

        self.instanceTemprature = 0
        self.instancePressure = 0
        self.instanceAltitude = 0
        self.instanceAccelX = 0
        self.instanceAccelY = 0
        self.instanceAccelZ = 0

    def timerForOneSecond(self):
        if self.connectButtonActivated == True:

            # telemetryDataS = hf.createRandomTestTelemetryObject()
            self.line = self.ser.readline().decode('utf-8').rstrip()
            self.commaData = altitudeSilinecek.parseData(self.line)
            self.commaData.append("SON")  # ! kaldırılacak

            # testTelemetryDatas.append(telemetryDataS)
            self.COUNTER_FROM_START = self.COUNTER_FROM_START + 1
            print(" [INFO - COUNTER]   ", self.COUNTER_FROM_START)
            self.updaterInterface()

    def checkNewDataAndCreateTelemetryObject(self, listData):
        newObject = tc.TelemetryData()
        print("LEN: ", len(listData))
        if len(listData) == 24:
            if listData[0] == '1007':
                if listData[-1] == "SON":
                    newObject.setDatabyCommaSepratedDataList(listData)

        current_time = QTime.currentTime()
        time_text = current_time.toString('hh:mm:ss')
        newObject.mission_time = time_text
        newObject.packet_count = self.packetCount
        self.packetCount += 1
        return newObject

    def updaterInterface(self):

        # self.newTelemetryObject = self.turnListToTelemetryObject(self.commaData)
        self.newTelemetryObject = self.checkNewDataAndCreateTelemetryObject(
            self.commaData)

        # print(self.newTelemetryObject)
        testTelemetryDatas.append(self.newTelemetryObject)
        print(testTelemetryDatas[len(testTelemetryDatas) - 1])

        if testTelemetryDatas[len(testTelemetryDatas) - 1].mission_time != None:
            self.timeText.setText(
                "Mission Time: " + testTelemetryDatas[len(testTelemetryDatas) - 1].mission_time)
            self.telemetryTable.setRowCount(len(testTelemetryDatas))
            for i in range(0, len(testTelemetryDatas)):
                tempList = testTelemetryDatas[i]
                for j in range(0, len(testTelemetryDatas[i].getDataAsList())):
                    tabloya_eklenecek_veri = tempList.getDataAsList()
                    tabloya_eklenecek_veri = tabloya_eklenecek_veri[j]
                    tabloya_eklenecek_veri = QTableWidgetItem(
                        str(tabloya_eklenecek_veri))
                    self.telemetryTable.setItem(i, j, tabloya_eklenecek_veri)

            self.telemetryTable.setCurrentCell(len(testTelemetryDatas) - 1, 0)
            self.instanceAltitude = testTelemetryDatas[len(
                testTelemetryDatas) - 1].altitude
            self.instanceTemprature = testTelemetryDatas[i].temp
            self.instancePressure = testTelemetryDatas[i].pressure
            # # self.instanceAirSpeed = testTelemetryDatas[i].air_speed
            # self.instanceVoltage = testTelemetryDatas[i].volt
            # # self.instanceParticleCount = testTelemetryDatas[i].particle_count
            self.instanceLatitude = testTelemetryDatas[len(
                testTelemetryDatas) - 1].gps_latitude
            self.instanceLongtitude = testTelemetryDatas[len(
                testTelemetryDatas) - 1].gps_longitude
            self.instanceGpsAltitude = testTelemetryDatas[len(
                testTelemetryDatas) - 1].gps_altitude
            self.instanceSatS = testTelemetryDatas[len(
                testTelemetryDatas) - 1].gps_sats
            self.instancePitch = testTelemetryDatas[len(
                testTelemetryDatas) - 1].tilt_x
            self.instanceRoll = testTelemetryDatas[len(
                testTelemetryDatas) - 1].tilt_y
            self.instanceAccelX = testTelemetryDatas[len(
                testTelemetryDatas) - 1].accelX
            self.instanceAccelY = testTelemetryDatas[len(
                testTelemetryDatas) - 1].accelY
            self.instanceAccelZ = testTelemetryDatas[len(
                testTelemetryDatas) - 1].accelZ
            print("ACCEL X Y Z ", self.instanceAccelX,
                  self.instanceAccelX, self.instanceAccelX)

            self.altitudeText.setText(
                "Altitude: {} m".format(self.instanceAltitude))
            self.latitudeLongitudeAltitudeSatsText.setText("Lat: {}  Long: {}  Alt: {} m  Sats: {}".format(
                self.instanceLatitude, self.instanceLongtitude, self.instanceGpsAltitude, self.instanceSatS))
            self.pitchRollYawText.setText("      Pitch: {}°              Roll: {}°".format(
                self.instancePitch, self.instanceRoll))

            # if self.progressBarCounter >= 100:
            #     self.progressBarCounter = 0
            # self.progressBar.setValue(self.progressBarCounter)
            # self.progressPercentLabel.setText(
            #     "{}%".format(self.progressBarCounter))
            # self.progressBarCounter += 1

            # if self.stateTableCounter > 3:
            #     self.stateTableCounter = 0
            # self.stateTable.selectRow(self.stateTableCounter)
            # self.stateTableCounter += 1

            self.instanceLatitude, self.instanceLongtitude = 40.739969, 30.331882  # ! Burası silinecek
            self.mapView.load(QUrl("https://www.openstreetmap.org/#map=14/{}/{}".format(
                self.instanceLatitude, self.instanceLongtitude)))

            print("SELF PRESSURE ", self.instancePressure)

            # hf.satir_ekleyen_fonksiyon(testTelemetryDatas[len(testTelemetryDatas) - 1].getDataCommaSeparated(), "/Users/agahozdemir/Documents/Programming/Turkish-Defenders-CanSAT-GCS-GUI/telemetryData.txt")

            print("LIST ", testTelemetryDatas[5], testTelemetryDatas[5],
                  testTelemetryDatas[5], testTelemetryDatas[5])
        else:
            print(" [INFO] None Data Error")

    def playAudioFile(self):
        # full_file_path = os.path.join(os.getcwd(), '/Users/agahozdemir/Desktop/Sakarya University.mp3')
        # url = QUrl.fromLocalFile(full_file_path)
        # content = QMediaContent(url)

        # self.player.setMedia(content)
        # self.player.play()
        pass

    def update_battery_percentage(self):
        output = subprocess.check_output(
            ['pmset', '-g', 'batt']).decode("utf-8")
        for line in output.split('\n'):
            if 'InternalBattery' in line:
                self.battery_percentage = int(
                    line.split()[2].replace('%;', ''))
        self.batteryProgressBar.setValue(self.battery_percentage)
        self.batteryText.setText(
            "Battery Percent: %" + str(self.battery_percentage))

        current_time = QTime.currentTime()
        time_text = current_time.toString('hh:mm:ss')
        self.timeLabel.setText(time_text)

    def save_to_csv(self):
        pass

    def showExitDialog(self):
        msgBox = QMessageBox()
        msgBox.setText("Are you sure you want to exit the program?")
        msgBox.setWindowTitle("Exit Confirmation")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            sys.exit()

    def enterFullScreen(self):

        if self.isFullScreen == False:
            self.showFullScreen()
            self.isFullScreen = True
            self.fullScreenButton.setText("Open Normal Screen")

        elif self.isFullScreen == True:
            self.showNormal()
            self.isFullScreen = False
            self.fullScreenButton.setText("Open Full Screen")


class BlackWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(85, 175, 1010, 480)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QBrush(QColor(30, 30, 30)))


class VTKWidget(QVTKRenderWindowInteractor):
    def __init__(self, parent=None):
        super().__init__(parent)
        renderer = vtk.vtkRenderer()
        self.GetRenderWindow().AddRenderer(renderer)

        reader = vtk.vtkOBJReader()
        reader.SetFileName("DigerDosyalar/model1.obj")
        reader.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(reader.GetOutput())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        renderer.AddActor(actor)

        renderer.SetBackground(0.2, 0.3, 0.4)

        self.Initialize()
        self.Start()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
