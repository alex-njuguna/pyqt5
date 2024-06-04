from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel and QLineEdit')

        label = QLabel('Fullname: ')
        self.line_edit = QLineEdit()

        # self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        # self.line_edit.textEdited.connect(self.text_edited)
        # self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.selectionChanged.connect(self.selection_changed)

        button = QPushButton('Grab data')
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel('I AM HERE')

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(button)
        layout.addWidget(self.text_holder_label)

        self.setLayout(layout)

    def button_clicked(self):
        print(f'fullname: {self.line_edit.text()}')
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self, old, new):
        print(f'old position: {old}  new position: {new}')

    def editing_finished(self):
        self.text_holder_label.setText(self.line_edit.text())

    def selection_changed(self):
        self.text_holder_label.setText(self.line_edit.selectedText())
        
    def text_edited(self, new_text):
        print(f'new text: {new_text}')