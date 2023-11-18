from PyQt6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QLineEdit


class OutWgt(QWidget):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.msg = QLineEdit(msg)
        # self.msg.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.msg.setReadOnly(True)
        self.layout.addWidget(self.msg)
        self.out = QLineEdit("Не определено")
        # self.out.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.out.setReadOnly(True)
        self.layout.addWidget(self.out)

    def setOut(self, out):
        self.out.setText(str(out))

    def getValue(self):
        return float(self.out.text())