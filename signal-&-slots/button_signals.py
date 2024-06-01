import sys
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked(data):
    print("you clicked this button, button checked:", data)

app = QApplication()

button = QPushButton()
button.setText('Click me!')
button.setCheckable(True)

button.clicked.connect(button_clicked)

button.show()

app.exec()