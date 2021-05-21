import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demosliders import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.horizontalScrollBarSugarLevel.valueChanged.connect(self.scrollhorizontal)
       
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scrollvertical)
        
        self.ui.horizontalSliderBloodPressure.valueChanged.connect(self.sliderhorizontal)
        self.ui.verticalSliderCholestrolLevel.valueChanged.connect(self.slidervertical)
        self.show()
        
    def scrollhorizontal(self, value):
        self.ui.lineEditResult.setText("Suger Level  "+str(value))
    
        
    def scrollvertical(self, value):
        self.ui.lineEditResult.setText("Pulse Rate "+str(value))
        
    def sliderhorizontal(self, value):
        self.ui.lineEditResult.setText("blood Pressure "+str(value))
    def slidervertical(self, value):
        self.ui.lineEditResult.setText("Cholestrol Level "+str(value))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
    