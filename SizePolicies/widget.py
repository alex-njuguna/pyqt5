from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('size policies')