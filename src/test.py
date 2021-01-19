
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

from sb import *

if __name__ == "__main__":
    import sys 
    app = QApplication([sys.argv])
    print("hello")
    task = Task(title="Test Task", description="This is the test description for the task. adding a bunch of task here because I want to check the behavior")
    screen = task

    screen.show()

    sys.exit(app.exec_())