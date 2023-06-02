import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QAction, QMenu, QHBoxLayout

from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QChart, QChartView, QLineSeries

class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.chart1 = QChartView(self.generate_chart())
        self.chart2 = QChartView(self.generate_chart())
        self.layout.addWidget(self.chart1)
        self.layout.addWidget(self.chart2)
        self.setLayout(self.layout)

    def generate_chart(self):
        series = QLineSeries()
        for i in range(10):
            series.append(i, random.randint(0, 100))
        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.legend().hide()
        return chart


class SecondPage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.chart1 = QChartView(self.generate_chart())
        self.chart2 = QChartView(self.generate_chart())
        self.chart3 = QChartView(self.generate_chart())
        self.layout.addWidget(self.chart1)
        self.layout.addWidget(self.chart2)
        self.layout.addWidget(self.chart3)
        self.setLayout(self.layout)

    def generate_chart(self):
        series = QLineSeries()
        for i in range(10):
            series.append(i, random.randint(0, 100))
        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.legend().hide()
        return chart


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Sayfa")
        self.setGeometry(200, 200, 600, 400)

        self.main_widget = QWidget(self)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.menu_layout = QHBoxLayout()
        self.menu_widget = QWidget(self)
        self.menu_widget.setLayout(self.menu_layout)

        self.main_menu = QMenu(self)
        self.page_menu = self.main_menu.addMenu("Sayfalar")

        self.main_page_action = QAction("Ana Sayfa", self)
        self.main_page_action.triggered.connect(self.open_main_page)
        self.page_menu.addAction(self.main_page_action)

        self.second_page_action = QAction("2. Sayfa", self)
        self.second_page_action.triggered.connect(self.open_second_page)
        self.page_menu.addAction(self.second_page_action)

        self.menu_layout.addWidget(self.main_menu)
        self.menu_layout.addStretch()

        self.main_layout.addWidget(self.menu_widget)
        self.main_layout.addWidget(MainPage())

        self.setCentralWidget(self.main_widget)

    def open_main_page(self):
        self.main_layout.removeWidget(self.centralWidget())
        self.centralWidget().setParent(None)
        self.main_layout.addWidget(MainPage())

    def open_second_page(self):
        self.main_layout.removeWidget(self.centralWidget())
        self.centralWidget().setParent(None)
        self.main_layout.addWidget(SecondPage())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
