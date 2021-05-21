import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
from demoDatabase import *
import sqlite3
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)    
        self.ui.pushButtonCreateTable.clicked.connect(self.createtb)
        self.ui.pushButtonAddColumn.clicked.connect(self.createcol)
        self.show()
    def createcol(self):
        global tabeldef
        if tabeldef=="":
            tabeldef = "CREATE TABEL IF NOT EXIST "+self.ui.lineEditTableName.text()+" (" + self.uilineEditColumnName.text()+" " +self.ui.ComboBoxDataType.itemText(self.ui.ComboBoxDataType.currentIndex())
        else:
            tabeldef+=","+self.ui.lineEditColumnName.text()+" "+self.ui.ComboBoxDataType.itemText(self.ui.ComboBoxDataType.currentIndex()
        self.ui.lineEditColumnName.setText("")
        self.ui.lineEditColumnName.setFocus()   
    def createtb(self):
        global tabeldef
        try:
            conn = sqlite3.connec(self.ui.lineEditDBName.text()+".db")
            self.ui.labelResponse.setText("database created sucessfully")
            cur = conn.cursor()
            tabeldef+=");"
            c.execute(tabeldef)
            self.ui.labelResponse.setText("Table Created sucessfully")
        except errora as e :
            self.ui.labelResponse.setText("Some errors happenned !")
        finally:
            conn.close()
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    w = MyForm()
    w.show()
    sys.exit(app.exec_())  