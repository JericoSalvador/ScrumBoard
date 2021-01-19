
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

from sb import Confirm

if __name__ == "__main__":
    import sys 
    app = QApplication([sys.argv])
    screen = Confirm("Are you sure?") 
    screen.exec_()

    print(bool(screen))
    
