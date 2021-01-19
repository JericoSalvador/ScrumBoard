from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

class Confirm(QDialog): 
    def __init__(self, parent = None, message = ""): 
        super().__init__(parent)

        self.confirm = False

        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        self.buttonbox.rejected.connect(self.reject)
        self.buttonbox.accepted.connect(self.onAccept)
        self.label = QLabel(message)

        self.layout.addRow(self.label)

        self.layout.addRow(self.buttonbox)

    def onAccept(self):
        self.confirm = True
        self.accept()
        self.close()
    
    def __bool__(self): 
        return self.confirm