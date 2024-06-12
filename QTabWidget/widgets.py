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



        "buttons tab"
        button_widget = QWidget()

        button_1 = QPushButton('button 1')
        button_2 = QPushButton('button 2')
        button_3 = QPushButton('button 3')

        button_layout = QVBoxLayout()
        button_layout.addWidget(button_1)
        button_layout.addWidget(button_2)
        button_layout.addWidget(button_3)
        button_widget.setLayout(button_layout)

        
        "add Widget tabs to the main tab"
        tab_widget.addTab(widget_form, 'Information')
        tab_widget.addTab(button_widget, 'Buttons')


        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)