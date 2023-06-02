import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(40, 30, 500, 500)

        # Google Maps URL'sini yükleyerek bir WebView oluşturun
        self.mapView = QWebEngineView(self)
        self.mapView.setGeometry(30,30, 350,350)
        self.enlem = 39.744422
        self.boylam = 39.490781
        self.mapView.load(QUrl("https://www.openstreetmap.org/#map=19/{}/{}".format(self.enlem, self.boylam)))
        # self.setCentralWidget(self.mapView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
