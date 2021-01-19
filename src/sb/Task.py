from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

from .TaskDetail import TaskDetail
from .db import BoardDatabase
class Task(QWidget): 
    def __init__(self, parent=None, title="", description=""): 
        self.stylesheet = """
        font-size:18px;
        background-color: orange; 
        padding: 3px;
        """
        super().__init__(parent)
        self.parent = parent
        self.title = title
        self.description = description

        self.label = QLabel(text=title)
        self.label.setStyleSheet(self.stylesheet)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def taskName(self):
        return self.title

    def getDescription(self): 
        return self.description

    def mousePressEvent(self, event):
        dialog = TaskDetail(self,task=self)
        if dialog.exec_() == QDialog.Accepted:
            db = BoardDatabase()
            oldStatus = db.getStatus(self.title)
            newStatus = dialog.getNewStatus()
            self.parent.moveTask(oldStatus, newStatus, self.title)
            db.changeStatus(taskname = self.title, status=newStatus)
        
        elif dialog.deleteTask(): 
            print("trying to delete")
            db = BoardDatabase()
            oldStatus = db.getStatus(self.title)
            self.parent.removeTaskFromLayout(oldStatus, self.title)
            db.removeTask(self.title)
        

if __name__ == "__main__":
    import sys 
    app = QApplication([])
    screen = Task( title = "task name", description="task description")
    screen.show()

    sys.exit(app.exec_())
