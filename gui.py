from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import ftpserver as ftp

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.submitButton = QPushButton("Start server")

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.submitContact)

        mainLayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")

    def submitContact(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please enter a name and address.")
            return
        else:
            QMessageBox.information(self, "Success!",
                                    "Hello %s!" % open('pyqt.py', 'r').readline())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())