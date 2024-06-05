from PySide6.QtWidgets import QWidget, QLabel

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Label as image')