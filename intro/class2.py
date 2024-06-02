import sys
from PyQt5.QtWidgets import QApplication, QWidget

class GUIWindow(QWidget):
    def __init__(self):
        super(GUIWindow, self).__init__()
        self.initializationUI()

    def initializationUI(self):
        self.setWindowTitle('Basic GUI Form')
        self.setGeometry(300, 300, 400, 300)
        self.show()

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = GUIWindow()
    sys.exit(myapp.exec_())