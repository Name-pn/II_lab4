
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QMouseEvent
from PyQt6.QtWidgets import QWidget, QApplication
class ClickWidget(QWidget):
    def __init__(self, rows, columns, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(250, 250)
        self.n = rows
        self.m = columns
        self.matr = [[0 for i in range(self.m)] for j in range(self.n)]

    def paintEvent(self, event):
        self.unitX = int(self.width() / self.m)
        self.unitY = int(self.height() / self.n)
        qp = QPainter()
        qp.begin(self)
        noPen = QPen()
        noPen.setWidth(0)
        brush = QBrush(QColor(0, 0, 0))
        qp.setPen(noPen)
        for i in range(self.n):
            for j in range(self.m):
                if (self.matr[i][j]):
                    qp.setBrush(brush)
                    qp.drawRect(j*self.unitX, i*self.unitY, self.unitX, self.unitY)
                else:
                    qp.setBrush(QColor(255, 255, 255))
                    qp.drawRect(j * self.unitX, i * self.unitY, self.unitX, self.unitY)

        qp.end()


    def mousePressEvent(self, event:QMouseEvent):
        pos = event.pos()
        i = int(pos.y() / self.unitY)
        j = int(pos.x() / self.unitX)
        self.matr[i][j] = (self.matr[i][j] + 1) % 2
        self.update()

    def getMatr(self):
        return self.matr