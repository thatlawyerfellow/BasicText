import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction,
                             QFileDialog, QFontDialog, QMessageBox, QDialog,
                             QVBoxLayout, QLineEdit, QPushButton, QLabel)
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super(FindReplaceDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.findLabel = QLabel("Find:", self)
        self.findLineEdit = QLineEdit(self)
        self.findButton = QPushButton("Find", self)
        self.findButton.clicked.connect(self.find)

        self.replaceLabel = QLabel("Replace with:", self)
        self.replaceLineEdit = QLineEdit(self)
        self.replaceButton = QPushButton("Replace", self)
        self.replaceButton.clicked.connect(self.replace)

        layout.addWidget(self.findLabel)
        layout.addWidget(self.findLineEdit)
        layout.addWidget(self.findButton)
        layout.addWidget(self.replaceLabel)
        layout.addWidget(self.replaceLineEdit)
        layout.addWidget(self.replaceButton)

        self.setLayout(layout)
        self.setWindowTitle("Find & Replace")

    def find(self):
        self.parent().findText(self.findLineEdit.text())

    def replace(self):
        self.parent().replaceText(self.findLineEdit.text(), self.replaceLineEdit.text())

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setWindowTitle('Basic Text')

        # File Menu Actions
        newAct = QAction('New', self)
        newAct.setShortcut('Ctrl+N')
        newAct.triggered.connect(self.newFile)

        openAct = QAction('Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.triggered.connect(self.openFile)

        saveAct = QAction('Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.triggered.connect(self.saveFile)

        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(self.exitCall)

        # Edit Menu Actions
        fontAct = QAction('Font', self)
        fontAct.triggered.connect(self.fontDialog)

        findAct = QAction('Find', self)
        findAct.setShortcut('Ctrl+F')
        findAct.triggered.connect(self.findDialog)

        # Alignment actions
        alignLeftAct = QAction('Left Align', self)
        alignLeftAct.setShortcut('Ctrl+L')
        alignLeftAct.triggered.connect(lambda: self.setAlignment(Qt.AlignLeft))

        alignCenterAct = QAction('Center Align', self)
        alignCenterAct.setShortcut('Ctrl+C')
        alignCenterAct.triggered.connect(lambda: self.setAlignment(Qt.AlignCenter))

        alignRightAct = QAction('Right Align', self)
        alignRightAct.setShortcut('Ctrl+R')
        alignRightAct.triggered.connect(lambda: self.setAlignment(Qt.AlignRight))

        justifyAct = QAction('Justify', self)
        justifyAct.setShortcut ('Ctrl+J')
        justifyAct.triggered.connect(lambda: self.setAlignment(Qt.AlignJustify))

        # Menubar and adding actions
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(fontAct)
        editMenu.addAction(findAct)

        alignMenu = editMenu.addMenu('Align')
        alignMenu.addAction(alignLeftAct)
        alignMenu.addAction(alignCenterAct)
        alignMenu.addAction(alignRightAct)
        alignMenu.addAction(justifyAct)

        helpMenu = menubar.addMenu('&Help')
        aboutAct = QAction('About', self)
        aboutAct.triggered.connect(self.aboutDialog)
        helpMenu.addAction(aboutAct)

        self.setGeometry(300, 300, 600, 400)

    # File Operations
    def newFile(self):
        self.textEdit.clear()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '/home')
        if filename:
            with open(filename, 'r') as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if filename:
            with open(filename, 'w') as file:
                text = self.textEdit.toPlainText()
                file.write(text)

    # Text Alignment
    def setAlignment(self, alignment):
        cursor = self.textEdit.textCursor()
        block_format = cursor.blockFormat()
        block_format.setAlignment(alignment)
        cursor.mergeBlockFormat(block_format)
        self.textEdit.mergeCurrentCharFormat(block_format)

    # Other features
    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def findDialog(self):
        dialog = FindReplaceDialog(self)
        dialog.exec_()

    def findText(self, query):
        text = self.textEdit.toPlainText()
        if query in text:
            QMessageBox.information(self, 'Found!', f"'{query}' found in the text")
        else:
            QMessageBox.information(self, 'Not Found', f"'{query}' not found in the text")

    def replaceText(self, query, replacement):
        text = self.textEdit.toPlainText()
        new_text = text.replace(query, replacement)
        self.textEdit.setPlainText(new_text)
        QMessageBox.information(self, 'Replaced', f"All occurrences of '{query}' have been replaced.")

    def aboutDialog(self):
        QMessageBox.about(self, "About Basic Text",
                          "BasicText v.1 | Developer: Ajay Kumar | Copyright: © 2024 (MMXXIV) | License: BasicText is released under the latest version of the GNU General Public License (GNU GPL) and any future versions of the license. | Disclaimer of Warranty: BasicText is provided 'as is' without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of the software is with you. Should the software prove defective, you assume the cost of all necessary servicing, repair, or correction. | This software is free; you are free to change and redistribute it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. | To get the Code: Visit the GitHub Repository https://github.com/thatlawyerfellow/BasicText")

    def exitCall(self):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

def main():
    app = QApplication(sys.argv)
    ex = TextEditor()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
