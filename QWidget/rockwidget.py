from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rock Widget')

        # define layout
        button_layout = QHBoxLayout()

        button1 = QPushButton('Button 1')
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton('Button 2')
        button2.clicked.connect(self.button2_clicked)

        # add buttons to the layout
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        # set layout
        self.setLayout(button_layout)

    def button1_clicked(self):
        print('button 1 clicked!')

    def button2_clicked(self):
        print('button 2 clicked!')
