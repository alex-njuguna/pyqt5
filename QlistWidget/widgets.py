from PySide6.QtWidgets import *

class Widget(QWidget):
    """define a class widget that inherits from QWidget"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QListWidget')

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)

        self.list_widget.addItem('one')
        self.list_widget.addItems(['two', 'three'])

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)

        self.setLayout(layout)