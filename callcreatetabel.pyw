import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore
from demoCreateTable import *
import sqlite3
from sqlite3 import Error
import traceback
tabledefinition=""
class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCreateTable.clicked.connect(self.createTable)
        self.ui.pushButtonAddColumn.clicked.connect(self.addColumns)
        #self.conn.commit()
        self.show()

    def addColumns(self):
        global tabledefinition         
        if tabledefinition=="":           
            pass 
            #tabledefinition="CREATE TABLE IF NOT EXISTS "+self.ui.lineEditTableName.text()+" ("+self.ui.lineEditColumnName.text()+" "+self.ui.ComboBoxDataType.itemText(self.ui.ComboBoxDataType.currentIndex())+");"
        else:
            tabledefinition+=", "+self.ui.lineEditColumnName.text()+" "+self.ui.ComboBoxDataType.itemText(self.ui.ComboBoxDataType.currentIndex())+");"
        self.ui.lineEditColumnName.setText("")
        self.ui.lineEditColumnName.setFocus()

    def createTable(self):
        global tabledefinition 
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text()+".db")
            self.ui.labelResponse.setText("Database is connected")
            c = conn.cursor()
            #tabledefinition+=""
            if tabledefinition=="":           
                tabledefinition="CREATE TABLE IF NOT EXISTS "+self.ui.lineEditTableName.text()+" ("+self.ui.lineEditColumnName.text()+" "+self.ui.ComboBoxDataType.itemText(self.ui.ComboBoxDataType.currentIndex())+");"
            else:
                tabledefinition+=", "+self.ui.lineEditColumnName.text()+" "+self.ui.ComboBoxDataType.itemText(self.ui.ComboBoxDataType.currentIndex())+");"
            c.execute(tabledefinition)
            conn.commit()
            self.ui.labelResponse.setText("Table is successfully created")
        except Error as e:
            self.ui.labelResponse.setText("Error in creating table")
            print(str(e))
            traceback.print_exc()
        finally:
            conn.close()


            
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    w = MyForm()
    w.show()
    sys.exit(app.exec_())  