# Form implementation generated from reading ui file 'md5_checker_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(384, 148)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.button = QtWidgets.QPushButton(parent=Form)
        self.button.setGeometry(QtCore.QRect(40, 100, 71, 24))
        self.button.setObjectName("button")
        self.line = QtWidgets.QLineEdit(parent=Form)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(70, 60, 301, 20))
        self.line.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.line.setAcceptDrops(False)
        self.line.setText("")
        self.line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line.setReadOnly(True)
        self.line.setObjectName("line")
        self.button_2 = QtWidgets.QPushButton(parent=Form)
        self.button_2.setGeometry(QtCore.QRect(160, 100, 71, 24))
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(parent=Form)
        self.button_3.setGeometry(QtCore.QRect(280, 100, 71, 24))
        self.button_3.setObjectName("button_3")
        self.line_2 = QtWidgets.QLineEdit(parent=Form)
        self.line_2.setEnabled(True)
        self.line_2.setGeometry(QtCore.QRect(70, 30, 301, 20))
        self.line_2.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.line_2.setAcceptDrops(False)
        self.line_2.setText("")
        self.line_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_2.setReadOnly(False)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MD5生成校验器"))
        self.button.setText(_translate("Form", "选择文件"))
        self.button_2.setText(_translate("Form", "复   制"))
        self.button_3.setText(_translate("Form", "校   验"))
        self.label.setText(_translate("Form", "文件MD5"))
        self.label_2.setText(_translate("Form", "目标MD5"))