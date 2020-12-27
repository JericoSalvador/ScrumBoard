from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
# from PyQt5.QtGui import *
import sys

def main():
    app = QApplication(sys.argv)

    screen = ScrumBoard()
    screen.show()

    sys.exit(app.exec_())

class ScrumBoard(QWidget):
    def __init__(self, parent = None): 
        super().__init__(parent)

        self.resize(1000, 600)
        self.setWindowTitle("Scrum Board")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.titles = ['To Do', 'In Progress', 'Testing', 'Done']
        self.createTitles()
        self.taskAreas = []
        self.taskLayouts = []
        self.taskWidgets = []
        self.createTaskArea()

        self.createAddTaskButton()
    
    def createTitles(self):

        for i in range(len(self.titles)): 
            label = QLabel(self.titles[i])
            label.setAlignment(Qt.AlignTop)
            label.setAlignment(Qt.AlignHCenter)
            self.layout.addWidget(label, 0, i)


    def createTaskArea(self): 
        for i in range(len(self.titles)):
            widget = QWidget()
            layout = QFormLayout()
            widget.setLayout(layout)

            self.taskLayouts.append(layout)
            self.taskWidgets.append(widget)

            scrollArea = QScrollArea()
            scrollArea.setWidgetResizable(True)
            scrollArea.setWidget(widget)

            self.layout.addWidget(scrollArea, 1, i)
            self.taskAreas.append(scrollArea)

    def createAddTaskButton(self): 
        button = QPushButton(text="Add Task")
        button.clicked.connect(self.addTask)
        self.layout.addWidget(button, 2, 0, 1, 4)

    def addTask(self): 
        dialog = TaskDialogue()
        if dialog.exec_() == QDialog.Accepted:
            taskName, taskDescription = dialog.getValues()

            if taskName != "": 
                layout = self.taskLayouts[0]
                layout.addWidget(Task(title=taskName, description=taskDescription))


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

            
class TaskDialogue(QDialog): 
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
        
    


if __name__ == "__main__":
    main()