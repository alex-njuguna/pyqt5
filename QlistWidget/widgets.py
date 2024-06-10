from PySide6.QtWidgets import *

class Widget(QWidget):
    """define a class widget that inherits from QWidget"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QListWidget')

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        self.list_widget.addItem('one')
        self.list_widget.addItems(['two', 'three'])

        add_item_button = QPushButton('Add Item')
        add_item_button.clicked.connect(self.add_item)

        delete_item_button = QPushButton('delete Item')
        delete_item_button.clicked.connect(self.delete_item)

        item_count_button = QPushButton('Item count')
        item_count_button.clicked.connect(self.item_count)

        selected_items_button = QPushButton('Selected Items')
        selected_items_button.clicked.connect(self.selected_items)

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(add_item_button)
        layout.addWidget(delete_item_button)
        layout.addWidget(item_count_button)
        layout.addWidget(selected_items_button)

        self.setLayout(layout)


    def current_item_changed(self, item):
        if item:
            print(f'current item: {item.text()}')
        else:
            print('no items')

    def current_text_changed(self, text):
        if text:
            print(f'current text changed: {text}')
        else:
            print('no items')

    def add_item(self):
        self.list_widget.addItem('new item')

    def delete_item(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def item_count(self):
        print(f'Items: {self.list_widget.count()}')

    def selected_items(self):
        items = self.list_widget.selectedItems()
        for item in items:
            print(item.text())
