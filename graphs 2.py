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
        graph_n_s = FunkyGraphs(n)
        graph_n_b = FunkyGraphs(-n)

        graph_collection = [graph_n_s,graph_n_b]

        self.graphs.append(graph_collection)

        graph_n_s.changed.connect(lambda e : self.toggleBig(e))
        graph_n_b.changed.connect(lambda e: self.toggleBig(e))

        self.refreshGraph(graph_collection)


    def layoutGraphs(self,total):
        for i in range(total // 2):
            self.vert_layouts.append(QVBoxLayout())

        for i in range(len(self.vert_layouts)):
            self.layout.addLayout(self.vert_layouts[i])
            self.vert_layouts[i].addWidget(self.graphs[2*i][0])
            self.vert_layouts[i].addWidget(self.graphs[2 * i + 1][0])

        if total%2 == 1:
            self.layout.addWidget(self.graphs[-1][0])

        for i in self.graphs:
            self.stacked_layout.addWidget(i[1])


    def __init__(self):
        super().__init__()
        self.temperature = []
        self.five_point_moving_average = []

        self.x_points = []
        self.y_points = []

        self.graphs = []

        randomise_data_button = QPushButton()
        randomise_data_button.setText("Randomise Data")

        randomise_data_button.clicked.connect(self.refreshHandler)

        self.layout = QHBoxLayout()
        self.stacked_layout = QStackedLayout()
        self.vert_layouts = []

        widget1 = QWidget()
        widget1.setLayout(self.layout)

        self.stacked_layout.addWidget(widget1)

        number_of_graphs = 5
        for i in range(number_of_graphs):
            self.add_graph(i+1)

        self.layoutGraphs(number_of_graphs)

        self.layout.addWidget(randomise_data_button)

        widget = QWidget()
        widget.setLayout(self.stacked_layout)

        self.setCentralWidget(widget)

    def plotData(self, graphs):
        for i in range(2):
            graphs[i].clear()
            graphs[i].plot([i for i in range(len(self.temperature))], self.temperature)
            pen = pg.mkPen(color=(255,100,100))
            graphs[i].plot(self.x_points, self.y_points, pen=pen)

        # self.graph.plot([i + 4 for i in range(len(self.five_point_moving_average))], self.five_point_moving_average)

    def randomiseData(self):
        self.temperature = [20 - 0.1 * i - 2 * random.random() for i in range(20)]
        self.five_point_moving_average = []

        for i in range(len(self.temperature)):
            try:
                self.five_point_moving_average.append(sum([self.temperature[4 + i - a] for a in range(5)]) / 5)
            except:
                pass

    def refreshGraph(self, graphs):
        self.randomiseData()
        self.coef()
        self.plotData(graphs)

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
        for i in self.graphs:
            self.refreshGraph(i)

    def toggleBig(self, num):
        if num > 0:
            self.stacked_layout.setCurrentIndex(num)
        else:
            self.stacked_layout.setCurrentIndex(0)





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()