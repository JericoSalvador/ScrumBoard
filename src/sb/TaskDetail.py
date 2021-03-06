from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

from .Confirm import Confirm
class TaskDetail(QDialog): 

    def __init__(self, master=None, task=None):
        super().__init__(master)

        self.setWindowTitle(task.title)
        self.setStyleSheet("background-color:white;")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok| QDialogButtonBox.Cancel)
        self.combobox = QComboBox()
        self.addItemsToCombobox()
        self.deleteTaskButton = QPushButton(text="Delete Task")
        self.deleteTaskButton.clicked.connect(self.deleteButtonPressed)

        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QFormLayout()
        self.titleLabel = QLabel(task.title)
        layout.addRow(self.titleLabel)
        self.titleLabel.setStyleSheet("font-size: 18px; padding: 5px; background-color: orange;")
        descriptionLabel = QLabel(task.description)
        descriptionLabel.setWordWrap(True)
        descriptionLabel.setStyleSheet("font-size: 14px;")
        layout.addRow(descriptionLabel)
        layout.addRow(QLabel("Move to:"),self.combobox)
        layout.addRow(self.buttonBox)
        layout.addRow(self.deleteTaskButton)

        self.setLayout(layout)
        self.delete = False

    def addItemsToCombobox(self): 
        self.combobox.addItem("To Do")
        self.combobox.addItem("In Progress")
        self.combobox.addItem("Testing")
        self.combobox.addItem("Done")

    def onAccept(self):
        self.newStatus = self.combobox.currentText()
        self.accept()
        self.close()

    def getNewStatus(self): 
        return self.newStatus
    
    def deleteButtonPressed(self):
        confirmDelete = Confirm(parent=self, message="Are you sure you want to delete?")
        confirmDelete.exec_()
        if(confirmDelete): 
            self.delete = True
            self.close()

    def deleteTask(self):
        return self.delete

