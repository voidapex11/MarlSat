import sys
import pyqtgraph as pg
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, pyqtSignal
import math
import random


class FunkyGraphs(pg.PlotWidget):
    changed = pyqtSignal(int, name="changed")
    def __init__(self,num):
        super().__init__()

        self.number = num

    def mousePressEvent(self, ev):
        self.changed.emit(self.number)

class MainWindow(QMainWindow):
    def add_graph(self,n):
        graph_n = FunkyGraphs(n)
        self.graphs.append(graph_n)
        graph_n.changed.connect(lambda e : self.toggleBig(e))
        self.refreshGraph(graph_n)

        self.layout.addWidget(graph_n)


    def __init__(self):
        super().__init__()
        self.temperature = []
        self.five_point_moving_average = []

        self.x_points = []
        self.y_points = []

        graph1 = FunkyGraphs(1)
        graph2 = FunkyGraphs(2)
        self.graphs = [graph1, graph2]
        graph1.changed.connect(lambda e : self.toggleBig(e))
        graph2.changed.connect(lambda e : self.toggleBig(e))
        self.refreshGraph(graph1)
        self.refreshGraph(graph2)

        randomise_data_button = QPushButton()
        randomise_data_button.setText("Randomise Data")

        randomise_data_button.clicked.connect(self.refreshHandler)

        self.layout = QHBoxLayout()
        self.layout.addWidget(graph1)
        self.layout.addWidget(graph2)
        self.layout.addWidget(randomise_data_button)


        widget1 = QWidget()
        widget1.setLayout(self.layout)


        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(widget1)
        # self.stacked_layout.addWidget(graph1)
        # self.stacked_layout.addWidget(graph2)

        widget = QWidget()
        widget.setLayout(self.stacked_layout)

        self.setCentralWidget(widget)

    def plotData(self, graph):
        graph.clear()
        graph.plot([i for i in range(len(self.temperature))], self.temperature)
        pen = pg.mkPen(color=(255,100,100))
        graph.plot(self.x_points, self.y_points, pen=pen)

        # self.graph.plot([i + 4 for i in range(len(self.five_point_moving_average))], self.five_point_moving_average)

    def randomiseData(self):
        self.temperature = [20 - 0.1 * i - 2 * random.random() for i in range(20)]
        self.five_point_moving_average = []

        for i in range(len(self.temperature)):
            try:
                self.five_point_moving_average.append(sum([self.temperature[4 + i - a] for a in range(5)]) / 5)
            except:
                pass

    def refreshGraph(self, graph):
        self.randomiseData()
        self.coef()
        self.plotData(graph)

    def coef(self):
        n = len(self.temperature)
        x = [i for i in range(len(self.temperature))]
        m_x = sum(x)/len(self.temperature)
        m_y = sum(self.temperature)/len(self.temperature)
        SS_xx = 0
        SS_yx = 0
        for i in range(len(self.temperature)):
            SS_yx += x[i] * self.temperature[i]
            SS_xx += x[i]**2
        SS_xx -= n*m_x*m_x
        SS_yx -= n*m_x*m_y

        b_1 = SS_yx/SS_xx
        b_0 = m_y - b_1*m_x

        self.x_points = [x[0], x[-1]]
        self.y_points = [b_0 + b_1*x[0], b_0 + b_1*x[-1]]

    def refreshHandler(self):
        self.refreshGraph(self.graphs[0])
        self.refreshGraph(self.graphs[1])

    def toggleBig(self, num):
        self.stacked_layout.setCurrentIndex(num)





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()