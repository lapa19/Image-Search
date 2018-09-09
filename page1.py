import os
import sys
from PyQt4 import QtCore, QtGui
import sift
from PyQt4.QtGui import QPixmap,QLabel,QMessageBox, QApplication
from PySide.QtGui import QLayout
import page2,time
from page2 import Ui_MainWindow

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

'''class ExampleApp(QtGui.QMainWindow, page2.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)'''

class MainUI(QtGui.QMainWindow):
    BUTTON_IMAGE = 'im.png'

    def __init__(self, *args):
        QtGui.QMainWindow.__init__(self)
        self.pix=None
	self.flag=0
        self.resize(350, 140)
        self.initButton(self)
        self.connect(self.ImageButton, QtCore.SIGNAL('clicked()'), self.buttonClicked)
        #self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.proceed)

    def initButton(self,MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(550, 600)
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
        self.widget.setMinimumSize(QtCore.QSize(800,450))
        self.widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        #self.label_3 = ExtendedQLabel(self.widget)
        self.ImageButton = ExtendedQLabel(self.widget)
        #self.ImageButton.move(0, 0)
        self.ImageButton.setPixmap(QtGui.QPixmap(self.BUTTON_IMAGE))
        #self.ImageButton.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        self.ImageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ImageButton.setText(_fromUtf8(""))
        self.ImageButton.setObjectName(_fromUtf8("ImageButton"))
        self.ImageButton.setScaledContents(True)

        self.verticalLayout.addWidget(self.widget)
        self.gridLayout.addWidget(self.ImageButton, 0, 0, 1, 1)
        self.pushButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalLayout.addWidget(self.pushButton, QtCore.Qt.AlignRight)
        self.pushButton.clicked.connect(self.proceed)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def buttonClicked(self):
        self.file_name = QtGui.QFileDialog.getOpenFileName(self, "Pick a folder")
        self.pix = QPixmap(self.file_name)
        if not self.pix.isNull():
            self.ImageButton.setPixmap(self.pix)
            self.flag=1

        else:
             self.ImageButton.setPixmap(QtGui.QPixmap(self.BUTTON_IMAGE))
             mBox=QMessageBox()
             mBox.setText("Not a Valid Image or Image Not Selected!")
             mBox.setWindowTitle("ERROR")
             mBox.setStandardButtons(QMessageBox.Ok)
             mBox.exec_()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "IMAGE BASED SEARCH", None))
        self.pushButton.setText(_translate("MainWindow", "Proceed", None))

    def proceed(self):
      if self.flag==1 and not self.pix.isNull() :
        self.list = []
        mpath="/home/aparna/4thsem/pop/ooad/pics_sift"
        print time.ctime()
        for f in os.listdir(mpath):
            print f
            res=sift.compare(str(os.path.join(mpath,f)),str(self.file_name),0)
            print time.ctime()
            if res >=8:
                self.list.append((str(os.path.join(mpath,f)),res))
            
        self.list=sorted(self.list,key=lambda x:x[1],reverse=True)
        for i in self.list:
          print i
        if len(self.list)!=0 :
          p1 = Ui_MainWindow(self.pix, self.list,self.file_name)
          p1.run(self.pix,self.list,self.file_name)
          #self.close()
        """app1 = QtGui.QApplication(sys.argv)
        print "Hi ..."
        form1 = Ui_MainWindow.setupUi()
        #form1.show()
        print "Hity ..."
        #sys.exit(app1.exec_())"""
      else :
            mBox=QMessageBox()
            mBox.setText("Please select an image !")
            mBox.setWindowTitle("ERROR")
            mBox.setStandardButtons(QMessageBox.Ok)
            mBox.exec_()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())
