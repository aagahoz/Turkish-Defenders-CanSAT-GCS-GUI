from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Refresh Button Example")
        self.setGeometry(100, 100, 300, 200)

        # QIcon nesnesi yükleyin
        refresh_icon = QIcon("/Users/agahozdemir/Documents/Programming/Turkish-Defenders-CanSAT-GCS-GUI/DigerDosyalar/Örnekler/refresh.png")
        # QPushButton nesnesi oluşturun
        refresh_button = QPushButton(refresh_icon, "Refresh", self)
        refresh_button.setGeometry(100, 100, 90, 25)
        refresh_button.clicked.connect(self.refresh)

    def refresh(self):
        print("Refresh button clicked")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
