import os
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Label as image')

        label = QLabel()
        image_path = os.path.join('QLabel-image', 'images/minions.jpg')
        label.setPixmap(QPixmap(image_path))