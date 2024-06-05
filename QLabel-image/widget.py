import os
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Label as image')
        self.setMaximumWidth(700)

        label = QLabel()
        image_path = 'images/minions.webp'
        label.setPixmap(QPixmap(image_path))

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)