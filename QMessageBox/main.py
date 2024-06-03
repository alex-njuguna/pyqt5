from PySide6.QtWidgets import QApplication

from widget import Widget

app = QApplication()

window = Widget(app)
window.show()

app.exec()
