from __future__ import annotations
from PyQt5.QtWidgets import QFrame, QPushButton, QWidget, \
    QTextEdit, QScrollArea, QLabel, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import QCoreApplication, QRect, Qt
from gui.scrollableProductComponent import ScrollPreviewComponent


class ProductManagerFrame(QFrame):
    def __init__(self, top):
        super().__init__(top.centralwidget)
        self.top = top
        self.setGeometry(QRect(760, 10, 330, 640))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.scrollArea = ScrollPreviewComponent(self)

        self.productBarcode = QTextEdit(self)
        self.productBarcode.setGeometry(QRect(10, 340, 310, 40))

        self.productDescription = QTextEdit(self)
        self.productDescription.setGeometry(QRect(10, 390, 310, 180))

        self.confirmButton = QPushButton(parent=self,text="Confirm")
        self.confirmButton.setGeometry(QRect(160, 580, 160, 50))

        self.cancelButton = QPushButton(parent=self,text="Cancel")
        self.cancelButton.setGeometry(QRect(10, 580, 140, 50))


    def setBarcode(self, text):
        self.productBarcode.setText(
            text
        )


    def getScrollArea(self) -> ScrollPreviewComponent:
        return self.scrollArea


    def setup(self):
        pass


    def cancelButtonClicked(self):
        pass


    def confirmButtonClicked(self):
        pass


    def setBarcode(self,barcode:str): self.productBarcode.setText(barcode)
    
    def setDescription(self,desc:str):  self.productDescription.setText(desc)


    def getAllData():
        pass

    def setNewData(data):


