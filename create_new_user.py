"""
Created By: Fatih Mehmet UNAL
- fatihunal@gmail.com
- fatihmehmet.unal@1000volt.com
"""

from PySide.QtGui import *


class create_new_user(QWidget):
    def __init__(self):

        super(create_new_user, self).__init__()

        self.userName = QLineEdit()
        self.userName.setPlaceholderText("Name")

        self.surName = QLineEdit()
        self.surName.setPlaceholderText("Surname")

        self.userIDLabel = QLabel("User ID: #00126")


        self.emplooyeName = QComboBox()
        self.emplooyeName.addItems(["Gorev_1","Gorev_2", "Gorev_3", "Gorev_4"])

        self.IDLayout = QHBoxLayout()
        self.IDLayout.addWidget(self.userIDLabel)


        self.freeLance = QCheckBox("Freelancer")
        self.inHouse = QCheckBox("Inhouse")

        self.createButton = QPushButton("Create User")
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.close)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.createButton)
        self.buttonLayout.addWidget(self.cancelButton)


        self.checklayout = QHBoxLayout()
        self.checklayout.addWidget(self.freeLance)
        self.checklayout.addWidget(self.inHouse)


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.userName)
        self.mainLayout.addWidget(self.surName)
        self.mainLayout.addWidget(self.emplooyeName)
        self.mainLayout.addLayout(self.checklayout)
        self.mainLayout.addLayout(self.IDLayout)
        self.mainLayout.addLayout(self.buttonLayout)
        self.setLayout(self.mainLayout)


def start_create_project_window():
    start_create_project_window.win = create_new_user()
    start_create_project_window.win.setWindowTitle("Create new user")
    start_create_project_window.win.show()
