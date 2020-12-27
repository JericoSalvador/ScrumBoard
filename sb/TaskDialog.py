from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

class TaskDialog(QDialog): 
    def __init__(self, parent=None): 
        super().__init__()

        self.setWindowTitle("New Task")

        self.taskNameEdit = QLineEdit()
        self.taskDescriptionEdit = QPlainTextEdit()

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.buttonBox.accepted.connect(self.getTask)
        self.buttonBox.rejected.connect(self.reject)

        layout = QFormLayout()
        layout.addRow(QLabel("Title:"), self.taskNameEdit)
        layout.addRow(QLabel("Description:"), self.taskDescriptionEdit)
        layout.addRow(self.buttonBox)

        self.setLayout(layout)

    def getTask(self): 
        self.values =  self.taskNameEdit.text() , self.taskDescriptionEdit.toPlainText()
        self.accept()
        self.close()

    def getValues(self): 
        return self.values
        