import sys

from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.btnClear.clicked.connect(self.initialState)
        self.btnLoad.clicked.connect(self.loadData)
        self.btnSave.clicked.connect(self.saveData)

        self.cboCollege.currentIndexChanged.connect(self.dataEntered)
        self.chkGraduate.stateChanged.connect(self.dataEntered)

        self.txtStudentName.textChanged.connect(self.dataEntered)
        self.txtStudentID.textChanged.connect(self.dataEntered)

        self.txtComponentName_1.textChanged.connect(self.dataEntered)
        self.txtComponentName_2.textChanged.connect(self.dataEntered)
        self.txtComponentName_3.textChanged.connect(self.dataEntered)
        self.txtComponentName_4.textChanged.connect(self.dataEntered)
        self.txtComponentName_5.textChanged.connect(self.dataEntered)
        self.txtComponentName_6.textChanged.connect(self.dataEntered)
        self.txtComponentName_7.textChanged.connect(self.dataEntered)
        self.txtComponentName_8.textChanged.connect(self.dataEntered)
        self.txtComponentName_9.textChanged.connect(self.dataEntered)
        self.txtComponentName_10.textChanged.connect(self.dataEntered)
        self.txtComponentName_11.textChanged.connect(self.dataEntered)
        self.txtComponentName_12.textChanged.connect(self.dataEntered)
        self.txtComponentName_13.textChanged.connect(self.dataEntered)
        self.txtComponentName_14.textChanged.connect(self.dataEntered)
        self.txtComponentName_15.textChanged.connect(self.dataEntered)
        self.txtComponentName_16.textChanged.connect(self.dataEntered)
        self.txtComponentName_17.textChanged.connect(self.dataEntered)
        self.txtComponentName_18.textChanged.connect(self.dataEntered)
        self.txtComponentName_19.textChanged.connect(self.dataEntered)
        self.txtComponentName_20.textChanged.connect(self.dataEntered)

        self.txtComponentCount_1.textChanged.connect(self.dataEntered)
        self.txtComponentCount_2.textChanged.connect(self.dataEntered)
        self.txtComponentCount_3.textChanged.connect(self.dataEntered)
        self.txtComponentCount_4.textChanged.connect(self.dataEntered)
        self.txtComponentCount_5.textChanged.connect(self.dataEntered)
        self.txtComponentCount_6.textChanged.connect(self.dataEntered)
        self.txtComponentCount_7.textChanged.connect(self.dataEntered)
        self.txtComponentCount_8.textChanged.connect(self.dataEntered)
        self.txtComponentCount_9.textChanged.connect(self.dataEntered)
        self.txtComponentCount_10.textChanged.connect(self.dataEntered)
        self.txtComponentCount_11.textChanged.connect(self.dataEntered)
        self.txtComponentCount_12.textChanged.connect(self.dataEntered)
        self.txtComponentCount_13.textChanged.connect(self.dataEntered)
        self.txtComponentCount_14.textChanged.connect(self.dataEntered)
        self.txtComponentCount_15.textChanged.connect(self.dataEntered)
        self.txtComponentCount_16.textChanged.connect(self.dataEntered)
        self.txtComponentCount_17.textChanged.connect(self.dataEntered)
        self.txtComponentCount_18.textChanged.connect(self.dataEntered)
        self.txtComponentCount_19.textChanged.connect(self.dataEntered)
        self.txtComponentCount_20.textChanged.connect(self.dataEntered)

        self.initialState()

    def initialState(self):
        self.txtStudentID.setText("")
        self.txtStudentName.setText("")

        self.txtComponentCount_1.setText("")
        self.txtComponentCount_2.setText("")
        self.txtComponentCount_3.setText("")
        self.txtComponentCount_4.setText("")
        self.txtComponentCount_5.setText("")
        self.txtComponentCount_6.setText("")
        self.txtComponentCount_7.setText("")
        self.txtComponentCount_8.setText("")
        self.txtComponentCount_9.setText("")
        self.txtComponentCount_10.setText("")
        self.txtComponentCount_11.setText("")
        self.txtComponentCount_12.setText("")
        self.txtComponentCount_13.setText("")
        self.txtComponentCount_14.setText("")
        self.txtComponentCount_15.setText("")
        self.txtComponentCount_16.setText("")
        self.txtComponentCount_17.setText("")
        self.txtComponentCount_18.setText("")
        self.txtComponentCount_19.setText("")
        self.txtComponentCount_20.setText("")

        self.txtComponentName_1.setText("")
        self.txtComponentName_2.setText("")
        self.txtComponentName_3.setText("")
        self.txtComponentName_4.setText("")
        self.txtComponentName_5.setText("")
        self.txtComponentName_6.setText("")
        self.txtComponentName_7.setText("")
        self.txtComponentName_8.setText("")
        self.txtComponentName_9.setText("")
        self.txtComponentName_10.setText("")
        self.txtComponentName_11.setText("")
        self.txtComponentName_12.setText("")
        self.txtComponentName_13.setText("")
        self.txtComponentName_14.setText("")
        self.txtComponentName_15.setText("")
        self.txtComponentName_16.setText("")
        self.txtComponentName_17.setText("")
        self.txtComponentName_18.setText("")
        self.txtComponentName_19.setText("")
        self.txtComponentName_20.setText("")

        self.cboCollege.setCurrentIndex(0)
        self.chkGraduate.setChecked(False)
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)

    def dataEntered(self):
        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)

    def saveData(self):
        fileName = "target.xml"

        listCN = [self.txtComponentName_1,
                  self.txtComponentName_2,
                  self.txtComponentName_3,
                  self.txtComponentName_4,
                  self.txtComponentName_5,
                  self.txtComponentName_6,
                  self.txtComponentName_7,
                  self.txtComponentName_8,
                  self.txtComponentName_9,
                  self.txtComponentName_10,
                  self.txtComponentName_11,
                  self.txtComponentName_12,
                  self.txtComponentName_13,
                  self.txtComponentName_14,
                  self.txtComponentName_15,
                  self.txtComponentName_16,
                  self.txtComponentName_17,
                  self.txtComponentName_18,
                  self.txtComponentName_19,
                  self.txtComponentName_20]

        listCC = [self.txtComponentCount_1,
                  self.txtComponentCount_2,
                  self.txtComponentCount_3,
                  self.txtComponentCount_4,
                  self.txtComponentCount_5,
                  self.txtComponentCount_6,
                  self.txtComponentCount_7,
                  self.txtComponentCount_8,
                  self.txtComponentCount_9,
                  self.txtComponentCount_10,
                  self.txtComponentCount_11,
                  self.txtComponentCount_12,
                  self.txtComponentCount_13,
                  self.txtComponentCount_14,
                  self.txtComponentCount_15,
                  self.txtComponentCount_16,
                  self.txtComponentCount_17,
                  self.txtComponentCount_18,
                  self.txtComponentCount_19,
                  self.txtComponentCount_20]

        i = 0
        if self.chkGraduate.isChecked() == True:
            grad = "true"
        else:
            grad = "false"

        with open(fileName, 'w') as file1:
            file1.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            file1.write("<Content>\n")
            file1.write("    <StudentName graduate=\"{0}\">{1}</StudentName>\n".format(grad,self.txtStudentName.text()))
            file1.write("    <StudentID>{0}</StudentID>\n".format(self.txtStudentID.text()))
            file1.write("    <College>{0}</College>\n".format(self.cboCollege.currentText()))
            file1.write("    <Components>\n")
            while i < 20:
                if listCN[i].text() != "":
                    file1.write("        <Component name=\"{0}\" count=\"{1}\" />\n".format(listCN[i].text(),listCC[i].text()))
                i += 1
            file1.write("    </Components>\n")
            file1.write("</Content>")

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        listCN = [self.txtComponentName_1,
                  self.txtComponentName_2,
                  self.txtComponentName_3,
                  self.txtComponentName_4,
                  self.txtComponentName_5,
                  self.txtComponentName_6,
                  self.txtComponentName_7,
                  self.txtComponentName_8,
                  self.txtComponentName_9,
                  self.txtComponentName_10,
                  self.txtComponentName_11,
                  self.txtComponentName_12,
                  self.txtComponentName_13,
                  self.txtComponentName_14,
                  self.txtComponentName_15,
                  self.txtComponentName_16,
                  self.txtComponentName_17,
                  self.txtComponentName_18,
                  self.txtComponentName_19,
                  self.txtComponentName_20]

        listCC = [self.txtComponentCount_1,
                  self.txtComponentCount_2,
                  self.txtComponentCount_3,
                  self.txtComponentCount_4,
                  self.txtComponentCount_5,
                  self.txtComponentCount_6,
                  self.txtComponentCount_7,
                  self.txtComponentCount_8,
                  self.txtComponentCount_9,
                  self.txtComponentCount_10,
                  self.txtComponentCount_11,
                  self.txtComponentCount_12,
                  self.txtComponentCount_13,
                  self.txtComponentCount_14,
                  self.txtComponentCount_15,
                  self.txtComponentCount_16,
                  self.txtComponentCount_17,
                  self.txtComponentCount_18,
                  self.txtComponentCount_19,
                  self.txtComponentCount_20]

        with open(filePath, 'r') as file1:
            lines = file1.readlines()

        i = 0
        j = 0

        for items in lines:
            if i == 2:
                words = items.split("\"")
                grad = words[1]
                if grad == "true":
                    self.chkGraduate.setChecked(True)
                else:
                    self.chkGraduate.setChecked(False)
                name = items.split(">")
                name2 = name[1].split("<")
                self.txtStudentName.setText(name2[0])
            elif i == 3:
                words = items.split(">")
                SID = words[1].split("<")
                self.txtStudentID.setText(SID[0])
            elif i == 4:
                words = items.split(">")
                college = words[1].split("<")
                if college[0] == "Aerospace Engineering":
                    self.cboCollege.setCurrentIndex(1)
                elif college[0] == "Civil Engineering":
                    self.cboCollege.setCurrentIndex(2)
                elif college[0] == "Computer Engineering":
                    self.cboCollege.setCurrentIndex(3)
                elif college[0] == "Electrical Engineering":
                    self.cboCollege.setCurrentIndex(4)
                elif college[0] == "Industrial Engineering":
                    self.cboCollege.setCurrentIndex(5)
                elif college[0] == "Mechanical Engineering":
                    self.cboCollege.setCurrentIndex(6)
                else:
                    self.cboCollege.setCurrentIndex(0)
            elif i == 0 or i == 1 or i == 5 or i == len(lines)-2 or i == len(lines)-1 or i >= 26:
                x = 0
            else:
                words = items.split("\"")
                listCN[j].setText(words[1])
                listCC[j].setText(words[3])
                j += 1

            i += 1

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
