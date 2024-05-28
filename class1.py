# import sys to access command line arguments
import sys
"""
QWidget - create an empty GUI
QApplication - application handler
"""
from PyQt5.QtWidgets import QWidget, QApplication


myapp = QApplication(sys.argv)
my_window = QWidget()

my_window.setWindowTitle('Basic GUI Form')
my_window.resize(400, 350)

my_window.show()

sys.exit(myapp.exec_())