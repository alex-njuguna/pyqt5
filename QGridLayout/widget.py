from PySide6.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('grid layout')

        button1 = QPushButton('one')
        button2 = QPushButton('two')
        button3 = QPushButton('three')
        button4 = QPushButton('four')
        button5 = QPushButton('five')
        button6 = QPushButton('six')
        button7 = QPushButton('seven')

        