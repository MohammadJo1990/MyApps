import sqlite3
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QAction ,QFileDialog
from createtable import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.createtable)
        
    def createtable(self):
        conn = sqlite3.connect("11.db")
        self.ui.label.setText("data base connected")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users (EmailAddress text NOT NULL,password integer NOT NULL);""")
        self.ui.label.setText("table created")
        
        

    

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
