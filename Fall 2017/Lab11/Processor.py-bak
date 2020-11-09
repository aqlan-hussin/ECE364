#! /usr/local/bin/python3.4
import sys

from PySide.QtGui import *
from PySide.QtCore import *
from SteganographyGUI import *
from Steganography import *
from imageio import *
from functools import partial

import numpy as np

class Processor(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Processor, self).__init__(parent)
        self.fileName = ''
        self.hasPayload1 = False
        self.hasCarrier1 = False
        self.setupUi(self)
        self.chkApplyCompression.stateChanged.connect(self.compressionToggled)
        self.slideCompression.valueChanged.connect(self.compressionApplied)
        self.chkOverride.stateChanged.connect(self.overrideToggled)
        self.btnSave.clicked.connect(self.saveImage)
        self.btnClean.clicked.connect(self.cleanImage)
        self.btnExtract.clicked.connect(self.extractImage)

        self.viewPayload1.dragEnterEvent = partial(self.dragEnterImage,self.viewPayload1)
        self.viewPayload1.dragMoveEvent = partial(self.dragMoveImage,self.viewPayload1)
        self.viewPayload1.dropEvent = partial(self.dropImage,self.viewPayload1)

        self.viewCarrier1.dragEnterEvent = partial(self.dragEnterImage,self.viewCarrier1)
        self.viewCarrier1.dragMoveEvent = partial(self.dragMoveImage,self.viewCarrier1)
        self.viewCarrier1.dropEvent = partial(self.dropImage,self.viewCarrier1)

        self.viewCarrier2.dragEnterEvent = partial(self.dragEnterImage,self.viewCarrier2)
        self.viewCarrier2.dragMoveEvent = partial(self.dragMoveImage,self.viewCarrier2)
        self.viewCarrier2.dropEvent = partial(self.dropImage,self.viewCarrier2)

        self.setAcceptDrops(True)



    def dragEnterImage(self, view, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveImage(self, view, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dropImage(self, view, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            self.fileName = str(event.mimeData().urls()[0].toLocalFile())
            self.displayImage(view)
            self.handleWidgetsAfterDrop(view)
        else:
            event.ignore()
        self.enableSaveButton()

    def enableSaveButton(self):
        if self.hasPayload1 and self.hasCarrier1 and int(self.txtPayloadSize.text()) < int(self.txtCarrierSize.text()):
            if self.lblPayloadFound.text() == "":
                self.btnSave.setEnabled(True)
            elif self.chkOverride.isChecked():
                self.btnSave.setEnabled(True)
            else:
                self.btnSave.setEnabled(False)
        else:
            self.btnSave.setEnabled(False)

    def displayImage(self, view):
        pixmap = QtGui.QPixmap(self.fileName)
        pixmap = pixmap.scaled(355,275,QtCore.Qt.KeepAspectRatio)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        view.setScene(scene)
        view.show()
        if view == self.viewPayload1:
            self.hasPayload1 = True
        if view == self.viewCarrier1:
            self.hasCarrier1 = True

    def handleWidgetsAfterDrop(self, view):
        if view == self.viewPayload1:
            self.chkApplyCompression.setChecked(False)
            self.compressionToggled()
            self.txtCompression.setText("0")
            self.slideCompression.setValue(0)
        elif view == self.viewCarrier1:
            self.calculateCarrierSize()
        elif view == self.viewCarrier2:
            scene = QGraphicsScene()
            self.viewPayload2.setScene(scene)
            self.viewPayload2.show()
            img = imread(self.fileName)
            carrier = Carrier(img)
            self.carrierImg = img
            if carrier.payloadExists():
                self.lblCarrierEmpty.clear()
                self.btnClean.setEnabled(True)
                self.btnExtract.setEnabled(True)
            else:
                self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")
                self.btnClean.setDisabled(True)
                self.btnExtract.setDisabled(True)

    def compressionToggled(self):
        if self.chkApplyCompression.isChecked() == True:
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
            self.calculatePayloadSize(compressionLevel=self.slideCompression.value())
        else:
            self.slideCompression.setDisabled(True)
            self.txtCompression.setDisabled(True)
            self.calculatePayloadSize(compressionLevel=-1)
        if self.txtPayloadSize.text() != "0":
            self.hasPayload1 = True
        if self.txtCarrierSize.text() != "0":
            self.hasCarrier1 = True
        self.enableSaveButton()

    def calculatePayloadSize(self, compressionLevel):
        img = imread(self.fileName)
        self.payloadImg = img
        payload = Payload(img, compressionLevel)
        json = payload.json
        self.txtPayloadSize.setText(str(len(json)))

    def compressionApplied(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        self.calculatePayloadSize(compressionLevel=self.slideCompression.value())

    def overrideToggled(self):
        if self.hasPayload1 and self.hasCarrier1 and int(self.txtPayloadSize.text()) < int(self.txtCarrierSize.text()):
            if self.lblPayloadFound.text() == "":
                self.btnSave.setEnabled(True)
            elif self.chkOverride.isChecked():
                self.btnSave.setEnabled(True)
            else:
                self.btnSave.setEnabled(False)
        else:
            self.btnSave.setEnabled(False)

    def calculateCarrierSize(self):
        img = imread(self.fileName)
        self.carrierImg = img
        carrier = Carrier(img)
        carrier_size = carrier.img.shape[0] * carrier.img.shape[1] * 4
        self.txtCarrierSize.setText(str(carrier_size))
        if carrier.payloadExists():
            self.lblPayloadFound.setText(">>>> Payload Found <<<<")
            self.chkOverride.setEnabled(True)
        else:
            self.lblPayloadFound.clear()
            self.chkOverride.setDisabled(True)

    def saveImage(self):
        path = QFileDialog.getSaveFileName(self)
        payload = Payload(self.payloadImg,self.slideCompression.value())
        carrier = Carrier(self.carrierImg)
        newImg = carrier.embedPayload(payload,self.chkOverride.isChecked())
        imsave(path[0],newImg)

    def cleanImage(self):
        carrier = Carrier(self.carrierImg)
        cleaned = carrier.clean()
        imsave(self.fileName,cleaned)
        self.displayImage(self.viewCarrier2)
        self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")
        self.btnClean.setDisabled(True)
        self.btnExtract.setDisabled(True)

    def extractImage(self):
        carrier = Carrier(self.carrierImg)
        extracted = carrier.extractPayload()
        imsave("extracted.png",extracted.rawData)
        self.fileName = "extracted.png"
        self.displayImage(self.viewPayload2)
        self.btnExtract.setDisabled(True)


currentApp = QApplication(sys.argv)
currentForm = Processor()

currentForm.show()
currentApp.exec_()