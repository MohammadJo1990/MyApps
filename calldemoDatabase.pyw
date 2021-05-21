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
        
        self.ui.pushButtonCreateDB.clicked.connect(self.createdb)
        self.show()
    def createdb(self):
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text()+".db")
            self.ui.labelResponse.setText("Database Created")
        except error as e:
            self.ui.labelResponse.setText("Error happened !")
        finally:
            conn.close()
		

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    w = MyForm()
    w.show()
    sys.exit(app.exec_())  