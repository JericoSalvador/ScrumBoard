from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

from .TaskDetail import TaskDetail
class Task(QWidget): 
    def __init__(self, parent=None, title="", description=""): 
        self.stylesheet = """
        background-color: orange; 
        font-size:18px;
        border: 1px solid black; 
        padding: 3px;
        """
        super().__init__(parent)

        self.title = title
        self.description = description

        self.label = QLabel(text=title)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.setStyleSheet(self.stylesheet)

    def taskName(self):
        return self.title

    def getDescription(self): 
        return self.description

    def mousePressEvent(self, event):
        dialog = TaskDetail(self,task=self)
        if dialog.exec_() == QDialog.Accepted:
            newStatus = dialog.getNewStatus()
            print(newStatus)
        

if __name__ == "__main__":
    import sys 
    app = QApplication([])
    screen = Task( title = "task name", description="task description")
    screen.show()

    sys.exit(app.exec_())
