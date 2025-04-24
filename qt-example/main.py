import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Inverter")

        self.label_1 = QLabel("Input", self)
        self.text_box_1 = QLineEdit(self)
        self.label_2 = QLabel("Output", self)
        self.text_box_2 = QLineEdit(self)
        self.inverse_button = QPushButton("Invert", self)

        self.text_box_2.setReadOnly(True)
        self.inverse_button.clicked.connect(self.inverse_text)

    
        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.text_box_1)
        layout.addWidget(self.label_2)
        layout.addWidget(self.text_box_2)
        layout.addWidget(self.inverse_button)

        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def inverse_text(self):
        text = self.text_box_1.text()
        self.text_box_2.setText(text[::-1])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
