import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from demoComboBox import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBoxAccountType.currentIndexChanged.connect(self.combomethod)
        self.show()
    def combomethod(self):
       
        self.ui.labelAccountType.setText("Account Type is "+str(self.ui.comboBoxAccountType.currentText()))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
    