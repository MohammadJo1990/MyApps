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
        c.execute("""CREATE TABLE IF NOT EXISTS emp (id integer PRIMARY KEY, name text, joindate date, basicsalary float, socialsecurity float, address text);""")
        c.execute("""CREATE TABLE IF NOT EXISTS addtions (id integer , name text, adddate date, type bool, amount float, FOREIGN KEY(id) REFERENCES emp(id));""")
        c.execute("""CREATE TABLE IF NOT EXISTS deductions (id integer,name text, dedate date,type bool,amount float, FOREIGN KEY(id) REFERENCES emp(id));""")
        c.execute("""CREATE TABLE IF NOT EXISTS sickleaves (id integer,name text, type text, fromdate date, todate date, noofdays integer, amount float, FOREIGN KEY(id) REFERENCES emp(id));""")
        c.execute("""CREATE TABLE IF NOT EXISTS annualleaves (id integer,name text, fromdate date, todate date , noofdays integer, amout float, FOREIGN KEY(id) REFERENCES emp(id));""")
        c.execute("""CREATE TABLE IF NOT EXISTS unpaidleaves (id integer,name text, fromdate date, todate date noofdays integer, amount float, FOREIGN KEY(id) REFERENCES emp(id));""")
        c.execute("""CREATE TABLE IF NOT EXISTS publicholidays (dates date);""")
        c.execute("""CREATE TABLE IF NOT EXISTS empattendance (id integer,fromdate date, todate date, totallogin float, tobededucted float, tobeadded float, skip bool, FOREIGN KEY(id) REFERENCES emp(id));""")
        c.execute("""CREATE TABLE IF NOT EXISTS payroll (id integer,name text, totalde float, totaladd float, netsalary float, FOREIGN KEY(id) REFERENCES emp(id));""")
        self.ui.label.setText("table created")
        
        

    

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
