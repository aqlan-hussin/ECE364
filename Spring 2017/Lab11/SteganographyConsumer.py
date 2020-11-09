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
        self.pload_filepath = ''
        self.carr_filepath = ''
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
        pload_img = scipy.misc.imread(self.filePath)
        carrier = Carrier(pload_img)
        cleaned_image = carrier.clean()
        scipy.misc.imsave("cleaned.png",cleaned_image)
        self.display_image(self.viewCarrier2,'cleaned.png')
        self.btnExtract.setDisabled(True)
        self.btnClean.setDisabled(True)
        self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")

    def extract(self):
        pload_img = scipy.misc.imread(self.filePath)
        carrier = Carrier(pload_img)
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
            self.setPloadSize(self.txtPayloadSize,self.pload_filepath,compression=self.slideCompression.value())
        else:
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)
            self.setPloadSize(self.txtPayloadSize,self.pload_filepath,compression=-1)


    def slider_moved(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        self.setPloadSize(self.txtPayloadSize,self.pload_filepath,compression=self.slideCompression.value())
        self.compression = self.slideCompression.value()

    def display_image(self,view,filePath):
        frame = QGraphicsScene()
        img = QPixmap(filePath)
        img = img.scaled(355,280, Qt.KeepAspectRatio)
        frame.addPixmap(img)
        view.setScene(frame)
        view.show()


    def setPloadSize(self,item,filePath,compression =-1):
        pload_img = scipy.misc.imread(filePath)
        pload = Payload(pload_img,compression)
        pload_xml = pload.xml
        if item == self.txtCarrierSize:
            item.setText(str(int(len(pload_xml)/8)))
        else:
            item.setText(str(len(pload_xml)))



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
            self.pload_filepath = filePath
            item = self.txtPayloadSize
            pload_img = scipy.misc.imread(self.pload_filepath)
            self.setPloadSize(item,self.pload_filepath)
            self.chkApplyCompression.setChecked(False)
            self.slideCompression.setValue(0)
            self.slideCompression.setDisabled(True)
            self.txtCompression.setText('0')
            self.txtCompression.setDisabled(True)
            self.payload_flag = 1
            self.payload_array = pload_img

        elif view == self.viewCarrier1:
            self.carr_filepath = filePath
            item = self.txtCarrierSize
            self.setPloadSize(item,self.carr_filepath)
            pload_img = scipy.misc.imread(self.carr_filepath)
            carrier = Carrier(pload_img)
            if carrier.payloadExists():
                self.lblPayloadFound.setText(">>>> Payload Found <<<<")
                self.chkOverride.setEnabled(True)
            else:
                self.lblPayloadFound.clear()
                self.chkOverride.setEnabled(False)
            self.carrier_flag = 1
            self.carrier_array = pload_img

        else:
            pload_img = scipy.misc.imread(filePath)
            carrier = Carrier(pload_img)
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