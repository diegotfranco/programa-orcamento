import sys
from PyQt5 import QtWidgets

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech with Tim Tutorial")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)
    
    def clicked(self):
        self.label.setText("you pressed the button!!!!!!")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myWindow()   
    win.show()
    sys.exit(app.exec_())


window()
