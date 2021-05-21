import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from demoListWidgetOp import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.psuhButtonAdd.clicked.connect(self.addItem)
        self.ui.pushButtonEdit.clicked.connect(self.editItem)
        self.ui.pushButtonDelete.clicked.connect(self.deleteItem)
        self.ui.pushButtonDeleteAll.clicked.connect(self.deleteAllItem)
        self.show()        
    def addItem(self):     
        self.ui.listWidgetSelectedItems.addItem(str(self.ui.lineEditFoodItem.text()))
        self.ui.lineEditFoodItem.clear()
        self.ui.lineEditFoodItem.setFocus()        
    def editItem(self):
        row = self.ui.listWidgetSelectedItems.currentRow()
        newtext, ok=QInputDialog.getText(self, "Enter new text", "Enter new text")
        if ok and (len(newtext) !=0):
            self.ui.listWidgetSelectedItems.takeItem(self.ui.listWidgetSelectedItems.currentRow())
            self.ui.listWidgetSelectedItems.insertItem(row,QListWidgetItem(newtext))
    def deleteItem(self):
        self.ui.listWidgetSelectedItems.takeItem(self.ui.listWidgetSelectedItems.currentRow())
    def deleteAllItem(self):
        self.ui.listWidgetSelectedItems.clear()           
if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
        