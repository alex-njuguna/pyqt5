from PySide6.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('grid layout')

        # define widgets
        button1 = QPushButton('one')
        button2 = QPushButton('two')
        button3 = QPushButton('three')
        button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button4 = QPushButton('four')
        button5 = QPushButton('five')
        button6 = QPushButton('six')
        button7 = QPushButton('seven')

        # define layout
        layout = QGridLayout()
        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 0, 1, 1, 2)
        layout.addWidget(button3, 1, 0, 2, 1)
        layout.addWidget(button4, 1, 1)
        layout.addWidget(button5, 1, 2)
        layout.addWidget(button6, 2, 1)
        layout.addWidget(button7, 2, 2)

        self.setLayout(layout)




