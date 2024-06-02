import os
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle('Custom Main window')

        # menu bar and menu actions
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('File')
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction('Copy')
        edit_menu.addAction('Cut')
        edit_menu.addAction('Paste')
        edit_menu.addAction('Undo')
        edit_menu.addAction('Redo')

        menu_bar.addMenu('Window')
        menu_bar.addMenu('&Setting')
        menu_bar.addMenu('&Help')

        # working with toolbars
        tool_bar = QToolBar('Main tool bar')
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)

        tool_bar.addAction(quit_action)

        action1 = QAction('Some action', self)
        action1.setStatusTip('Some message here')
        action1.triggered.connect(self.toolbar_button_click)
        tool_bar.addAction(action1)

        icon_path = os.path.join('main-window', 'start.png')
        action2 = QAction(QIcon(icon_path), 'Some other action', self)
        action2.setStatusTip('some other action message here')
        action2.triggered.connect(self.toolbar_button_click)
        tool_bar.addAction(action2)

        tool_bar.addSeparator()
        tool_bar.addWidget(QPushButton('Click here'))

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        print('Tool bar button clicked')
