import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction,
                             QFileDialog, QFontDialog, QMessageBox, QDialog,
                             QVBoxLayout, QLineEdit, QPushButton, QLabel)
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt

# Define the FindReplaceDialog class, which provides a dialog for finding and replacing text
class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super(FindReplaceDialog, self).__init__(parent)
        self.initUI()  # Initialize the UI components

    def initUI(self):
        layout = QVBoxLayout()  # Use a vertical box layout

        # Create and configure UI components for finding text
        self.findLabel = QLabel("Find:", self)
        self.findLineEdit = QLineEdit(self)
        self.findButton = QPushButton("Find", self)
        self.findButton.clicked.connect(self.find)  # Connect the find button to the find method

        # Create and configure UI components for replacing text
        self.replaceLabel = QLabel("Replace with:", self)
        self.replaceLineEdit = QLineEdit(self)
        self.replaceButton = QPushButton("Replace", self)
        self.replaceButton.clicked.connect(self.replace)  # Connect the replace button to the replace method

        # Add the components to the layout and set the layout for the dialog
        layout.addWidget(self.findLabel)
        layout.addWidget(self.findLineEdit)
        layout.addWidget(self.findButton)
        layout.addWidget(self.replaceLabel)
        layout.addWidget(self.replaceLineEdit)
        layout.addWidget(self.replaceButton)

        self.setLayout(layout)
        self.setWindowTitle("Find & Replace")  # Set the window title

    def find(self):
        self.parent().findText(self.findLineEdit.text())  # Call the parent's findText method with the input text

    def replace(self):
        self.parent().replaceText(self.findLineEdit.text(), self.replaceLineEdit.text())  # Call the parent's replaceText method with the input and replacement text

# Define the TextEditor class, which represents the main window of the text editor application
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()  # Initialize the UI components

    def initUI(self):
        self.textEdit = QTextEdit()  # Create a QTextEdit widget for text editing
        self.setCentralWidget(self.textEdit)  # Set the QTextEdit widget as the central widget
        self.setWindowTitle('Basic Text')  # Set the window title

        # Create actions for the file menu
        newAct = QAction('New', self)
        newAct.setShortcut('Ctrl+N')
        newAct.triggered.connect(self.newFile)  # Connect the action to the newFile method

        openAct = QAction('Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.triggered.connect(self.openFile)  # Connect the action to the openFile method

        saveAct = QAction('Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.triggered.connect(self.saveFile)  # Connect the action to the saveFile method

        exitAct = QAction('Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(self.exitCall)  # Connect the action to the exitCall method

        # Create actions for the edit menu
        fontAct = QAction('Font', self)
        fontAct.triggered.connect(self.fontDialog)  # Connect the action to the fontDialog method

        findAct = QAction('Find', self)
        findAct.setShortcut('Ctrl+F')
        findAct.triggered.connect(self.findDialog)  # Connect the action to the findDialog method

        # Create actions for text alignment
        alignLeftAct = QAction('Left Align', self)
        alignLeftAct.setShortcut('Ctrl+L')
        alignLeftAct.triggered.connect(lambda: self.setAlignment(Qt.AlignLeft))  # Set text alignment to left

        alignCenterAct = QAction('Center Align', self)
        alignCenterAct.setShortcut('Ctrl+C')
        alignCenterAct.triggered.connect(lambda: self.setAlignment(Qt.AlignCenter))  # Set text alignment to center

        alignRightAct = QAction('Right Align', self)
        alignRightAct.setShortcut('Ctrl+R')
        alignRightAct.triggered.connect(lambda: self.setAlignment(Qt.AlignRight))  # Set text alignment to right

        justifyAct = QAction('Justify', self)
        justifyAct.setShortcut ('Ctrl+J')
        justifyAct.triggered.connect(lambda: self.setAlignment(Qt.AlignJustify))  # Set text alignment to justify

        # Create the menu bar and add the actions to their respective menus
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
        aboutAct.triggered.connect(self.aboutDialog)  # Connect the action to the aboutDialog method
        helpMenu.addAction(aboutAct)

        self.setGeometry(300, 300, 600, 400)  # Set the initial size and position of the window

    # Define methods for file operations, text alignment, font dialog, find and replace dialog, and the about dialog
    def newFile(self):
        self.textEdit.clear()

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r') as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def exitCall(self):
        self.close()

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def findDialog(self):
        self.findReplaceDialog = FindReplaceDialog(self)
        self.findReplaceDialog.show()

    def aboutDialog(self):
        QMessageBox.about(self, "About", "Basic Text Editor\n(c) Ajay Kumar 2024\nReleased under the GNU GPL\nCode available at https://github.com/thatlawyerfellow")

    def setAlignment(self, alignment):
        self.textEdit.setAlignment(alignment)

    def findText(self, text):
        if not self.textEdit.find(text):
            cursor = self.textEdit.textCursor()
            cursor.movePosition(QTextCursor.Start)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.find(text)

    def replaceText(self, findText, replaceText):
        text = self.textEdit.toPlainText()
        self.textEdit.setText(text.replace(findText, replaceText))

# Entry point of the application
def main():
    app = QApplication(sys.argv)  # Create an application instance
    ex = TextEditor()  # Create an instance of the TextEditor
    ex.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application's event loop

if __name__ == '__main__':
    main()

# (c) Ajay Kumar 2024 Released under the GNU GPL code available at https://github.com/thatlawyerfellow
