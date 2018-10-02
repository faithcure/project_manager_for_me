"""
Created By: Fatih Mehmet UNAL
- fatihunal@gmail.com
- fatihmehmet.unal@1000volt.com
This script contains remove personal or rename of the label.
"""
from PySide.QtGui import *
class user_settings(QWidget):
    def __init__(self):

        super(user_settings, self).__init__()

        self.listUsers = QTableWidget()

        self.searchInTable = QLineEdit()
        self.searchInTable.setPlaceholderText("Search and Find")

        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.close)

        self.deleteUser = QPushButton("Kill Him!")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.listUsers)
        self.mainLayout.addWidget(self.searchInTable)
        self.mainLayout.addWidget(self.deleteUser)
        self.mainLayout.addWidget(self.cancelButton)
        self.setLayout(self.mainLayout)


def start_user_settings():
    start_user_settings.win = user_settings()
    start_user_settings.win.setWindowTitle("User Settings")
    start_user_settings.win.show()
