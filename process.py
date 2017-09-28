
import sys
from PySide import QtGui
from PySide import QtCore
from PIL import Image
from random import randint

class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):

        print("Initializing")

        filePick = QtGui.QHBoxLayout()

        self.fileLabel = QtGui.QLabel('No file selected')
        filePick.addWidget(self.fileLabel)
        fileBtn = QtGui.QPushButton('Choose file', self)
        filePick.addWidget(fileBtn)

        self.connect(fileBtn, QtCore.SIGNAL('clicked()'), self.get_fname)
        pixmap = QtGui.QPixmap()
        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setPixmap(pixmap)
        self.imageString = ""
        self.sliderValue = 0

        bottomBox = QtGui.QHBoxLayout()
        topBox = QtGui.QHBoxLayout()
        sideBox = QtGui.QVBoxLayout()
        sideBoxPad = QtGui.QHBoxLayout()
        topBox.addStretch(1)
        topBox.addLayout(filePick)
        topBox.addStretch(1)
        bottomBox.addStretch(1)
        bottomBox.addWidget(self.imageLabel)
        bottomBox.addStretch(1)

        normalButton = QtGui.QPushButton("Normal")
        self.connect(normalButton, QtCore.SIGNAL('clicked()'), self.normal_image)
        saveButton = QtGui.QPushButton("Save")
        self.connect(saveButton, QtCore.SIGNAL('clicked()'), self.normal_image)
        addButton = QtGui.QPushButton("Add")
        self.connect(addButton, QtCore.SIGNAL('clicked()'), self.add)
        blurButton = QtGui.QPushButton("Blur")
        self.connect(blurButton, QtCore.SIGNAL('clicked()'), self.blur)
        contrastButton = QtGui.QPushButton("Contrast")
        self.connect(contrastButton, QtCore.SIGNAL('clicked()'), self.contrast)
        edgeDetectButton = QtGui.QPushButton("Edge Detect")
        self.connect(edgeDetectButton, QtCore.SIGNAL('clicked()'), self.edge_detect)
        invertButton = QtGui.QPushButton("Invert")
        self.connect(invertButton, QtCore.SIGNAL('clicked()'), self.invert)
        multiplyButton = QtGui.QPushButton("Multiply")
        self.connect(multiplyButton, QtCore.SIGNAL('clicked()'), self.multiply)
        sharpenButton = QtGui.QPushButton("Sharpen")
        self.connect(sharpenButton, QtCore.SIGNAL('clicked()'), self.sharpen)
        twoToneButton = QtGui.QPushButton("Two Tone")
        self.connect(twoToneButton, QtCore.SIGNAL('clicked()'), self.two_tone)

        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 50)
        sld.valueChanged[int].connect(self.change_slider)

        sideBox.addStretch(1)
        sideBox.addWidget(normalButton)
        sideBox.addStretch(1)
