from PyQt6.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QSizePolicy, QLineEdit, QRadioButton

from libs.OutWgt import OutWgt


class OutWgtRadio(OutWgt):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
        self.radio = QRadioButton()
        self.layout.addWidget(self.radio)
        self.out.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.msg.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
    def getRadio(self):
        return self.radio

    def isChecked(self):
        return self.radio.isChecked()