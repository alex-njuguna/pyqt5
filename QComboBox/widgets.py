from PySide6.QtWidgets import *

"""frame for the entire app"""
class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QComboBox')
        self.resize(350, 200)

        self.combo_box = QComboBox(self)

        self.combo_box.addItem('Mercury')
        self.combo_box.addItem('Venus')
        self.combo_box.addItem('Earth')
        self.combo_box.addItem('Mars')
        self.combo_box.addItem('Jupiter')

        current_value_button = QPushButton('Current Value')
        current_value_button.clicked.connect(self.current_value)

        set_value_button = QPushButton('Set Value')
        set_value_button.clicked.connect(self.set_value)

        get_value_button = QPushButton('All Values')
        get_value_button.clicked.connect(self.get_values)

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(current_value_button)
        layout.addWidget(set_value_button)
        layout.addWidget(get_value_button)
        self.setLayout(layout)

    def current_value(self):
        print(f"Current value: {self.combo_box.currentText()} - Current index [{self.combo_box.currentIndex()}]")

    def set_value(self):
        self.combo_box.setCurrentIndex(2)

    def get_values(self):
        for i in range(self.combo_box.count()):
            print(f"value {self.combo_box.itemText(i)} -- index [{i}]")