#        sideBox.addWidget(saveButton)
        sideBox.addWidget(addButton)
        sideBox.addWidget(blurButton)
        sideBox.addWidget(contrastButton)
        sideBox.addWidget(edgeDetectButton)
        sideBox.addWidget(invertButton)
        sideBox.addWidget(multiplyButton)
        sideBox.addWidget(sharpenButton)
        sideBox.addWidget(twoToneButton)
        sideBox.addWidget(sld)
        sideBox.addStretch(1)
        sideBoxPad.addStretch(1)
        sideBoxPad.addLayout(sideBox)
        sideBoxPad.addStretch(1)

        grid = QtGui.QGridLayout()
        grid.addLayout(topBox, 0, 1)
        grid.addLayout(sideBoxPad, 1, 0)
        grid.addLayout(bottomBox, 1, 1)
        self.setLayout(grid)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Image Processing Functions')

        self.show()

    def get_fname(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Select file')
        print(fname)
        if fname:
            self.fileLabel.setText(fname[0])
            self.load_image(fname[0])
        else:
            self.fileLabel.setText("No file selected")


    def load_image(self, filepath):

        print("Loading Image")
        pixmap = QtGui.QPixmap(filepath)
        self.imageLabel.setPixmap(pixmap)
        self.imageString = filepath


    def set_image(self, image):

        self.imageLabel.setPixmap(image)


    def normal_image(self):

        print("Loading Image")
        pixmap = QtGui.QPixmap(self.imageString)
        self.imageLabel.setPixmap(pixmap)


    def change_slider(self, value):
        self.sliderValue = value

    def add(self):
        print(self.imageString)
        if self.imageString:
            print("Processing")
            img = Image.open(self.imageString)
            im=Image.new('RGBA', img.size)
            im.paste(img)
            imdata = im.tobytes()
            imWidth = im.size[0]
            imHeight = im.size[1]

            newqim = QtGui.QImage(imWidth, imHeight, QtGui.QImage.Format_ARGB32)
            for xstep in range(0,imWidth):
                for ystep in range(0,imHeight):

                    pixelValueTuple = im.getpixel((xstep,ystep))
                    pixelR = pixelValueTuple[0]
                    pixelG = pixelValueTuple[1]
                    pixelB = pixelValueTuple[2]

                    addValue = self.sliderValue
                    pixelR += addValue
                    pixelG += addValue
                    pixelB += addValue

                    if pixelR > 255:
                        pixelR = 255
                    if pixelG > 255:
                        pixelG = 255
                    if pixelB > 255:
                        pixelB = 255

                    if pixelR < 0:
                        pixelR = 0
                    if pixelG < 0:
                        pixelG = 0
                    if pixelB < 0:
                        pixelB = 0

                    copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)

                    newqim.setPixel(xstep, ystep, copiedValue)


            pix = QtGui.QPixmap.fromImage(newqim)
            self.set_image(pix)

    def blur(self):
        if self.imageString:
            print("Processing")
            img = Image.open(self.imageString)
            im=Image.new('RGBA', img.size)
            im.paste(img)
            imdata = im.tobytes()
            imWidth = im.size[0]
            imHeight = im.size[1]

            newqim = QtGui.QImage(imWidth, imHeight, QtGui.QImage.Format_ARGB32)
            for xstep in range(0,imWidth):
                for ystep in range(0,imHeight):

                    pixelValueTuple = im.getpixel((xstep,ystep))
                    pixelR = pixelValueTuple[0]
                    pixelG = pixelValueTuple[1]
                    pixelB = pixelValueTuple[2]

                    averageR = 0
                    averageG = 0
                    averageB = 0

                    for i in range(-1,2):
                        for j in range(-1,2):
                            if(xstep > 0 and xstep < imWidth-1):
                                if(ystep > 0 and ystep < imHeight-1):
                                    offsetpixel = im.getpixel((xstep+i,ystep+j))
                                    averageR += (offsetpixel[0]*.11111)
                                    averageG += (offsetpixel[1]*.11111)
                                    averageB += (offsetpixel[2]*.11111)

                    pixelR = averageR
                    pixelG = averageG
                    pixelB = averageB

                    if pixelR > 255:
                        pixelR = 255
                    if pixelG > 255:
                        pixelG = 255
                    if pixelB > 255:
                        pixelB = 255

                    if pixelR < 0:
                        pixelR = 0
                    if pixelG < 0:
                        pixelG = 0
                    if pixelB < 0:
                        pixelB = 0

                    copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)

                    newqim.setPixel(xstep, ystep, copiedValue)

            pix = QtGui.QPixmap.fromImage(newqim)
            self.set_image(pix)

    def contrast(self):
        print(self.imageString)
        if self.imageString:
            print("Processing")
            img = Image.open(self.imageString)
            im=Image.new('RGBA', img.size)
            im.paste(img)
            imdata = im.tobytes()
            imWidth = im.size[0]
            imHeight = im.size[1]

            factor = (self.sliderValue*2.0)/100.0

            newqim = QtGui.QImage(imWidth, imHeight, QtGui.QImage.Format_ARGB32)
            for xstep in range(0,imWidth):
                for ystep in range(0,imHeight):

                    pixelValueTuple = im.getpixel((xstep,ystep))
                    pixelR = pixelValueTuple[0]
                    pixelG = pixelValueTuple[1]
                    pixelB = pixelValueTuple[2]

                    pixelR = (factor * (pixelR - 128)) + 128
                    pixelG = (factor * (pixelG - 128)) + 128
                    pixelB = (factor * (pixelB - 128)) + 128

                    if pixelR > 255:
                        pixelR = 255
                    if pixelG > 255:
                        pixelG = 255
                    if pixelB > 255:
                        pixelB = 255

                    if pixelR < 0:
                        pixelR = 0
                    if pixelG < 0:
                        pixelG = 0
                    if pixelB < 0:
                        pixelB = 0

                    copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)

                    newqim.setPixel(xstep, ystep, copiedValue)

            pix = QtGui.QPixmap.fromImage(newqim)
            self.set_image(pix)

    def edge_detect(self):
        if self.imageString:
            print("Processing")
            img = Image.open(self.imageString)
            im=Image.new('RGBA', img.size)
            im.paste(img)
            imdata = im.tobytes()
            imWidth = im.size[0]
            imHeight = im.size[1]

            newqim = QtGui.QImage(imWidth, imHeight, QtGui.QImage.Format_ARGB32)
            for xstep in range(0,imWidth):
                for ystep in range(0,imHeight):

                    pixelValueTuple = im.getpixel((xstep,ystep))
                    pixelR = pixelValueTuple[0]
                    pixelG = pixelValueTuple[1]
                    pixelB = pixelValueTuple[2]

                    averageR = pixelR*9
                    averageG = pixelG*9
                    averageB = pixelB*9

                    for i in range(-1,2):
                        for j in range(-1,2):
                            if(xstep > 0 and xstep < imWidth-1):
                               if(ystep > 0 and ystep < imHeight-1):
                                   offsetpixel = im.getpixel((xstep+i,ystep+j))
                                   averageR += (offsetpixel[0]*-1)
                                   averageG += (offsetpixel[1]*-1)
                                   averageB += (offsetpixel[2]*-1)

                    pixelR = averageR
                    pixelG = averageG
                    pixelB = averageB

                    if pixelR > 255:
                        pixelR = 255
                    if pixelG > 255:
                        pixelG = 255
                    if pixelB > 255:
                        pixelB = 255

                    if pixelR < 0:
                        pixelR = 0
                    if pixelG < 0:
                        pixelG = 0
                    if pixelB < 0:
                        pixelB = 0

                    copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)

                    newqim.setPixel(xstep, ystep, copiedValue)

            pix = QtGui.QPixmap.fromImage(newqim)
            self.set_image(pix)

    def invert(self):
        if self.imageString:
            print("Processing")
            img = Image.open(self.imageString)
            im=Image.new('RGBA', img.size)
            im.paste(img)
            imdata = im.tobytes()
            imWidth = im.size[0]
            imHeight = im.size[1]

            newqim = QtGui.QImage(imWidth, imHeight, QtGui.QImage.Format_ARGB32)
            for xstep in range(0,imWidth):
                for ystep in range(0,imHeight):

                    pixelValueTuple = im.getpixel((xstep,ystep))
                    pixelR = pixelValueTuple[0]
                    pixelG = pixelValueTuple[1]
                    pixelB = pixelValueTuple[2]

                    pixelR = 255-pixelR
                    pixelG = 255-pixelG
                    pixelB = 255-pixelB

                    if pixelR > 255:
                        pixelR = 255
                    if pixelG > 255:
                        pixelG = 255
                    if pixelB > 255:
                        pixelB = 255

                    if pixelR < 0:
                        pixelR = 0
                    if pixelG < 0:
                        pixelG = 0
                    if pixelB < 0:
                        pixelB = 0

                    copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)
                    newqim.setPixel(xstep, ystep, copiedValue)

            pix = QtGui.QPixmap.fromImage(newqim)
            self.set_image(pix)

    def multiply(self):
        if self.imageString:
            print("Processing")
            img = Image.open(self.imageString)
            im=Image.new('RGBA', img.size)
            im.paste(img)
            imdata = im.tobytes()
            imWidth = im.size[0]
            imHeight = im.size[1]

            multValue = (self.sliderValue*2.0)/100.0

            newqim = QtGui.QImage(imWidth, imHeight, QtGui.QImage.Format_ARGB32)
            for xstep in range(0,imWidth):
                for ystep in range(0,imHeight):

                    pixelValueTuple = im.getpixel((xstep,ystep))
                    pixelR = pixelValueTuple[0]
                    pixelG = pixelValueTuple[1]
                    pixelB = pixelValueTuple[2]

                    pixelR *= multValue
                    pixelG *= multValue
                    pixelB *= multValue

                    if pixelR > 255:
                        pixelR = 255
                    if pixelG > 255:
                        pixelG = 255
                    if pixelB > 255:
                        pixelB = 255

                    if pixelR < 0:
                        pixelR = 0
                    if pixelG < 0:
                        pixelG = 0
                    if pixelB < 0:
                        pixelB = 0

                    copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)

                    newqim.setPixel(xstep, ystep, copiedValue)

            pix = QtGui.QPixmap.fromImage(newqim)
            self.set_image(pix)

    def sharpen(self):
        if self.imageString:
            print("Processing")
            img = Image.open(self.imageString)
            im=Image.new('RGBA', img.size)
            im.paste(img)
            imdata = im.tobytes()
            imWidth = im.size[0]
            imHeight = im.size[1]

            newqim = QtGui.QImage(imWidth, imHeight, QtGui.QImage.Format_ARGB32)
            for xstep in range(0,imWidth):
                for ystep in range(0,imHeight):

                    pixelValueTuple = im.getpixel((xstep,ystep))
                    pixelR = pixelValueTuple[0]
                    pixelG = pixelValueTuple[1]
                    pixelB = pixelValueTuple[2]

                    averageR = pixelR*10
                    averageG = pixelG*10
                    averageB = pixelB*10
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if(xstep > 0 and xstep < imWidth-1):
                               if(ystep > 0 and ystep < imHeight-1):
                                  offsetpixel = im.getpixel((xstep+i,ystep+j))
                                  averageR += (offsetpixel[0]*-1)
                                  averageG += (offsetpixel[1]*-1)
                                  averageB += (offsetpixel[2]*-1)

                    pixelR = averageR
                    pixelG = averageG
                    pixelB = averageB

                    if pixelR > 255:
                        pixelR = 255
                    if pixelG > 255:
                        pixelG = 255
                    if pixelB > 255:
                        pixelB = 255

                    if pixelR < 0:
                        pixelR = 0
                    if pixelG < 0:
                        pixelG = 0
                    if pixelB < 0:
                        pixelB = 0

                    copiedValue = QtGui.qRgb(pixelR, pixelG, pixelB)

                    newqim.setPixel(xstep, ystep, copiedValue)

            pix = QtGui.QPixmap.fromImage(newqim)
            self.set_image(pix)

    def two_tone(self):
        if self.imageString:
            print("Processing")
            img = Image.open(self.imageString)
            im=Image.new('RGBA', img.size)
            im.paste(img)
            imdata = im.tobytes()
            imWidth = im.size[0]
            imHeight = im.size[1]

            cutoffValue = self.sliderValue*2.55

            newqim = QtGui.QImage(imWidth, imHeight, QtGui.QImage.Format_ARGB32)
            for xstep in range(0,imWidth):
                for ystep in range(0,imHeight):

                    pixelValueTuple = im.getpixel((xstep,ystep))
                    pixelR = pixelValueTuple[0]
                    pixelG = pixelValueTuple[1]
                    pixelB = pixelValueTuple[2]

                    grayPixel = (pixelR*.21) + (pixelG*.71) + (pixelB*.07)

                    if(grayPixel > cutoffValue):
                        grayPixel = 255
                    else:
                        grayPixel = 1

                    if grayPixel > 255:
                        grayPixel = 255
                    if grayPixel < 0:
                        grayPixel = 0

                    copiedValue = QtGui.qRgb(grayPixel, grayPixel, grayPixel)

                    newqim.setPixel(xstep, ystep, copiedValue)

            pix = QtGui.QPixmap.fromImage(newqim)
            self.set_image(pix)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

main()
