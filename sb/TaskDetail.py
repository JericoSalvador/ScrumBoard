from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

class TaskDetail(QDialog): 

    def __init__(self, master=None, task=None):
        super().__init__(master)

        self.setWindowTitle(task.title)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.combobox = QComboBox()
        self.addItemsToCombobox()

        self.buttonBox.rejected.connect(self.reject)

        layout = QFormLayout()
        titleLabel = QLabel(task.title)
        layout.addRow(titleLabel)
        titleLabel.setStyleSheet("font-size: 18px; padding: 5px; background-color: orange;")
        descriptionLabel = QLabel(task.description)
        descriptionLabel.setWordWrap(True)
        descriptionLabel.setStyleSheet("font-size: 14px;")
        layout.addRow(descriptionLabel)
        layout.addRow(QLabel("Move to:"),self.combobox)
        layout.addRow(self.buttonBox)

        self.setLayout(layout)

    def addItemsToCombobox(self): 
        self.combobox.addItem("To Do")
        self.combobox.addItem("In Progress")
        self.combobox.addItem("Testing")
        self.combobox.addItem("Done")
