

def initUI():

    count = 0
    connectButtonActivated = False
    testDataCounter = 0
    instanceAltitude = 0
    instanceTemprature = 0
    instancePressure = 0
    instanceAirSpeed = 0
    instanceVoltage = 0
    instanceParticleCount = 0
    instanceLatitude = 0
    instanceLongtitude = 0
    instanceGpsAltitude = 0
    instanceSatS = 0
    instancePitch = 0
    instanceRoll = 0
    instanceYaw = 0

    progressBarCounter = 0
    stateTableCounter = 0
    COUNTER_FROM_START = 0


    comList = dict()

    isFullScreen = False

    central_widget = QWidget(
    setCentralWidget(central_widget)
    black_widget = BlackWidget(central_widget)
    black_widget.setGeometry(40, 180, 1120, 540)

    # add connect button
    connectButton = QPushButton('Connect', 
    connectButton.setGeometry(QtCore.QRect(60, 72, 100, 32))
    connectButton.clicked.connect(connectButtonFunction)
    connectButton.setFont(QFont("Calibri", 15))

    # add disconnect button
    disconnectButton = QPushButton('Disconnect', 
    disconnectButton.setGeometry(QtCore.QRect(176, 72, 120, 32))
    disconnectButton.clicked.connect(disconnectButtonFunction)
    disconnectButton.setFont(QFont("Calibri", 15))

    # add enable button
    enableButton = QPushButton('Enable', 
    enableButton.setGeometry(QtCore.QRect(325, 29, 100, 32))
    enableButton.clicked.connect(enableButtonFunction)
    enableButton.setFont(QFont("Calibri", 15))

    # add disable button
    disableButton = QPushButton('Disable', 
    disableButton.setGeometry(QtCore.QRect(325, 60, 100, 32))
    disableButton.clicked.connect(disableButtonFunction)
    disableButton.setFont(QFont("Calibri", 15))

    # add disconnect button
    simulationButton = QPushButton('Simulation', 
    simulationButton.setGeometry(QtCore.QRect(315, 91, 120, 32))
    simulationButton.clicked.connect(simulationButtonFunction)
    simulationButton.setFont(QFont("Calibri", 15))

    # add import csv button
    importCsvButton = QPushButton('Import CSV', 
    importCsvButton.setGeometry(110, 112, 140, 32)
    importCsvButton.setFont(QFont("Calibri", 15))

    # add table widget button
    telemetryTableButton = QPushButton(
    telemetryTableButton.setText("Clear Table")
    telemetryTableButton.setGeometry(QtCore.QRect(1200, 945, 110, 32))
    # telemetryTableButton.clicked.connect(cleanTelemetryTableButtonFunction)
    telemetryTableButton.setFont(QFont("Calibri", 15))

    # add save csv button
    save_button = QPushButton("Save To CSV", 
    save_button.clicked.connect(save_to_csv)
    save_button.setGeometry(QtCore.QRect(1310, 945, 130, 32))
    # telemetryTableButton.clicked.connect(save_to_csv)
    save_button.setFont(QFont("Calibri", 15))

    # add com selector
    comSelector = QComboBox(
    comSelector.setGeometry(QtCore.QRect(30, 35, 170, 40))
    # comSelector.addItem('COM1')
    # comSelector.addItem('COM2')
    # comSelector.addItem('COM3')
    # comSelector.addItem('COM4')
    comList = hf.getUsbSerialDevices(hf.getComList())
    for key, value in comList.items():
        comSelector.addItem(value)
    comSelector.currentTextChanged.connect(currentComChanged)
    comSelector.setFont(QFont("Calibri", 16))

    # add baud rate selector
    baudrateSelector = QComboBox(
    baudrateSelector.setGeometry(QtCore.QRect(200, 35, 100, 40))
    baudrateSelector.addItem('9600')
    baudrateSelector.addItem('115200')
    baudrateSelector.addItem('230400')
    baudrateSelector.addItem('460800')
    baudrateSelector.addItem('921600')
    baudrateSelector.currentTextChanged.connect(
        currentBaudrateChanged)
    baudrateSelector.setFont(QFont("Calibri", 16))

    # QIcon nesnesi yükleyin
    refresh_icon = QIcon("/Users/agahozdemir/Documents/Programming/Turkish-Defenders-CanSAT-GCS-GUI/DigerDosyalar/Örnekler/refresh.png")
    # QPushButton nesnesi oluşturun
    refresh_button = QPushButton(refresh_icon, "Refresh", 
    refresh_button.setGeometry(70, 8, 90, 25)
    refresh_button.clicked.connect(refresh)

    # add progress bar
    progressBar = QtWidgets.QProgressBar(
    progressBar.setGeometry(QtCore.QRect(870, 50, 250, 40))
    progressBar.setProperty("value", 24)
    progressBar.setObjectName("progressBar")
    progressBar.setValue(0)
    progressBar.setMaximum(100)
    progressBar.setMinimum(0)
    # add progress bar label
    progressBarLabel = QLabel(
    progressBarLabel.setText("Mission Progress ")
    progressBarLabel.setFont(QFont('Arial', 18))
    progressBarLabel.setGeometry(QtCore.QRect(920, 27, 140, 20))
    progressBarLabel.setStyleSheet("color: rgb(179, 226, 229);")
    # add progress percent label
    progressPercentLabel = QLabel(
    progressPercentLabel.setFont(QFont('Arial', 18))
    progressPercentLabel.setText("0%")
    progressPercentLabel.setGeometry(QtCore.QRect(1067, 27, 100, 20))
    progressPercentLabel.setStyleSheet("color: rgb(179, 226, 229);")

    # add telemetry table widget
    telemetryTable = QtWidgets.QTableWidget(
    telemetryTable.setGeometry(QtCore.QRect(25, 740, 1159, 230))
    telemetryTable.setObjectName("telemetryTable")

    telemetryTable.setColumnCount(20)
    telemetryTable.setRowCount(10)
    telemetryTable.setHorizontalHeaderLabels(["Team ID", "Mission Time", "Packet Count", "Mode", "State", "Altitude", "HS Deployed",
                                                    "PC Deployed", "Mast Raised", "Temp", "Pressure", "Volt", "GPS Time", "GPS Altitude", "GPS Latitude", "GPS Longitude", "GPS SatS", "Tilt X", "Tilt Y", "CMD Echo"])
    # print(telemetryTable.rowCount())
    telemetryTable.setSortingEnabled(True)
    telemetryTable.setCornerButtonEnabled(False)
    telemetryTable.setGridStyle(QtCore.Qt.SolidLine)
    telemetryTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    telemetryTable.setSelectionBehavior(QAbstractItemView.SelectRows)
    telemetryTable.setSelectionMode(QAbstractItemView.SingleSelection)
    telemetryTable.setAlternatingRowColors(True)
    telemetryTable.setShowGrid(True)
    telemetryTable.setWordWrap(False)
    telemetryTable.setCornerButtonEnabled(False)
    # select one row
    # telemetryTable.setCurrentCell(8, 0)

    # set table column width
    telemetryTable.setColumnWidth(0, 50)  # team id
    telemetryTable.setColumnWidth(1, 90)  # mission time
    telemetryTable.setColumnWidth(2, 90)  # packet count
    telemetryTable.setColumnWidth(3, 50)  # altitude
    telemetryTable.setColumnWidth(4, 60)  # pressure
    telemetryTable.setColumnWidth(5, 50)  # temp
    telemetryTable.setColumnWidth(6, 50)  # volt
    telemetryTable.setColumnWidth(7, 70)  # gps Time
    telemetryTable.setColumnWidth(8, 80)  # gps latitude
    telemetryTable.setColumnWidth(9, 90)  # gps longtitude
    telemetryTable.setColumnWidth(10, 80)  # gps altitude
    telemetryTable.setColumnWidth(11, 70)  # gps sats
    telemetryTable.setColumnWidth(12, 70)  # air speed
    telemetryTable.setColumnWidth(13, 85)  # particle count
    telemetryTable.setColumnWidth(14, 45)  # pitch
    telemetryTable.setColumnWidth(15, 45)  # roll
    telemetryTable.setColumnWidth(16, 45)  # yaw
    telemetryTable.setColumnWidth(17, 45)  # 
    telemetryTable.setColumnWidth(18, 45)  # 
    telemetryTable.setColumnWidth(19, 45)  # 
    # set table row height
    for i in range(0, telemetryTable.rowCount()):
        telemetryTable.setRowHeight(i, 20)

    # chose a row to highlight green
    telemetryTable.selectRow(16)
    telemetryTable.setStyleSheet(
        "QTableWidget::item:selected {background-color: YellowGreen;}")
    telemetryTable.setFrameStyle(QFrame.Panel | QFrame.Sunken)

    # map view
    mapView = QWebEngineView(
    mapView.setGeometry(1230, 180, 350, 350)
    mapView.load(QUrl("https://www.openstreetmap.org/#map=19/{}/{}".format(
        40.797215, 29.425327)))
    mapView.show()

    # 3D view
    imageLabel = QLabel(
    imageLabel.setGeometry(1230, 560, 350, 350)
    imageLabel.setPixmap(QPixmap("DigerDosyalar/3DMODELYENI.png"))
    imageLabel.setScaledContents(True)
    imageLabel.setAlignment(Qt.AlignCenter)
    imageLabel.setStyleSheet("background-color: white")
    imageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
    imageLabel.show()

    # add time label
    timeString = "Mission Time: "
    timeText = QLabel(
    timeText.setGeometry(460, 45, 180, 30)
    timeText.setFont(QFont('Arial', 15))
    timeText.setText(timeString + "00:00:00")
    timeText.setAlignment(Qt.AlignCenter)
    timeText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
    timeText.setStyleSheet("background-color: white")

    # Timer'ın oluşturulması
    generalTimer = QTimer()
    generalTimer.timeout.connect(timerForOneSecond)
    # Her 1000 milisaniyede bir timeout sinyali gönderir
    generalTimer.start(1000)

    # add altitude label
    altitudeString = "Altitude: 0 m"
    altitudeText = QLabel(
    altitudeText.setGeometry(935, 98, 130, 30)
    altitudeText.setFont(QFont('Arial', 15))
    altitudeText.setText(altitudeString)
    altitudeText.setAlignment(Qt.AlignCenter)
    # altitudeText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
    altitudeText.setStyleSheet("background-color: white")
    altitudeText.show()

    # create table
    stateTable = QTableWidget(
    stateTable.setGeometry(1150, 20, 147, 90)
    stateTable.setColumnCount(2)
    stateTable.setRowCount(4)
    # not show index
    stateTable.verticalHeader().setVisible(False)
    stateTable.horizontalHeader().setVisible(False)
    stateTable.setItem(0, 1, QTableWidgetItem("Started"))
    stateTable.setItem(1, 1, QTableWidgetItem("Not Started"))
    stateTable.setItem(2, 1, QTableWidgetItem("Not Started"))
    stateTable.setItem(3, 1, QTableWidgetItem("Not Started"))
    stateTable.setItem(0, 0, QTableWidgetItem("Launch"))
    stateTable.setItem(1, 0, QTableWidgetItem("Ascent"))
    stateTable.setItem(2, 0, QTableWidgetItem("Descent"))
    stateTable.setItem(3, 0, QTableWidgetItem("Landing"))
    stateTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    stateTable.setShowGrid(False)
    # chose a row to highlight green
    stateTable.selectRow(0)
    stateTable.setStyleSheet(
        "QTableWidget::item:selected {background-color: YellowGreen;}")
    stateTable.setFrameStyle(QFrame.Panel | QFrame.Sunken)
    stateTable.resizeColumnsToContents()
    stateTable.resizeRowsToContents()
    stateTable.show()

    # Exit button
    exitButton = QPushButton('Exit', 
    exitButton.setToolTip('Click to exit the program')
    exitButton.setStyleSheet("color: white; background-color: red;")
    exitButton.setGeometry(1530, 10, 60, 25)
    exitButton.clicked.connect(showExitDialog)
    exitButton.setFont(QFont('Comic Sans MS', 15))

    # full screen button
    fullScreenButton = QPushButton("Open Full Screen", 
    fullScreenButton.setToolTip('Click to full screen the program')
    fullScreenButton.clicked.connect(enterFullScreen)
    fullScreenButton.setStyleSheet(
        "color: white; background-color: green;")
    fullScreenButton.setGeometry(1368, 10, 160, 25)
    fullScreenButton.setFont(QFont('Comic Sans MS', 15))

    # QProgressBar Battery Percent
    batteryProgressBar = QProgressBar(
    batteryProgressBar.setGeometry(1390, 80, 160, 15)
    batteryProgressBar.setValue(0)
    batteryProgressBar.setTextVisible(True)
    # add batteryVoltage label
    batteryString = "Battery Percent: "
    batteryText = QLabel(
    batteryText.setGeometry(1394, 103, 150, 25)
    batteryText.setFont(QFont('Arial', 14))
    batteryText.setText(batteryString + "%" + "0")
    batteryText.setAlignment(Qt.AlignCenter)
    batteryText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
    batteryText.setStyleSheet("background-color: white")
    # QTimer
    timerBattery = QTimer(
    timerBattery.timeout.connect(update_battery_percentage)
    timerBattery.start(1000)

    # add instance time label
    timeLabel = QLabel(
    timeLabel.setFont(QFont('Arial', 15))
    timeLabel.setGeometry(QtCore.QRect(1440, 50, 140, 20))
    timeLabel.setStyleSheet("color: rgb(179, 226, 229);")

    # add latitude longitude altitude sats label
    latitudeLongitudeAltitudeSatsString = "Lat: 00.000000  Long: 00.000000  Alt: 000.0 m  Sats: 0"
    latitudeLongitudeAltitudeSatsText = QLabel(
    latitudeLongitudeAltitudeSatsText.setGeometry(1230, 490, 350, 40)
    latitudeLongitudeAltitudeSatsText.setFont(QFont('Arial', 13))
    latitudeLongitudeAltitudeSatsText.setText(
        latitudeLongitudeAltitudeSatsString)
    latitudeLongitudeAltitudeSatsText.setAlignment(Qt.AlignCenter)
    latitudeLongitudeAltitudeSatsText.setFrameStyle(
        QFrame.Panel | QFrame.Sunken)
    latitudeLongitudeAltitudeSatsText.setStyleSheet(
        "background-color: white")
    latitudeLongitudeAltitudeSatsText.show()

    # add pitch roll yaw label
    pitchRollYawString = "      Pitch: 0°              Roll: 0°"
    pitchRollYawText = QLabel(
    pitchRollYawText.setGeometry(1230, 890, 350, 40)
    pitchRollYawText.setFont(QFont('Arial', 13))
    pitchRollYawText.setText(pitchRollYawString)
    pitchRollYawText.setAlignment(Qt.AlignCenter)
    pitchRollYawText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
    pitchRollYawText.setStyleSheet("background-color: white")
    pitchRollYawText.show()

    # Plot Altitude
    AltitudePlot = pg.PlotWidget(
    AltitudePlot.setGeometry(50, 190, 340, 240)
    xAltitude = list(range(10))  # 100 time points
    yAltitude = [randint(0, 0) for _ in range(10)]  # 100 data points
    AltitudePlot.setBackground(QColor(70, 70, 70))
    AltitudePlot.showGrid(x=True, y=True)
    AltitudePlot.setLabel('left', 'Altitude', units='m', color='k')
    AltitudePlot.setLabel('bottom', 'Time', units='s', color='k')
    pen = pg.mkPen(color=(255, 0, 0), width=3)  # Beyaz çizgi
    data_line_altitude = AltitudePlot.plot(
        xAltitude, yAltitude, pen=pen)

    # Plot Temprature
    TempraturePlot = pg.PlotWidget(
    TempraturePlot.setGeometry(430, 190, 340, 240)
    xTemprature = list(range(10))  # 100 time points
    yTemprature = [randint(0, 0)
                        for _ in range(10)]  # 100 data points
    TempraturePlot.setBackground(QColor(70, 70, 70))
    TempraturePlot.showGrid(x=True, y=True)
    TempraturePlot.setLabel(
        'left', 'Temprature', units='C', color='k')
    TempraturePlot.setLabel('bottom', 'Time', units='s', color='k')
    pen = pg.mkPen(color=(255, 0, 0), width=3)
    data_line_temprature = TempraturePlot.plot(
        xTemprature, yTemprature, pen=pen)

    # Plot Pressure
    PressurePlot = pg.PlotWidget(
    PressurePlot.setGeometry(810, 190, 340, 240)
    xPressure = list(range(10))  # 100 time points
    yPressure = [randint(0, 0) for _ in range(10)]  # 100 data points
    PressurePlot.setBackground(QColor(70, 70, 70))
    PressurePlot.showGrid(x=True, y=True)
    PressurePlot.setLabel('left', 'Pressure', units='Pa', color='k')
    PressurePlot.setLabel('bottom', 'Time', units='s', color='k')
    pen = pg.mkPen(color=(255, 0, 0), width=3)
    data_line_pressure = PressurePlot.plot(
        xPressure, yPressure, pen=pen)

    # Plot AirSpeed
    AirSpeedPlot = pg.PlotWidget(
    AirSpeedPlot.setGeometry(50, 470, 340, 240)
    xAirSpeed = list(range(10))  # 100 time points
    yAirSpeed = [randint(0, 0) for _ in range(10)]  # 100 data points
    AirSpeedPlot.setBackground(QColor(70, 70, 70))
    AirSpeedPlot.showGrid(x=True, y=True)
    AirSpeedPlot.setLabel('left', 'Air Speed', units='m/s', color='k')
    AirSpeedPlot.setLabel('bottom', 'Time', units='s', color='k')
    pen = pg.mkPen(color=(255, 0, 0), width=3)
    data_line_airspeed = AirSpeedPlot.plot(
        xAirSpeed, yAirSpeed, pen=pen)

    # Plot Voltage
    VoltagePlot = pg.PlotWidget(
    VoltagePlot.setGeometry(430, 470, 340, 240)
    xVoltage = list(range(10))  # 100 time points
    yVoltage = [randint(0, 0) for _ in range(10)]  # 100 data points
    VoltagePlot.setBackground(QColor(70, 70, 70))
    VoltagePlot.showGrid(x=True, y=True)
    VoltagePlot.setLabel('left', 'Voltage', units='V', color='k')
    VoltagePlot.setLabel('bottom', 'Time', units='s', color='k')
    pen = pg.mkPen(color=(255, 0, 0), width=3)
    data_line_voltage = VoltagePlot.plot(
        xVoltage, yVoltage, pen=pen)

    # Plot ParticleCount
    ParticleCountPlot = pg.PlotWidget(
    ParticleCountPlot.setGeometry(810, 470, 340, 240)
    xParticleCount = list(range(10))  # 100 time points
    yParticleCount = [randint(0, 0)
                            for _ in range(10)]  # 100 data points
    ParticleCountPlot.setBackground(QColor(70, 70, 70))
    ParticleCountPlot.showGrid(x=True, y=True)
    ParticleCountPlot.setLabel(
        'left', 'Particle Count', units='m', color='k')
    ParticleCountPlot.setLabel('bottom', 'Time', units='s', color='k')
    pen = pg.mkPen(color=(255, 0, 0), width=3)
    data_line_particlecount = ParticleCountPlot.plot(
        xParticleCount, yParticleCount, pen=pen)

    # Plot Timer
    timerPlot = QtCore.QTimer()
    timerPlot.setInterval(1000)
    timerPlot.timeout.connect(update_plots_data)
    timerPlot.start()

    show()