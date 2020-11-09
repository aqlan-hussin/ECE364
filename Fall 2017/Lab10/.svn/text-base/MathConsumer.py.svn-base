import sys

from PySide.QtGui import *
from calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)

        self.btnCalculate.clicked.connect(self.performOperation)

    def performOperation(self):
        if self.edtNumber1.text() == "" or self.edtNumber2.text() == "":
            self.edtResult.setText("E")
        if "." in self.edtNumber1.text() or "." in self.edtNumber2.text():
            try:
                n1 = float(self.edtNumber1.text())
                n2 = float(self.edtNumber2.text())
                if self.cboOperation.currentIndex() == 0:
                    result = n1 + n2
                    self.edtResult.setText(str(result))
                elif self.cboOperation.currentIndex() == 1:
                    result = n1 - n2
                    self.edtResult.setText(str(result))
                elif self.cboOperation.currentIndex() == 2:
                    result = n1 * n2
                    self.edtResult.setText(str(result))
                else:
                    result = n1 / n2
                    self.edtResult.setText(str(result))
            except:
                self.edtResult.setText("E")
        else:
            try:
                n1 = int(self.edtNumber1.text())
                n2 = int(self.edtNumber2.text())
                if self.cboOperation.currentIndex() == 0:
                    result = n1 + n2
                    self.edtResult.setText(str(result))
                elif self.cboOperation.currentIndex() == 1:
                    result = n1 - n2
                    self.edtResult.setText(str(result))
                elif self.cboOperation.currentIndex() == 2:
                    result = n1 * n2
                    self.edtResult.setText(str(result))
                else:
                    result = n1 / n2
                    self.edtResult.setText(str(result))
            except:
                self.edtResult.setText("E")

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()

    currentForm.show()
    currentApp.exec_()