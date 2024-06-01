import sys
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked():
    print("you clicked this button, didn't you?")

app = QApplication()

button = QPushButton()
button.setText('Click me!')

button.clicked.connect(button_clicked)

button.show()

app.exec()