# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created: Tue Apr 12 14:31:51 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import pickle
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QLabel, QMessageBox, QPixmap
import popsift
import sys, time
import cv2

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class ExtendedQLabel(QtGui.QLabel):
    def __init(self, parent):
        QLabel.__init__(self, parent)

    def mouseReleaseEvent(self, ev):
        self.emit(QtCore.SIGNAL('clicked()'))


class Ui_MainWindow(QtGui.QMainWindow):
    BUTTON_IMAGE = 'im.png'

    def __init__(self, *args):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.connect(self.ImageButton, QtCore.SIGNAL('clicked()'), self.buttonClicked)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(563, 554)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Kinnari"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QtCore.QSize(600, 450))
        self.widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ImageButton = ExtendedQLabel(self.widget)
        # self.ImageButton.move(0, 0)
        self.pix1 = QtGui.QPixmap(self.BUTTON_IMAGE)
        self.ImageButton.setPixmap(self.pix1)
        # self.ImageButton.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.ImageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ImageButton.setText(_fromUtf8(""))
        self.ImageButton.setObjectName(_fromUtf8("ImageButton"))
        self.ImageButton.setScaledContents(True)
        # sift=cv2.xfeatures2d.SIFT_create()
        self.gridLayout.addWidget(self.ImageButton, 0, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.widget)
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monotype Corsiva"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.verticalLayout.addWidget(self.label_2)
        '''self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.pushButton = QtGui.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(200, 0, 150, 31))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.annotate)
        self.verticalLayout.addWidget(self.widget_2)'''
        self.pushButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalLayout.addWidget(self.pushButton, QtCore.Qt.AlignHCenter)
        self.pushButton.clicked.connect(self.annotate)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Automatic Image Anotation", None))
        self.pushButton.setText(_translate("MainWindow", "Anotate Image", None))

    def buttonClicked(self):
        self.label_2.setText("")
        self.progressBar.setProperty("value", 0)
        self.file_name = QtGui.QFileDialog.getOpenFileName(self, "Pick a folder")
        self.pix = QPixmap(self.file_name)
        if not self.pix.isNull():
            self.ImageButton.setPixmap(self.pix)
            self.flag = 1

        else:
            self.ImageButton.setPixmap(QtGui.QPixmap(self.BUTTON_IMAGE))
            mBox = QMessageBox()
            mBox.setText("Not a Valid Image or Image Not Selected!")
            mBox.setWindowTitle("ERROR")
            mBox.setStandardButtons(QMessageBox.Ok)
            mBox.exec_()

    def annotate(self):
        self.val = 0.0
        userdes = popsift.computeKp(str(self.file_name))
        f = open('monuments.pkl', 'rb')
        tup = pickle.load(f)

        maxp = -1
        completed = 0
        prev = time.time()
        while (tup):
            self.val = self.val + float(100)/29
            self.progressBar.setProperty("value", self.val)
            print tup[1]
            c = popsift.compare(userdes, tup[0], 0)
            print time.ctime()

            if c > 0:
                if maxp < c:
                    maxp = c
                    self.qpath = tup[1]

            try:
                tup = pickle.load(f)
            except:
                if maxp != -1:
                    print self.qpath
                    ind = self.qpath.rfind("/")
                    ind2 = -1
                    for i in ['1', '2', '3', '4', '5']:
                        ind2 = max(self.qpath.find(i), ind2)
                    self.label_2.setText("The image is of : " + self.qpath[ind + 1:ind2])
                else:
                    self.label_2.setText("Sorry !No matches found")
                break
        now = time.time()
        print "Total time elapsed :", now - prev


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
