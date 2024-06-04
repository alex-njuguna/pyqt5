from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel and QLineEdit')

        label = QLabel('Fullname: ')
        self.line_edit = QLineEdit()

        button = QPushButton('Grab data')
        self.text_holder_label = QLabel('I AM HERE')