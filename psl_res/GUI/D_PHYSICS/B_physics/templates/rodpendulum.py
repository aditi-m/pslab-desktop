# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rodpendulum.ui'

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(735, 612)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widgetFrameOuter = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setStyleSheet(_fromUtf8(""))
        self.widgetFrameOuter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.widgetFrameOuter.setObjectName(_fromUtf8("widgetFrameOuter"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame_4 = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setMargin(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton = QtGui.QPushButton(self.frame_4)
        self.pushButton.setMinimumSize(QtCore.QSize(94, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.frame_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(94, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.progressBar = QtGui.QProgressBar(self.frame_4)
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar:horizontal {\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"background: white;\n"
"padding: 1px;\n"
"text-align: right;\n"
"margin-right: 5ex;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #467, stop:1 white);\n"
"margin-right: 1px; /* space */\n"
"width: 5px;\n"
"}"))
        self.progressBar.setMaximum(2500)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.timerProgress = QtGui.QProgressBar(self.frame_4)
        self.timerProgress.setMaximumSize(QtCore.QSize(16777215, 18))
        self.timerProgress.setStyleSheet(_fromUtf8(""))
        self.timerProgress.setMaximum(60)
        self.timerProgress.setProperty("value", 0)
        self.timerProgress.setTextVisible(True)
        self.timerProgress.setObjectName(_fromUtf8("timerProgress"))
        self.horizontalLayout_2.addWidget(self.timerProgress)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_2 = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.resultsTable = QtGui.QTableWidget(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsTable.sizePolicy().hasHeightForWidth())
        self.resultsTable.setSizePolicy(sizePolicy)
        self.resultsTable.setMinimumSize(QtCore.QSize(360, 0))
        self.resultsTable.setAlternatingRowColors(True)
        self.resultsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.resultsTable.setGridStyle(QtCore.Qt.DashLine)
        self.resultsTable.setRowCount(100)
        self.resultsTable.setColumnCount(1)
        self.resultsTable.setObjectName(_fromUtf8("resultsTable"))
        self.resultsTable.horizontalHeader().setDefaultSectionSize(150)
        self.resultsTable.horizontalHeader().setMinimumSectionSize(40)
        self.resultsTable.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.resultsTable)
        self.frame_3 = QtGui.QFrame(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBox = QtGui.QComboBox(self.frame_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox, 10, 1, 1, 1)
        self.line = QtGui.QFrame(self.frame_3)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 8, 0, 1, 2)
        self.pushButton_6 = QtGui.QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_2.addWidget(self.pushButton_6, 13, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.frame_3)
        self.line_2.setMinimumSize(QtCore.QSize(30, 0))
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 4, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 15, 0, 1, 1)
        self.averageLabel = QtGui.QLabel(self.frame_3)
        self.averageLabel.setObjectName(_fromUtf8("averageLabel"))
        self.gridLayout_2.addWidget(self.averageLabel, 5, 1, 1, 1)
        self.averageLabel_2 = QtGui.QLabel(self.frame_3)
        self.averageLabel_2.setObjectName(_fromUtf8("averageLabel_2"))
        self.gridLayout_2.addWidget(self.averageLabel_2, 10, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 11, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_2.addWidget(self.pushButton_4, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.gLabel = QtGui.QLabel(self.frame_3)
        self.gLabel.setObjectName(_fromUtf8("gLabel"))
        self.gridLayout_2.addWidget(self.gLabel, 13, 1, 1, 1)
        self.lenBox = QtGui.QDoubleSpinBox(self.frame_3)
        self.lenBox.setObjectName(_fromUtf8("lenBox"))
        self.gridLayout_2.addWidget(self.lenBox, 11, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.frame_3)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 12, 0, 1, 2)
        self.pointBox = QtGui.QSpinBox(self.frame_3)
        self.pointBox.setMinimum(5)
        self.pointBox.setMaximum(1000)
        self.pointBox.setObjectName(_fromUtf8("pointBox"))
        self.gridLayout_2.addWidget(self.pointBox, 0, 1, 1, 1)
        self.line_4 = QtGui.QFrame(self.frame_3)
        self.line_4.setMinimumSize(QtCore.QSize(30, 0))
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_2.addWidget(self.line_4, 1, 0, 1, 2)
        self.line_5 = QtGui.QFrame(self.frame_3)
        self.line_5.setMinimumSize(QtCore.QSize(30, 0))
        self.line_5.setLineWidth(1)
        self.line_5.setMidLineWidth(0)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 2, 0, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 16, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_2.addWidget(self.pushButton_5, 16, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout_3.addWidget(self.widgetFrameOuter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.run)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.stop)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.calcAvg)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.setPendulumType)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.calculateg)
        QtCore.QObject.connect(self.pointBox, QtCore.SIGNAL(_fromUtf8("editingFinished()")), MainWindow.setTotalPoints)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.saveData)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.clearTable)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.widgetFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.pushButton_3.setText(_translate("MainWindow", "Stop", None))
        self.progressBar.setFormat(_translate("MainWindow", "%v", None))
        self.timerProgress.setToolTip(_translate("MainWindow", "Time left before the stopwatch overflows.\n"
" Oscillations must finish within this time limit", None))
        self.timerProgress.setFormat(_translate("MainWindow", "%v Seconds to timeout", None))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.resultsTable.setToolTip(_translate("MainWindow", "List of time periods for complete oscillations.\n"
"Click and drag to select points.\n"
"Hold down CTRL key and click to select non consecutive points", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Simple Pendulum", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Rod Pendulum", None))
        self.pushButton_6.setText(_translate("MainWindow", "Calculate", None))
        self.averageLabel.setText(_translate("MainWindow", "result", None))
        self.averageLabel_2.setText(_translate("MainWindow", "Value of g using :", None))
        self.label_2.setText(_translate("MainWindow", "Length (cm)", None))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Obtain average of data points selected in the table", None))
        self.pushButton_4.setText(_translate("MainWindow", "Average Selected points>", None))
        self.label.setText(_translate("MainWindow", "Data Analysis", None))
        self.label.setProperty("class", _translate("MainWindow", "headingLabel", None))
        self.gLabel.setText(_translate("MainWindow", "g:", None))
        self.label_3.setText(_translate("MainWindow", "Points to acquire", None))
        self.pushButton_2.setText(_translate("MainWindow", "Clear Table", None))
        self.pushButton_5.setText(_translate("MainWindow", "Save Table", None))
