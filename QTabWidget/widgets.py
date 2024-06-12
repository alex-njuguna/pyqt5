from PySide6.QtWidgets import *

class Widget(QMainWindow):
    "Canvas for the entire app"
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QTabWidget')