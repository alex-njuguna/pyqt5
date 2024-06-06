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



        layout = QVBoxLayout()
        layout.addWidget(os)
        self.setLayout(layout)


    def windows_toggled(self):
        pass

    def linux_toggled(self):
        pass

    def mac_toggled(self):
        pass

