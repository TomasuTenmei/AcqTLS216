# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acq-tls216.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
from GUI.Icons import icons8_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(703, 725)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Settings/services.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.widget_2)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.spinBox_2 = QSpinBox(self.widget_2)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout.addWidget(self.spinBox_2)

        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.ipFrame = QFrame(self.widget_2)
        self.ipFrame.setObjectName(u"ipFrame")
        self.hLayout_IP = QHBoxLayout(self.ipFrame)
        self.hLayout_IP.setSpacing(0)
        self.hLayout_IP.setObjectName(u"hLayout_IP")
        self.hLayout_IP.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_IP.addItem(self.horizontalSpacer)

        self.label_7 = QLabel(self.ipFrame)
        self.label_7.setObjectName(u"label_7")

        self.hLayout_IP.addWidget(self.label_7)

        self.spinBox_3 = QSpinBox(self.ipFrame)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setEnabled(True)
        self.spinBox_3.setWrapping(False)
        self.spinBox_3.setFrame(False)
        self.spinBox_3.setAlignment(Qt.AlignCenter)
        self.spinBox_3.setReadOnly(False)
        self.spinBox_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_3.setKeyboardTracking(True)
        self.spinBox_3.setProperty("showGroupSeparator", False)
        self.spinBox_3.setMaximum(255)

        self.hLayout_IP.addWidget(self.spinBox_3)

        self.label_4 = QLabel(self.ipFrame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.hLayout_IP.addWidget(self.label_4)

        self.spinBox_4 = QSpinBox(self.ipFrame)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setWrapping(False)
        self.spinBox_4.setFrame(False)
        self.spinBox_4.setAlignment(Qt.AlignCenter)
        self.spinBox_4.setReadOnly(False)
        self.spinBox_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_4.setKeyboardTracking(True)
        self.spinBox_4.setMaximum(255)

        self.hLayout_IP.addWidget(self.spinBox_4)

        self.label_5 = QLabel(self.ipFrame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setTextInteractionFlags(Qt.NoTextInteraction)

        self.hLayout_IP.addWidget(self.label_5)

        self.spinBox_5 = QSpinBox(self.ipFrame)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setWrapping(False)
        self.spinBox_5.setFrame(False)
        self.spinBox_5.setAlignment(Qt.AlignCenter)
        self.spinBox_5.setReadOnly(False)
        self.spinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_5.setKeyboardTracking(True)
        self.spinBox_5.setMaximum(255)

        self.hLayout_IP.addWidget(self.spinBox_5)

        self.label_6 = QLabel(self.ipFrame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setTextInteractionFlags(Qt.NoTextInteraction)

        self.hLayout_IP.addWidget(self.label_6)

        self.spinBox_6 = QSpinBox(self.ipFrame)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setWrapping(False)
        self.spinBox_6.setFrame(False)
        self.spinBox_6.setAlignment(Qt.AlignCenter)
        self.spinBox_6.setReadOnly(False)
        self.spinBox_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_6.setKeyboardTracking(True)
        self.spinBox_6.setMaximum(255)

        self.hLayout_IP.addWidget(self.spinBox_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_IP.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.ipFrame)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_18, 7, 3, 1, 1)

        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_27, 19, 3, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_12, 3, 3, 1, 1)

        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_26, 17, 3, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 5, 5, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 3, 5, 1, 1)

        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_20, 9, 3, 1, 1)

        self.line_11 = QFrame(self.frame_2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_11, 34, 5, 1, 1)

        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_2.addWidget(self.label_39, 27, 5, 1, 1)

        self.line_4 = QFrame(self.frame_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 0))
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 0, 6, 35, 1)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 0, 4, 35, 1)

        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_2.addWidget(self.label_40, 29, 5, 1, 1)

        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_2.addWidget(self.label_41, 31, 5, 1, 1)

        self.line_10 = QFrame(self.frame_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_10, 34, 1, 1, 1)

        self.label_42 = QLabel(self.frame_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_2.addWidget(self.label_42, 33, 5, 1, 1)

        self.line_14 = QFrame(self.frame_2)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_14, 4, 1, 1, 1)

        self.line_18 = QFrame(self.frame_2)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_18, 8, 1, 1, 1)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_24, 13, 3, 1, 1)

        self.line_15 = QFrame(self.frame_2)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_15, 4, 3, 1, 1)

        self.line_16 = QFrame(self.frame_2)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_16, 4, 5, 1, 1)

        self.line_17 = QFrame(self.frame_2)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_17, 6, 1, 1, 1)

        self.line_19 = QFrame(self.frame_2)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_19, 10, 1, 1, 1)

        self.line_22 = QFrame(self.frame_2)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_22, 16, 1, 1, 1)

        self.line_26 = QFrame(self.frame_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_26, 24, 1, 1, 1)

        self.line_27 = QFrame(self.frame_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_27, 26, 1, 1, 1)

        self.line_24 = QFrame(self.frame_2)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_24, 20, 1, 1, 1)

        self.line_28 = QFrame(self.frame_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_28, 28, 1, 1, 1)

        self.line_29 = QFrame(self.frame_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_29, 30, 1, 1, 1)

        self.line_25 = QFrame(self.frame_2)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_25, 22, 1, 1, 1)

        self.line_21 = QFrame(self.frame_2)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_21, 14, 1, 1, 1)

        self.line_23 = QFrame(self.frame_2)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_23, 18, 1, 1, 1)

        self.line_20 = QFrame(self.frame_2)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_20, 12, 1, 1, 1)

        self.line_32 = QFrame(self.frame_2)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_32, 8, 3, 1, 1)

        self.line_34 = QFrame(self.frame_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_34, 12, 3, 1, 1)

        self.line_36 = QFrame(self.frame_2)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_36, 16, 3, 1, 1)

        self.line_33 = QFrame(self.frame_2)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.HLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_33, 10, 3, 1, 1)

        self.line_37 = QFrame(self.frame_2)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_37, 18, 3, 1, 1)

        self.line_30 = QFrame(self.frame_2)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_30, 32, 1, 1, 1)

        self.line_39 = QFrame(self.frame_2)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_39, 22, 3, 1, 1)

        self.line_41 = QFrame(self.frame_2)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.HLine)
        self.line_41.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_41, 26, 3, 1, 1)

        self.line_38 = QFrame(self.frame_2)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.HLine)
        self.line_38.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_38, 20, 3, 1, 1)

        self.line_42 = QFrame(self.frame_2)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.HLine)
        self.line_42.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_42, 28, 3, 1, 1)

        self.line_40 = QFrame(self.frame_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.HLine)
        self.line_40.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_40, 24, 3, 1, 1)

        self.line_44 = QFrame(self.frame_2)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.HLine)
        self.line_44.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_44, 32, 3, 1, 1)

        self.line_43 = QFrame(self.frame_2)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.HLine)
        self.line_43.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_43, 30, 3, 1, 1)

        self.line_35 = QFrame(self.frame_2)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_35, 14, 3, 1, 1)

        self.line_46 = QFrame(self.frame_2)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.HLine)
        self.line_46.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_46, 8, 5, 1, 1)

        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        sizePolicy2.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy2)
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_31.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_31, 27, 3, 1, 1)

        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        sizePolicy2.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy2)
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_29.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_29, 23, 3, 1, 1)

        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        sizePolicy2.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy2)
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_32, 29, 3, 1, 1)

        self.checkBox_6 = QCheckBox(self.frame_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy3)
        self.checkBox_6.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_6.setCheckable(True)
        self.checkBox_6.setChecked(False)
        self.checkBox_6.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_6, 11, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.frame_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        sizePolicy3.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy3)
        self.checkBox_8.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_8.setCheckable(True)
        self.checkBox_8.setChecked(False)
        self.checkBox_8.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_8, 15, 1, 1, 1)

        self.checkBox_9 = QCheckBox(self.frame_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy3.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy3)
        self.checkBox_9.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_9.setCheckable(True)
        self.checkBox_9.setChecked(False)
        self.checkBox_9.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_9, 17, 1, 1, 1)

        self.checkBox_7 = QCheckBox(self.frame_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        sizePolicy3.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy3)
        self.checkBox_7.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_7.setCheckable(True)
        self.checkBox_7.setChecked(False)
        self.checkBox_7.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_7, 13, 1, 1, 1)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 15, 5, 1, 1)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 0))
        self.line_5.setLineWidth(1)
        self.line_5.setMidLineWidth(0)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 0, 0, 35, 1)

        self.checkBox_10 = QCheckBox(self.frame_2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy3.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy3)
        self.checkBox_10.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_10.setCheckable(True)
        self.checkBox_10.setChecked(False)
        self.checkBox_10.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_10, 19, 1, 1, 1)

        self.checkBox_11 = QCheckBox(self.frame_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        sizePolicy3.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy3)
        self.checkBox_11.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_11.setCheckable(True)
        self.checkBox_11.setChecked(False)
        self.checkBox_11.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_11, 21, 1, 1, 1)

        self.checkBox_12 = QCheckBox(self.frame_2)
        self.checkBox_12.setObjectName(u"checkBox_12")
        sizePolicy3.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy3)
        self.checkBox_12.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_12.setCheckable(True)
        self.checkBox_12.setChecked(False)
        self.checkBox_12.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_12, 23, 1, 1, 1)

        self.checkBox_15 = QCheckBox(self.frame_2)
        self.checkBox_15.setObjectName(u"checkBox_15")
        sizePolicy3.setHeightForWidth(self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy3)
        self.checkBox_15.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_15.setCheckable(True)
        self.checkBox_15.setChecked(False)
        self.checkBox_15.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_15, 29, 1, 1, 1)

        self.checkBox_14 = QCheckBox(self.frame_2)
        self.checkBox_14.setObjectName(u"checkBox_14")
        sizePolicy3.setHeightForWidth(self.checkBox_14.sizePolicy().hasHeightForWidth())
        self.checkBox_14.setSizePolicy(sizePolicy3)
        self.checkBox_14.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_14.setCheckable(True)
        self.checkBox_14.setChecked(False)
        self.checkBox_14.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_14, 27, 1, 1, 1)

        self.checkBox_16 = QCheckBox(self.frame_2)
        self.checkBox_16.setObjectName(u"checkBox_16")
        sizePolicy3.setHeightForWidth(self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy3)
        self.checkBox_16.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_16.setCheckable(True)
        self.checkBox_16.setChecked(False)
        self.checkBox_16.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_16, 31, 1, 1, 1)

        self.checkBox_13 = QCheckBox(self.frame_2)
        self.checkBox_13.setObjectName(u"checkBox_13")
        sizePolicy3.setHeightForWidth(self.checkBox_13.sizePolicy().hasHeightForWidth())
        self.checkBox_13.setSizePolicy(sizePolicy3)
        self.checkBox_13.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_13.setCheckable(True)
        self.checkBox_13.setChecked(False)
        self.checkBox_13.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_13, 25, 1, 1, 1)

        self.checkBox_17 = QCheckBox(self.frame_2)
        self.checkBox_17.setObjectName(u"checkBox_17")
        sizePolicy3.setHeightForWidth(self.checkBox_17.sizePolicy().hasHeightForWidth())
        self.checkBox_17.setSizePolicy(sizePolicy3)
        self.checkBox_17.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_17.setCheckable(True)
        self.checkBox_17.setChecked(False)
        self.checkBox_17.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_17, 33, 1, 1, 1)

        self.line_13 = QFrame(self.frame_2)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_13, 0, 5, 1, 1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 17, 5, 1, 1)

        self.line_12 = QFrame(self.frame_2)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_12, 0, 3, 1, 1)

        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_2.addWidget(self.label_35, 19, 5, 1, 1)

        self.label_36 = QLabel(self.frame_2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_2.addWidget(self.label_36, 21, 5, 1, 1)

        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_2.addWidget(self.label_37, 23, 5, 1, 1)

        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_2.addWidget(self.label_38, 25, 5, 1, 1)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 2, 35, 1)

        self.checkBox_2 = QCheckBox(self.frame_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy3.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy3)
        self.checkBox_2.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_2, 3, 1, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 13, 5, 1, 1)

        self.checkBox_3 = QCheckBox(self.frame_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy3.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy3)
        self.checkBox_3.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_3, 5, 1, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 11, 5, 1, 1)

        self.checkBox_4 = QCheckBox(self.frame_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy3.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy3)
        self.checkBox_4.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_4.setCheckable(True)
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_4, 7, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.frame_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy3.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy3)
        self.checkBox_5.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_5.setCheckable(True)
        self.checkBox_5.setChecked(False)
        self.checkBox_5.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox_5, 9, 1, 1, 1)

        self.line_9 = QFrame(self.frame_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_9, 34, 3, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_2.addWidget(self.label_10, 1, 5, 1, 1)

        self.line_6 = QFrame(self.frame_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 2, 1, 1, 1)

        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_23, 11, 3, 1, 1)

        self.line_8 = QFrame(self.frame_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 2, 5, 1, 1)

        self.line_7 = QFrame(self.frame_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 2, 3, 1, 1)

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 9, 5, 1, 1)

        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        sizePolicy2.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy2)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_30.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_30, 25, 3, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 1)

        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_25, 15, 3, 1, 1)

        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_34.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_34, 33, 3, 1, 1)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 7, 5, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_15, 5, 3, 1, 1)

        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")
        sizePolicy2.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy2)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_33, 31, 3, 1, 1)

        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_28.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.gridLayout_2.addWidget(self.label_28, 21, 3, 1, 1)

        self.line_31 = QFrame(self.frame_2)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_31, 6, 3, 1, 1)

        self.line_45 = QFrame(self.frame_2)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.HLine)
        self.line_45.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_45, 6, 5, 1, 1)

        self.line_47 = QFrame(self.frame_2)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.HLine)
        self.line_47.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_47, 10, 5, 1, 1)

        self.line_48 = QFrame(self.frame_2)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.HLine)
        self.line_48.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_48, 12, 5, 1, 1)

        self.line_49 = QFrame(self.frame_2)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.HLine)
        self.line_49.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_49, 14, 5, 1, 1)

        self.line_50 = QFrame(self.frame_2)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.HLine)
        self.line_50.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_50, 16, 5, 1, 1)

        self.line_51 = QFrame(self.frame_2)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.HLine)
        self.line_51.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_51, 18, 5, 1, 1)

        self.line_52 = QFrame(self.frame_2)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShape(QFrame.HLine)
        self.line_52.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_52, 20, 5, 1, 1)

        self.line_53 = QFrame(self.frame_2)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShape(QFrame.HLine)
        self.line_53.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_53, 22, 5, 1, 1)

        self.line_54 = QFrame(self.frame_2)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.HLine)
        self.line_54.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_54, 24, 5, 1, 1)

        self.line_55 = QFrame(self.frame_2)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.HLine)
        self.line_55.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_55, 26, 5, 1, 1)

        self.line_56 = QFrame(self.frame_2)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.HLine)
        self.line_56.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_56, 28, 5, 1, 1)

        self.line_57 = QFrame(self.frame_2)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.HLine)
        self.line_57.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_57, 30, 5, 1, 1)

        self.line_58 = QFrame(self.frame_2)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.HLine)
        self.line_58.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_58, 32, 5, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AcqTLS216", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tektronix TLS 216 data acquisition application", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GPIB", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"gateway: IP <> GPIB", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"IP gateway:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CH5", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CH7", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"CH8", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CH6", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"CH9", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"CH10", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"CH11", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"CH14", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"CH13", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"CH15", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"CH12", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"CH16", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CH3", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CH4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

