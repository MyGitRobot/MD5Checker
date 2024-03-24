# -*- coding: utf-8 -*-

"""
Program: MD5 Generator and Checker
Author: MrCrawL
Created Date: 2024-01-28
Last Modified: 2024-03-24
Modified by: MrCrawL
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon
from hashlib import md5
from md5_checker_ui import Ui_Form
from mr_ico import icon_hex


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(384, 148)
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(bytes.fromhex(icon_hex))
        self.icon = QIcon(self.pixmap)
        self.setWindowIcon(self.icon)

        self.line.setPlaceholderText('选择文件后生成MD5')
        self.line_2.setPlaceholderText('输入官方提供的MD5值')
        self.button.clicked.connect(self.select_file)
        self.button_2.clicked.connect(self.copy)
        self.button_3.clicked.connect(self.check)

        self.fileDialog = QFileDialog()
        self.file = None
        self.md5 = None

    def Msgbox(self, msg_text:str):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(self.icon)
        msgBox.setWindowTitle('提示')
        msgBox.setIcon(QMessageBox.Icon.Information)
        msgBox.setText(msg_text)
        msgBox.addButton(QMessageBox.StandardButton.Ok)
        return msgBox

    def select_file(self):
        if self.fileDialog.exec():
            self.file = self.fileDialog.selectedFiles()[0]
            self.generate_md5()

    def generate_md5(self):
        if not self.file:
            msgBox = self.Msgbox('请选择需要校验的文件！')
            msgBox.exec()
            return None
        md5_hash = md5()
        with open(self.file, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                md5_hash.update(chunk)
            self.md5 = md5_hash.hexdigest()
            self.line.setText(self.md5)

    def copy(self):
        app.clipboard().setText(self.line.text())

    def check(self):
        origin_md5 = self.line_2.text()
        if len(origin_md5) != 32:
            msgBox = self.Msgbox('请输入有效的目标MD5值！')
            msgBox.exec()
            return None
        self.generate_md5()
        if origin_md5 == self.md5:
            msgBox = self.Msgbox('文件MD5值与目标MD5值一致。')
        else:
            msgBox = self.Msgbox('警告！MD5值不一致，\n请确认文件来源是否安全。')
        msgBox.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec())
