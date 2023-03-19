from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu

app = QApplication([])
tray_icon = QSystemTrayIcon()

# İkonu yükle
icon = QIcon()
icon.addPixmap(QPixmap("logoTeam.png"))
tray_icon.setIcon(icon)

# Menüyü oluştur
menu = QMenu()
menu.addAction("Action 1")
menu.addAction("Action 2")

tray_icon.setContextMenu(menu)
tray_icon.show()

# Bildirim göster
tray_icon.showMessage("Title", "Message")
