import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoListWidget3 import *
class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.pushButtonAdd.clicked.connect(self.additem)
        self.show()
    def additem(self):
        
        self.ui.listWidgetSelectedItems.addItem(str(self.ui.lineEditFoodItem.text()))
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
        