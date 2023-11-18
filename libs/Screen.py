from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QButtonGroup, QMessageBox

import libs.Neurons
from libs import Dataset
from libs.ClickWidget import ClickWidget
from libs.OutWgt import OutWgt
from libs.OutWgtRadio import OutWgtRadio

class Screen(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('ИНС для определения цифр')
        self.wgt = QWidget()
        self.button = QPushButton("Распознать")
        self.button2 = QPushButton("Обучить")
        self.layout = QGridLayout()
        self.clickWdg = ClickWidget(5, 5)
        self.layout.addWidget(self.clickWdg, 2, 0, 8, 1)
        self.layout.addWidget(self.button, 1, 0, 1, 1)
        self.layout.addWidget(self.button2, 0, 0, 1, 1)
        self.wgt.setLayout(self.layout)
        self.initOutRadio()
        self.initOut()
        self.setCentralWidget(self.wgt)
        self.button.clicked.connect(self.predict)
        self.button2.clicked.connect(self.learn)

    def learn(self):
        idx = -1
        for i in range(len(self.outsRadio)):
            if self.outsRadio[i].isChecked():
                idx = i
                break
        if (idx != -1):
            libs.Neurons.singleTrain(self.clickWdg.getMatr(), idx)
            self.updateErrors()
        else:
            box = QMessageBox()
            box.setWindowTitle("Ошибка")
            box.setText("Для обучения выберите радиокнопку соответствующую введенной цифре")
            box.setIcon(QMessageBox.Icon.Information)
            box.exec()

    def initOut(self):
        self.outs = []
        self.outs.append(OutWgt('Значение функции ошибки на обучающей выборке'))
        self.outs.append(OutWgt('Значение функции ошибки на тестовой выборке'))
        self.updateErrors()
        self.layout.addWidget(self.outs[0], 11, 0, 1, 2)
        self.layout.addWidget(self.outs[1], 12, 0, 1, 2)
        self.button3 = QPushButton("Выполнить обучение на обучающей выборке 100 эпох")
        self.layout.addWidget(self.button3, 13, 0, 1, 2)
        self.button3.clicked.connect(self.learnNetwork)

    def updateErrors(self):
        self.outs[0].setOut(libs.Neurons.getError(Dataset.x_train, Dataset.y_train))
        self.outs[1].setOut(libs.Neurons.getError(Dataset.x_test, Dataset.y_test))
    def learnNetwork(self):
        libs.Neurons.train(Dataset.x_train, Dataset.y_train)
        self.updateErrors()

    def initOutRadio(self):
        self.outsRadio = []
        self.group = QButtonGroup()

        for i in range(10):
            self.outsRadio.append(OutWgtRadio(str(i)))
            self.layout.addWidget(self.outsRadio[i], i, 1, 1, 1)
            self.group.addButton(self.outsRadio[i].getRadio())

    def predict(self):
        matr = self.clickWdg.getMatr()
        y = libs.Neurons.run_network(matr)
        self.setPredicts(y)
        self.highlight()

    def setPredicts(self, y):
        size = y.shape
        for i in range(size[0]):
            self.outsRadio[i].setOut(y[i])

    def findMax(self):
        index = -1
        lmax = -1.
        for i in range(len(self.outsRadio)):
            if (self.outsRadio[i].getValue() > lmax):
                lmax = self.outsRadio[i].getValue()
                index = i
        return index

    def highlight(self):
        i = self.findMax()
        self.outsRadio[i].setStyleSheet('color: green')
        for j in range(i):
            self.outsRadio[j].setStyleSheet('color: red')
        for j in range(i + 1, len(self.outsRadio)):
            self.outsRadio[j].setStyleSheet('color: red')