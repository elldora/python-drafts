from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Inverse Word")
     




app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()