import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
import time


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("Grafikler")

        self.graph_widget = QWidget(self)
        self.setCentralWidget(self.graph_widget)
        self.graph_layout = QVBoxLayout()
        self.graph_widget.setLayout(self.graph_layout)

        self.graphs = []
        for i in range(3):
            graph = plt.figure()
            self.graphs.append(graph)

        self.graph_timer = QTimer(self)
        self.graph_timer.timeout.connect(self.update_graphs)
        self.graph_timer.start(1000)

    def update_graphs(self):
        data = np.loadtxt("scripts/testGrafik/1.txt")
        for i in range(3):
            time.sleep(1)
            graph = self.graphs[i]
            graph.clf()
            ax = graph.add_subplot(111)
            ax.plot(data[:, i])
            ax.set_xlabel("Zaman (s)")
            ax.set_ylabel("Değer")
            ax.set_title("Grafik {}".format(i+1))
            ax.grid(True)
        self.graph_layout.addWidget(self.graphs[0].canvas)
        self.graph_layout.addWidget(self.graphs[1].canvas)
        self.graph_layout.addWidget(self.graphs[2].canvas)
        self.graph_widget.setLayout(self.graph_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())
