import os
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Label as image')
        self.resize(400, 300)

        label = QLabel()
        image_path = 'images/minions.webp'
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(400, 300)
        label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)