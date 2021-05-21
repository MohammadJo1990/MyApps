import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoCalendar import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        ''' you can use selectionChanged '''
        self.ui.calendarWidget.clicked.connect(self.dispdate)
        self.show()
    def dispdate(self):
        '''or use setDisplayFormat() for formats AND MMM must be capital'''
        self.ui.dateEdit.setDisplayFormat('dd/MM/yyyy')

        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())
        self.ui.calendarWidget.hide()
        
if __name__ == "__main__":
    app =QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())