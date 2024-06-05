import os
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Label as image')
        try:
            self.setWindowIcon(QIcon('images/icon.png'))
        except Exception as e:
            print("Error setting window icon:", e)
        
        self.resize(400, 300)

        label = QLabel()
        image_path = 'images/minions.jpg'
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(QSize(400, 300))
        label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)