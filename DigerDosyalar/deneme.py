from PyQt5 import *

app = QtWidgets.QApplication([])

# Create a QWidget instance
widget = QtWidgets.QWidget()

# Set the background color to a modern dark color on Mac OS
widget.setStyleSheet("background-color: #222D32;")

# Show the widget
widget.show()

# Run the main application loop
app.exec_()
