from PySide6.QtWidgets import *

class Widget(QWidget):
    "Canvas for the entire app"
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QTabWidget')

        tab_widget = QTabWidget(self)

        "information form"
        widget_form = QWidget()
        label = QLabel('fullname: ')
        line_edit = QLineEdit()

        widget_form_layout = QHBoxLayout()
        widget_form_layout.addWidget(label)
        widget_form_layout.addWidget(line_edit)
        widget_form.setLayout(widget_form_layout)


        tab_widget.addTab(widget_form, 'Information')


        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)