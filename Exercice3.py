from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ihm3(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400,300)
        self.setWindowTitle("IHM")
        self.icon = QIcon("image.png")
        self.setWindowIcon(self.icon)

        self.layout = QVBoxLayout()

        self.label = QLabel("Hello Word")
        self.label.setAlignment(Qt.AlignCenter)

        self.barre = QProgressBar()
        self.barre.setValue(50)

        self.line = QLineEdit()
        self.button =  QPushButton("Clic if you can")
        self.button.setToolTip("HEY, you win")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.barre)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = ihm3()
   win.show()
   app.exec_()
