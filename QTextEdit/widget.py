from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text Editor')