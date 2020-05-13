from PySide2.QtWidgets import *

class window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.layoutVertical = QVBoxLayout()

        self.label = QLabel("Ceci est un QLabel")
        self.button = QPushButton("Ceci est un QPushButton")
        self.button2 = QPushButton("Cancel")

        self.layoutVertical.addWidget(self.label)
        self.layoutVertical.addWidget(self.button)
        self.layoutVertical.addWidget(self.button2)

        self.setLayout(self.layoutVertical)

if __name__ == "__main__":
   app = QApplication([])
   win = window()
   win.show()
   app.exec_()




