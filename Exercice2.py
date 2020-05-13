from PySide2.QtWidgets import *

class ihm2(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("M.Drucker")
        self.layout = QGridLayout()

        self.label = QLabel("Présentateur un peu fou")
        self.txt = QTextEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.txt)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = ihm2()
   win.show()
   app.exec_()
