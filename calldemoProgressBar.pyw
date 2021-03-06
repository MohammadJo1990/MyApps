import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from demoProgressBar import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonStart.clicked.connect(self.updateprogressbar)
        self.show()
    def updateprogressbar(self):
        x = 0
        while x < 1000 :
            x += 0.0001
            self.ui.progressBar.setValue(x)
            
if __name__ == "__main__":
    app =QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())