import sys
from functools import partial
from os.path import splitext
from SteganographyGUI import *
from PySide.QtCore import *
from PySide.QtGui import *
from Steganography import *
import scipy.misc
import numpy as np

class SteganographyConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(SteganographyConsumer, self).__init__(parent)
        self.payload_file = ''
        self.carrier_file = ''
        self.payload_flag = 0
        self.carrier_flag = 0
        self.payload_array = 0
        self.carrier_array = 0
        self.compression = -1
        self.setupUi(self)
        self.chkApplyCompression.stateChanged.connect(lambda :self.compression_changed())
        self.slideCompression.valueChanged.connect(lambda:self.slider_moved())
        self.chkOverride.stateChanged.connect(lambda:self.override_chkd())
        self.btnSave.clicked.connect(lambda:self.save())
        self.btnClean.clicked.connect(lambda:self.clean())
        self.btnExtract.clicked.connect(lambda:self.extract())

        views = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]
        accept = lambda e: e.accept()

        for view in views:
            view.dragEnterEvent = accept
            view.dragMoveEvent = accept
            view.dragLeaveEvent = accept

            view.dropEvent = partial(self.processDrop, view)


    def clean(self):
        payload = scipy.misc.imread(self.filePath)
        carrier = Carrier(payload)
        cleaned_image = carrier.clean()
        scipy.misc.imsave("cleaned.png",cleaned_image)
        self.display_image(self.viewCarrier2,'cleaned.png')
        self.btnExtract.setDisabled(True)
        self.btnClean.setDisabled(True)
        self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")

    def extract(self):
        payload = scipy.misc.imread(self.filePath)
        carrier = Carrier(payload)
        pload = carrier.extractPayload()
        scipy.misc.imsave("extracted.png",pload.img)
        self.display_image(self.viewPayload2,'extracted.png')

    def override_chkd(self):
        if self.chkOverride.isChecked() and self.txtPayloadSize.text() != '0':
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setDisabled(True)

    def save(self):
        if self.chkOverride.isChecked():
            override = True
        else:
            override = False

        filePath, _ = QFileDialog.getSaveFileName(self, caption='Embed Payload into Carrier', filter="PNG files (*.png)")

        payload = Payload(self.payload_array,compressionLevel=self.compression)
        carrier = Carrier(self.carrier_array)
        image = carrier.embedPayload(payload,override)

        scipy.misc.imsave(filePath,image)

    def compression_changed(self):
        if self.chkApplyCompression.isChecked():
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
            self.setSize(self.txtPayloadSize,self.payload_file,compression=self.slideCompression.value())
        else:
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)
            self.setSize(self.txtPayloadSize,self.payload_file,compression=-1)


    def slider_moved(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        self.setSize(self.txtPayloadSize,self.payload_file,compression=self.slideCompression.value())
        self.compression = self.slideCompression.value()

    def display_image(self,view,filePath):
        frame = QGraphicsScene()
        img = QPixmap(filePath)
        img = img.scaled(355,280, Qt.KeepAspectRatio)
        frame.addPixmap(img)
        view.setScene(frame)
        view.show()


    def setSize(self,item,filePath,compression =-1):
        img = scipy.misc.imread(filePath)
        payload = Payload(img,compression)
        if item == self.txtCarrierSize:
            item.setText(str(payload.size/8))
        else:
            item.setText(str(payload.size))


    def processDrop(self, view, e):

        mime = e.mimeData()

        if not mime.hasUrls():
            return

        filePath = mime.urls()[0].toLocalFile()
        _, ext = splitext(filePath)

        if not ext == ".png":
            return

        self.filePath = filePath
        self.display_image(view,filePath)

        if view == self.viewPayload1:
            self.payload_file = filePath
            item = self.txtPayloadSize
            payload = scipy.misc.imread(self.payload_file)
            self.setSize(item,self.payload_file)
            self.chkApplyCompression.setChecked(False)
            self.slideCompression.setValue(0)
            self.slideCompression.setDisabled(True)
            self.txtCompression.setText('0')
            self.txtCompression.setDisabled(True)
            self.payload_flag = 1
            self.payload_array = payload

        elif view == self.viewCarrier1:
            self.carrier_file = filePath
            item = self.txtCarrierSize
            self.setSize(item,self.carrier_file)
            payload = scipy.misc.imread(self.carrier_file)
            carrier = Carrier(payload)
            if carrier.payloadExists():
                self.lblPayloadFound.setText(">>>> Payload Found <<<<")
                self.chkOverride.setEnabled(True)
            else:
                self.lblPayloadFound.clear()
                self.chkOverride.setEnabled(False)
            self.carrier_flag = 1
            self.carrier_array = payload

        else:
            payload = scipy.misc.imread(filePath)
            carrier = Carrier(payload)
            if not carrier.payloadExists():
                self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")
                self.btnExtract.setDisabled(True)
                self.btnClean.setDisabled(True)
            else:
                self.lblCarrierEmpty.clear()
                self.btnExtract.setDisabled(False)
                self.btnClean.setDisabled(False)

        if self.carrier_flag == 1 and self.payload_flag == 1:
            carrier_size = int(self.txtCarrierSize.text())
            payload_size = int(self.txtPayloadSize.text())
            if self.lblPayloadFound.text() == "" or self.chkOverride.isChecked() == True and carrier_size >= payload_size and self.txtPayloadSize.text() != '0':
                self.btnSave.setEnabled(True)
            else:
                self.btnSave.setEnabled(False)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = SteganographyConsumer()
    currentForm.show()
    currentApp.exec_()