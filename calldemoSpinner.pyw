import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoSpinner import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        """ you can use both valueChanged signal or editingFinished """
        self.ui.spinBoxBookQty.valueChanged.connect(self.result1)
        self.ui.doubleSpinBoxSugarWeight.valueChanged.connect(self.result2)
        self.show()
        
    def result1(self):
        if len(self.ui.lineEditBookPrice.text())!=0 :
            bookPrice = int(self.ui.lineEditBookPrice.text())
        else:
            bookPrice = 0
        totalBookAmount = self.ui.spinBoxBookQty.value() * bookPrice
        self.ui.lineEditBookAmount.setText(str(totalBookAmount))
        
    def result2(self):
        if len(self.ui.lineEditSugarPrice.text())!=0:
            sugerPrice = float(self.ui.lineEditSugarPrice.text())
        else:
            sugerPrice = 0
        totalSugerAmount = self.ui.doubleSpinBoxSugarWeight.value() * sugerPrice
        self.ui.lineEditSugarAmount.setText(str(round(totalSugerAmount, 2)))
        totalBookAmount = int(self.ui.lineEditBookAmount.text())
        totalAmount = totalBookAmount + totalSugerAmount 
        self.ui.labelTotalAmount.setText(str(round(totalAmount, 2)))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
    