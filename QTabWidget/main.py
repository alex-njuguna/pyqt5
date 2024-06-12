import sys
from PySide6.QtWidgets import QApplication

from widgets import Widget

app = QApplication(sys.argv)

window = Widget()
window.show()

app.exec()
