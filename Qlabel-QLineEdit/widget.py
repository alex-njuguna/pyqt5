from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel and QLineEdit')

        label = QLabel('Fullname: ')
        self.line_edit = QLineEdit()

        self.line_edit.textChanged.connect(self.text_changed)

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