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

        # set buttons layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        # set app layout
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    def set_plain_text(self):
        self.text_edit.setPlainText('This is plain text with no formatting')

    def set_html(self):
        self.text_edit.setHtml("<b>This text is bold</b> and has <font color='red'>red color</font>.")
