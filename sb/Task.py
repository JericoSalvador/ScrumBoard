from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

class Task(QWidget): 
    def __init__(self, parent=None, title="", description=""): 
        super().__init__(parent)

        self.title = title
        self.description = description

        self.button = QPushButton(text=title)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def taskName(self):
        return self.title

    def getDescription(self): 
        return self.description
