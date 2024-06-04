from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Text Editor')

        self.text_edit = QTextEdit()

        copy_button = QPushButton('copy')
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton('cut')
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton('paste')
        paste_button.clicked.connect(self.text_edit.paste)

        undo_button = QPushButton('undo')
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton('redo')
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton('plain text')
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton('html')
        set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton('clear')
        clear_button.clicked.connect(self.text_edit.clear)

