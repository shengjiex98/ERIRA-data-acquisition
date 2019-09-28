# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stripchart = QtWidgets.QWidget(self.centralwidget)
        self.stripchart.setObjectName("stripchart")
        self.gridLayout.addWidget(self.stripchart, 0, 1, 2, 1)
        self.stripchart_control_group = QtWidgets.QGroupBox(self.centralwidget)
        self.stripchart_control_group.setObjectName("stripchart_control_group")
        self.chart_refresh_button = QtWidgets.QPushButton(self.stripchart_control_group)
        self.chart_refresh_button.setGeometry(QtCore.QRect(9, 214, 124, 32))
        self.chart_refresh_button.setObjectName("chart_refresh_button")
        self.speed_slower_button = QtWidgets.QRadioButton(self.stripchart_control_group)
        self.speed_slower_button.setGeometry(QtCore.QRect(13, 48, 67, 20))
        self.speed_slower_button.setObjectName("speed_slower_button")
        self.chart_clear_button = QtWidgets.QPushButton(self.stripchart_control_group)
        self.chart_clear_button.setGeometry(QtCore.QRect(9, 163, 109, 32))
        self.chart_clear_button.setObjectName("chart_clear_button")
        self.speed_default_radio = QtWidgets.QRadioButton(self.stripchart_control_group)
        self.speed_default_radio.setEnabled(True)
        self.speed_default_radio.setGeometry(QtCore.QRect(13, 84, 69, 20))
        self.speed_default_radio.setChecked(True)
        self.speed_default_radio.setObjectName("speed_default_radio")
        self.speed_faster_radio = QtWidgets.QRadioButton(self.stripchart_control_group)
        self.speed_faster_radio.setGeometry(QtCore.QRect(13, 120, 64, 20))
        self.speed_faster_radio.setObjectName("speed_faster_radio")
        self.gridLayout.addWidget(self.stripchart_control_group, 1, 0, 1, 1)
        self.data_display_group = QtWidgets.QGroupBox(self.centralwidget)
        self.data_display_group.setObjectName("data_display_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.data_display_group)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.channelB_label = QtWidgets.QLabel(self.data_display_group)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.channelB_label.setFont(font)
        self.channelB_label.setObjectName("channelB_label")
        self.gridLayout_2.addWidget(self.channelB_label, 4, 0, 1, 1)
        self.channelA_label = QtWidgets.QLabel(self.data_display_group)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.channelA_label.setFont(font)
        self.channelA_label.setObjectName("channelA_label")
        self.gridLayout_2.addWidget(self.channelA_label, 2, 0, 1, 1)
        self.dec_label = QtWidgets.QLabel(self.data_display_group)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.dec_label.setFont(font)
        self.dec_label.setObjectName("dec_label")
        self.gridLayout_2.addWidget(self.dec_label, 1, 0, 1, 1)
        self.dec_value = QtWidgets.QLabel(self.data_display_group)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.dec_value.setFont(font)
        self.dec_value.setScaledContents(False)
        self.dec_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dec_value.setObjectName("dec_value")
        self.gridLayout_2.addWidget(self.dec_value, 1, 1, 1, 1)
        self.channelA_value = QtWidgets.QLabel(self.data_display_group)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.channelA_value.setFont(font)
        self.channelA_value.setScaledContents(False)
        self.channelA_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.channelA_value.setObjectName("channelA_value")
        self.gridLayout_2.addWidget(self.channelA_value, 2, 1, 1, 1)
        self.channelB_value = QtWidgets.QLabel(self.data_display_group)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.channelB_value.setFont(font)
        self.channelB_value.setScaledContents(False)
        self.channelB_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.channelB_value.setObjectName("channelB_value")
        self.gridLayout_2.addWidget(self.channelB_value, 4, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.data_display_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 42)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 5, 0, 1, 2)
        self.ra_value = QtWidgets.QLabel(self.data_display_group)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.ra_value.setFont(font)
        self.ra_value.setScaledContents(False)
        self.ra_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ra_value.setObjectName("ra_value")
        self.gridLayout_2.addWidget(self.ra_value, 0, 1, 1, 1)
        self.ra_label = QtWidgets.QLabel(self.data_display_group)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.ra_label.setFont(font)
        self.ra_label.setObjectName("ra_label")
        self.gridLayout_2.addWidget(self.ra_label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.data_display_group, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuCalibration = QtWidgets.QMenu(self.menubar)
        self.menuCalibration.setObjectName("menuCalibration")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRA = QtWidgets.QAction(MainWindow)
        self.actionRA.setObjectName("actionRA")
        self.actionDec = QtWidgets.QAction(MainWindow)
        self.actionDec.setObjectName("actionDec")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionworld = QtWidgets.QAction(MainWindow)
        self.actionworld.setObjectName("actionworld")
        self.actionSurvey = QtWidgets.QAction(MainWindow)
        self.actionSurvey.setObjectName("actionSurvey")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionScan = QtWidgets.QAction(MainWindow)
        self.actionScan.setObjectName("actionScan")
        self.actionSpectrum = QtWidgets.QAction(MainWindow)
        self.actionSpectrum.setObjectName("actionSpectrum")
        self.menuCalibration.addAction(self.actionRA)
        self.menuCalibration.addAction(self.actionDec)
        self.menuNew.addAction(self.actionSurvey)
        self.menuNew.addAction(self.actionScan)
        self.menuNew.addAction(self.actionSpectrum)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionInfo)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionStop)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCalibration.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stripchart_control_group.setTitle(_translate("MainWindow", "Strip chart"))
        self.chart_refresh_button.setText(_translate("MainWindow", "Refresh chart"))
        self.speed_slower_button.setText(_translate("MainWindow", "Slower"))
        self.chart_clear_button.setText(_translate("MainWindow", "Clear chart"))
        self.speed_default_radio.setText(_translate("MainWindow", "Default"))
        self.speed_faster_radio.setText(_translate("MainWindow", "Faster"))
        self.data_display_group.setTitle(_translate("MainWindow", "Data"))
        self.channelB_label.setText(_translate("MainWindow", "Channel B voltage:"))
        self.channelA_label.setText(_translate("MainWindow", "Channel A voltage:"))
        self.dec_label.setText(_translate("MainWindow", "Declination:"))
        self.dec_value.setText(_translate("MainWindow", "0.0deg"))
        self.channelA_value.setText(_translate("MainWindow", "0.00V"))
        self.channelB_value.setText(_translate("MainWindow", "0.00V"))
        self.ra_value.setText(_translate("MainWindow", "00:00:00"))
        self.ra_label.setText(_translate("MainWindow", "Right Ascension:"))
        self.menuCalibration.setTitle(_translate("MainWindow", "Calibrate"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.actionRA.setText(_translate("MainWindow", "RA..."))
        self.actionDec.setText(_translate("MainWindow", "Dec..."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionworld.setText(_translate("MainWindow", "world"))
        self.actionSurvey.setText(_translate("MainWindow", "Survey"))
        self.actionInfo.setText(_translate("MainWindow", "Info..."))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionHelp.setText(_translate("MainWindow", "Help..."))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionScan.setText(_translate("MainWindow", "Scan"))
        self.actionSpectrum.setText(_translate("MainWindow", "Spectrum"))
