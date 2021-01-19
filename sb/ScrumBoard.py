from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

from .db import BoardDatabase
from .Task import Task
from .TaskDialog import TaskDialog  

class ScrumBoard(QWidget):
    currentSprint = None
    taskAreas = []
    taskLayouts = {}
    taskWidgets = []

    def __init__(self, parent = None): 
        super().__init__(parent)
        self.db = BoardDatabase()
        self.resize(1000, 600)
        self.setWindowTitle("Scrum Board")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.titles = ['To Do', 'In Progress', 'Testing', 'Done']
        self.createTitles()
        self.createTaskArea()
        self.createAddTaskButton()
        self.createRemoveTaskButton()
        self.loadTask()
    
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

            self.taskLayouts[self.titles[i]] = layout
            self.taskWidgets.append(widget)

            scrollArea = QScrollArea()
            scrollArea.setWidgetResizable(True)
            scrollArea.setWidget(widget)

            self.layout.addWidget(scrollArea, 1, i)
            self.taskAreas.append(scrollArea)

    def createAddTaskButton(self): 
        button = QPushButton(text="Add Task")
        button.clicked.connect(self.addTask)
        self.layout.addWidget(button, 2, 0, 1, 2)

    def createRemoveTaskButton(self): 
        button = QPushButton(text="Delete Task")
        button.clicked.connect(lambda: self.removeTask(self.taskLayouts['To Do'], "7"))
        self.layout.addWidget(button, 2, 2, 1, 2)

    def createNewSprintButton(self): 
        pass

    def addTask(self): 
        dialog = TaskDialog()
        if dialog.exec_() == QDialog.Accepted:
            taskName, taskDescription = dialog.getValues()

            if taskName != "": 
                layout = self.taskLayouts[0]
                layout.addWidget(Task(title=taskName, description=taskDescription))

                self.db.addTask(taskName, taskDescription)
                self.db.addTaskToSprint(taskName, "Sprint1")

    def loadTask(self): 
        for _, title, description in self.db.getAllTasks(): 
                layout = self.taskLayouts['To Do']
                layout.addWidget(Task(title=title, description=description))

    def removeTask(self, layout, taskname):
        for i in range(layout.count()):
            layout_item = layout.itemAt(i)
            if (layout_item): 
                task = layout_item.widget()
                if taskname == task.title: 
                    task.setParent(None)
                    layout.removeItem(layout.itemAt(i))
                    print('removed', taskname)

    
