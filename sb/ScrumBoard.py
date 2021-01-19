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
        button.clicked.connect(lambda : self.addTask(self.taskLayouts['To Do']))
        self.layout.addWidget(button, 2, 0, 1, 2)

    def createRemoveTaskButton(self): 
        button = QPushButton(text="Move Task")
        button.clicked.connect(lambda: self.moveTask('To Do', 'In Progress', 'hello'))
        self.layout.addWidget(button, 2, 2, 1, 2)

    def createNewSprintButton(self): 
        pass

    def addTaskToLayout(self,layout, taskName, taskDescription):
        layout.addWidget(Task(title=taskName, description=taskDescription))

    def addTask(self, layout):
        dialog = TaskDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            taskName, taskDescription = dialog.getValues()

            if taskName != "": 
                self.addTaskToLayout(layout, taskName, taskDescription)
                self.db.addTask(taskName, taskDescription)
                self.db.addTaskToSprint(taskName, "Sprint1")


    def loadTask(self): 
        for status in self.titles: 

            for title, description in self.db.getTaskWithStatus(status): 
                    layout = self.taskLayouts[status]
                    layout.addWidget(Task(title=title, description=description))

    def removeTaskFromLayout(self, layout, taskname):
        for i in range(layout.count()):
            layout_item = layout.itemAt(i)
            if (layout_item): 
                task = layout_item.widget()
                if task.title == taskname: 
                    task.setParent(None)
                    title = task.title
                    description = task.description
                    layout.removeItem(layout.itemAt(i))
                    print('removed', taskname)

                    return title, description

    def moveTask(self, oldStatus, newStatus, taskname): 
        srcLayout = self.taskLayouts[oldStatus]
        destLayout = self.taskLayouts[newStatus]
        title, description = self.removeTaskFromLayout(srcLayout, taskname)
        self.addTaskToLayout(destLayout, title, description)
        self.db.changeStatus(taskname, newStatus)
        
    
