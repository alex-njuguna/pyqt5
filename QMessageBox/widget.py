from PySide6.QtWidgets import QWidget, QPushButton, QMessageBox, QVBoxLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QMessageBox')

        # define buttons
        button_hard = QPushButton('Hard')
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton('critical')
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton('question')
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton('information')
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton('warning')
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton('about')
        button_about.clicked.connect(self.button_clicked_about)

        # define layout
        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    def button_clicked_hard(self):
        # setting up the message box he hard way
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle('message box')
        message.setText('sth happened')
        message.setInformativeText('sth has happened during...')
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        # dispay the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print('user clicked ok!')
        else:
            print('user cancelled')

    def button_clicked_critical(self):
        ret = QMessageBox.critical(self, 'message title', 'crirtical message!', QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print('user clicked ok!')
        else:
            print('user cancelled')

    def button_clicked_question(self):
        print('question')

    def button_clicked_information(self):
        print('information')

    def button_clicked_warning(self):
        print('warning')

    def button_clicked_about(self):
        print('about')


