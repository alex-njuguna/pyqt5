from PySide6.QtWidgets import *

"""frame for the entire app"""
class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QComboBox')