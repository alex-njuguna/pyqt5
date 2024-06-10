from PySide6.QtWidgets import *

class Widget(QWidget):
    """define a class widget that inherits from QWidget"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QListWidget')

       