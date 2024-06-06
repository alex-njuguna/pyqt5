from PySide6.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('check boxes and radio buttons')


        # os checkboxes setup
        os = QGroupBox('select operating system')

        windows = QCheckBox('Windows')
        windows.toggled.connect(self.windows_toggled)

        linux = QCheckBox('Linux')
        linux.toggled.connect(self.linux_toggled)

        mac = QCheckBox('mac')
        mac.toggled.connect(self.mac_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)


        # exclusive checkboxes
        drinks = QGroupBox('Choose your drink')
        beer = QCheckBox('beer')
        tea = QCheckBox('tea')
        juice = QCheckBox('juice')
        beer.setChecked(True)

        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(tea)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.setExclusive(True)

        drinks_layout = QVBoxLayout()
        drinks_layout.addWidget(beer)
        drinks_layout.addWidget(tea)
        drinks_layout.addWidget(juice)
        drinks.setLayout(drinks_layout)


        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        self.setLayout(layout)


    def windows_toggled(self, checked):
        if checked:
            print('Windows box checked')
        else:
            print('Windows box unchecked')

    def linux_toggled(self, checked):
        if checked:
            print('Linux box checked')
        else:
            print('Linux box unchecked')

    def mac_toggled(self, checked):
        if checked:
            print('Mac box checked')
        else:
            print('Mac box unchecked')

