from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
import sys

from sb import ScrumBoard

if __name__ == "__main__":
    app = QApplication(sys.argv)

    screen = ScrumBoard()
    screen.show()

    sys.exit(app.exec_())

