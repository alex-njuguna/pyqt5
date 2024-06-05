from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('size policies')

        label = QLabel('some data')
        line_edit = QLineEdit()

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)