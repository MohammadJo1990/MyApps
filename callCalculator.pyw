import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoCalculator import *
class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButtonPlus.clicked.connect(self.addtwonum)
		self.ui.pushButtonSubtract.clicked.connect(self.subtracttwonum)
		self.ui.pushButtonMultiply.clicked.connect(self.multiplytwonum)
		self.ui.pushButtonDivide.clicked.connect(self.dividetwonum)		
	def addtwonum(self):
		if len(self.ui.lineEditFirstNumber.text()) !=0:
			a=int(self.ui.lineEditFirstNumber.text())
		else:
			a = 0			
		if len(self.ui.lineEditSecondNumber.text()) !=0:
			b=int(self.ui.lineEditSecondNumber.text())
		else:
			b = 0
		sum = a+b
		self.ui.labelResult.setText("The Sum is "+str(sum))
	def subtracttwonum(self):
		if len(self.ui.lineEditFirstNumber.text()) !=0:
			a=int(self.ui.lineEditFirstNumber.text())
		else:
			a = 0			
		if len(self.ui.lineEditSecondNumber.text()) !=0:
			b=int(self.ui.lineEditSecondNumber.text())
		else:
			b = 0
		sub= a-b
		self.ui.labelResult.setText("The Subtraction is "+str(sub))
	def multiplytwonum(self):
		if len(self.ui.lineEditFirstNumber.text()) !=0:
			a=int(self.ui.lineEditFirstNumber.text())
		else:
			a = 0			
		if len(self.ui.lineEditSecondNumber.text()) !=0:
			b=int(self.ui.lineEditSecondNumber.text())
		else:
			b = 0
		mul = a*b
		self.ui.labelResult.setText("The Multiplication "+str(mul))
	def dividetwonum(self):
		if len(self.ui.lineEditFirstNumber.text()) !=0:
			a=int(self.ui.lineEditFirstNumber.text())
		else:
			a = 0			
		if len(self.ui.lineEditSecondNumber.text()) !=0:
			b=int(self.ui.lineEditSecondNumber.text())
		else:
			b = 0
		try:
		        divi = a/b
		except ZeroDivisionError:
        		divi = 0		
		self.ui.labelResult.setText("The Division is "+str(round(divi, 2)))
if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	app.exit(app.exec_())