import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *
import locale


class SimpleCalculator(QMainWindow, Ui_Calculator):

    locale.setlocale(locale.LC_ALL, "")

    def __init__(self, parent=None):
        super(SimpleCalculator, self).__init__(parent)
        self.setupUi(self)

        self.setupButtons()
        self.arg1 = None
        self.operator = None
        self.arg2Flag = False
        self.clearFlag = True
        self.clear()



    def setupButtons(self):
        self.num_btn = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4,
                        self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]

        self.btn0.clicked.connect(lambda: self.numberClicked(0))
        self.btn1.clicked.connect(lambda: self.numberClicked(1))
        self.btn2.clicked.connect(lambda: self.numberClicked(2))
        self.btn3.clicked.connect(lambda: self.numberClicked(3))
        self.btn4.clicked.connect(lambda: self.numberClicked(4))
        self.btn5.clicked.connect(lambda: self.numberClicked(5))
        self.btn6.clicked.connect(lambda: self.numberClicked(6))
        self.btn7.clicked.connect(lambda: self.numberClicked(7))
        self.btn8.clicked.connect(lambda: self.numberClicked(8))
        self.btn9.clicked.connect(lambda: self.numberClicked(9))

        self.btnPlus.clicked.connect(lambda: self.operatorClicked("+"))
        self.btnMinus.clicked.connect(lambda: self.operatorClicked("-"))
        self.btnMultiply.clicked.connect(lambda: self.operatorClicked("*"))
        self.btnDivide.clicked.connect(lambda: self.operatorClicked("/"))
        self.btnDot.clicked.connect(self.dotClicked)

        self.btnEqual.clicked.connect(self.equals)
        self.btnClear.clicked.connect(self.clear)

        self.cboDecimal.setCurrentIndex(2)

        self.cboDecimal.currentIndexChanged.connect(lambda: self.displayThis(float(self.txtDisplay.text().replace(',', ''))))

        self.chkSeparator.stateChanged.connect(lambda: self.displayThis(float(self.txtDisplay.text().replace(',', ''))))

    def equals(self):
        if(self.arg1 == None) :
            return

        arg2 = float(self.txtDisplay.text().replace(',', ''))
        result = self.evaluteMath(self.arg1, arg2, self.operator)
        self.displayThis(result)
        self.arg1 = None
        self.arg2Flag = True

    def clear(self):
        self.txtDisplay.setText("0")
        self.arg1 = None
        self.operator = None
        self.clearFlag = True

    def dotClicked(self):
        current_disp = self.txtDisplay.text().replace(',', '')

        if "." in current_disp :
            return
        self.clearFlag = False
        self.txtDisplay.setText(current_disp + ".")

    def operatorClicked(self, operator):
        current_disp = float(self.txtDisplay.text().replace(',', ''))
        if(current_disp == 0 and operator == "-") :
            self.txtDisplay.setText("-")
            return

        if(self.arg1 == None):
            self.arg1 = current_disp
            self.arg2Flag = True
            self.operator = operator
        else :
            result = self.evaluteMath(self.arg1, float(self.txtDisplay.text().replace(',', '')), self.operator)
            self.displayThis(result)
            self.arg1 = float(result)
            self.arg2Flag = True
            self.operator = operator

    def displayThis(self, displayMe):
        decimals = int(self.cboDecimal.currentText())

        if (self.chkSeparator.isChecked()):
            string = locale.format("%." + str(decimals) + "f", displayMe, grouping=True)
            self.txtDisplay.setText(string)
        else :
            string = locale.format("%." + str(decimals) + "f", displayMe, grouping=False)
            self.txtDisplay.setText(string)


    def evaluteMath(self, arg1, arg2, operator):
        if (operator == "+"):
            return arg1 + arg2

        if (operator == "-"):
            return arg1 - arg2

        if (operator == "*"):
            return arg1 * arg2

        if (operator == "/"):
            return arg1 / arg2


    def numberClicked(self, num):
        if(self.arg2Flag):
            self.txtDisplay.setText("0")
            self.arg2Flag = False

        current_val = self.txtDisplay.text().replace(',', '')
        if(current_val == "-") :
            self.txtDisplay.setText(current_val + str(num))
            return

        if self.clearFlag == True:
            self.txtDisplay.setText(str(num))
            self.clearFlag = False
            return

        if float(current_val) == 0 and "." not in current_val:
            if num == 0 :
                return
            if ("." in current_val):
                self.txtDisplay.setText("0." + str(num))
                return
            self.txtDisplay.setText(str(num))
            return
        self.txtDisplay.setText(str(current_val) + str(num))


def main() :
    currentApp = QApplication(sys.argv)
    currentForm = SimpleCalculator()

    currentForm.show()
    currentApp.exec_()


# Entry-point
if __name__ == "__main__":
    main()