import sys

from PyQt6.QtWidgets import QWidget, QApplication, QLabel
import libs.Neurons
from libs.Screen import Screen

app = QApplication(sys.argv)
# libs.Neurons.train(libs.Dataset.x_train, libs.Dataset.y_train)
# libs.Neurons.go_forward_all(libs.Dataset.x_train)
window = Screen()
window.show()
app.exec()