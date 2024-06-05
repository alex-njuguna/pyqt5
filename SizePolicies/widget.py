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

        button_1 = QPushButton('button 1')
        button_2 = QPushButton('button 2')
        button_3 = QPushButton('button 3')

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1, 2)
        h_layout_2.addWidget(button_2, 1)
        h_layout_2.addWidget(button_3, 1)

        default_layout = QVBoxLayout()
        default_layout.addLayout(h_layout_1)
        default_layout.addLayout(h_layout_2)

        self.setLayout(default_layout)


