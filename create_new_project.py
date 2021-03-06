"""
Created By: Fatih Mehmet UNAL
- fatihunal@gmail.com
- fatihmehmet.unal@1000volt.com
-Start new project; this widget creates to:
- 3D
- edl
- exports
- offline
- online
- sound
- sources
- telecine
"""
from PySide.QtCore import QRegExp
from PySide.QtGui import *
import os
import datetime
import time
import sqlite3

class startProjectWindow(QWidget):
    def __init__(self):

        super(startProjectWindow, self).__init__()

        self.projectName = QLineEdit()
        self.projectName.setPlaceholderText("Project Name: ")
        regex = QRegExp("[a-z-A-Z_ ]+")

        Validator= QRegExpValidator(regex)
        self.projectName.setValidator(Validator)

        self.projectCode = QLineEdit()
        self.projectCode.setPlaceholderText("FW Code: ")
        regexCode = QRegExp("[0-9]+")
        regexCodeValidator = QRegExpValidator(regexCode)
        self.projectCode.setValidator(regexCodeValidator)

        self.infoTextNote = QLabel("You can put the info in to follow Textbox:")
        self.createNote = QTextEdit()
        self.createNote.setFixedHeight(50)

        self.projectOwner = QComboBox()
        personals = ["Select Creator", "Coordinator 1", "Coordinator 2", "Coordinator 3", "Coordinator 4"]
        self.projectOwner.addItems(personals)

        self.projectStyle = QComboBox()
        personals = ["Advertisment", "Motion Picture", "Other"]
        self.projectStyle.addItems(personals)

        self.folderCheckGroupBox = QGroupBox("Primary Folder(s)")

        self.check3D = QCheckBox("3D Folder")
        self.check3D.setChecked(1)
        self.check3D.setEnabled(0)
        self.checkEDL = QCheckBox("EDL Folder")
        self.checkEDL.setChecked(1)
        self.checkEDL.setEnabled(0)
        self.checkExports = QCheckBox("Exports")
        self.checkExports.setChecked(1)
        self.checkExports.setEnabled(0)
        self.checkOffline = QCheckBox("Offline")
        self.checkOffline.setChecked(1)
        self.checkOffline.setEnabled(0)
        self.checkOnline = QCheckBox("Online")
        self.checkOnline.setChecked(1)
        self.checkOnline.setEnabled(0)
        self.checkSound = QCheckBox("Sound(s)")
        self.checkSound.setChecked(1)
        self.checkSound.setEnabled(0)
        self.checkSources = QCheckBox("Source(s)")
        self.checkSources.setChecked(1)
        self.checkSources.setEnabled(0)
        self.checkTelecine = QCheckBox("Telecine")
        self.checkTelecine.setChecked(1)
        self.checkTelecine.setEnabled(0)

        self.checkLeftLayout = QVBoxLayout()
        self.checkRightLayout = QVBoxLayout()

        self.checkLeftLayout.addWidget(self.check3D)
        self.checkLeftLayout.addWidget(self.checkEDL)
        self.checkLeftLayout.addWidget(self.checkExports)
        self.checkLeftLayout.addWidget(self.checkOffline)

        self.checkRightLayout.addWidget(self.checkOnline)
        self.checkRightLayout.addWidget(self.checkSound)
        self.checkRightLayout.addWidget(self.checkSources)
        self.checkRightLayout.addWidget(self.checkTelecine)

        self.checkMainLayout = QHBoxLayout()
        self.checkMainLayout.addLayout(self.checkLeftLayout)
        self.checkMainLayout.addLayout(self.checkRightLayout)

        self.folderCheckGroupBox.setLayout(self.checkMainLayout)

        self.createButton = QPushButton()
        self.createButton.setText("Create Project")
        self.createButton.clicked.connect(self.createButtonDef)

        self.cancelButton = QPushButton("Close")
        self.cancelButton.clicked.connect(self.close)



        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.projectName)
        self.mainLayout.addWidget(self.projectCode)
        self.mainLayout.addWidget(self.infoTextNote)
        self.mainLayout.addWidget(self.createNote)
        self.mainLayout.addWidget(self.folderCheckGroupBox)
        self.mainLayout.addWidget(self.projectStyle)
        self.mainLayout.addWidget(self.projectOwner)
        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.addWidget(self.createButton)
        self.ButtonLayout.addWidget(self.cancelButton)
        self.mainLayout.addLayout(self.ButtonLayout)
        self.setLayout(self.mainLayout)


    def createButtonDef(self):
        """
        Create button fonction: What you want?
        :return:
        """
        self.ifEmptySection()

    def ifEmptySection(self):
        """
        Project required areas not empty section.
        :return:
        """
        if self.projectCode.text() == "":
            print "FW code is empty!"
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Required fields is not empty!\nProject Code(FW) is empty.")
            msgBox.exec_()

        else:
            self.createMainFolder()

        if self.projectName.text() == "":
            print "Project name is empty!"
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Required fields is not empty!\nProject Name is empty.")
            msgBox.exec_()
        else:
            self.createMainFolder()



    def createMainFolder(self):
        """
        Create main project and it's subfolders if not exists...
        - 3D
        - edl
        - exports
        - offline
        - online
        - sound
        - sources
        - telecine
        """
        if self.projectStyle.currentText() == "Advertisment":
            path = "C:/temp/adv/"
            os.mkdir(path + self.projectName.text())

            fw_code = self.projectCode.text()
            project_name = self.projectName.text()
            created_by = self.projectOwner.currentText()
            modified_time = str(datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y, %H:%M"))
            type = self.projectStyle.currentText()
            logPath = path + "/" + self.projectName.text()+ "/" + self.projectName.text()+"_log.db"

            con_adv = sqlite3.connect(logPath)
            con_adv.execute("CREATE TABLE IF NOT EXISTS log (fw_code INT, project_name TXT, created_by TEXT, modified_time REAL, type STR)")
            con_adv.commit()
            con_adv.execute("INSERT INTO log (fw_code, project_name, created_by, modified_time, type) VALUES (?,?,?,?,?)", (fw_code, project_name, created_by, modified_time, type))
            con_adv.commit()
            con_adv.close()

            os.makedirs(path + self.projectName.text() + "/" + "_OLD")
            os.makedirs(path + self.projectName.text() + "/" + "3D/final_render")
            os.makedirs(path + self.projectName.text() + "/" + "3D/pre_render")
            os.makedirs(path + self.projectName.text() + "/" + "EDL/online")
            os.makedirs(path + self.projectName.text() + "/" + "EDL/telecine")
            os.makedirs(path + self.projectName.text() + "/" + "exports/high_res")
            os.makedirs(path + self.projectName.text() + "/" + "exports/low_res")
            os.makedirs(path + self.projectName.text() + "/" + "exports/sound")
            os.makedirs(path + self.projectName.text() + "/" + "exports/transfer")
            os.makedirs(path + self.projectName.text() + "/" + "offline/from_offline")
            os.makedirs(path + self.projectName.text() + "/" + "offline/omf_aaf")
            os.makedirs(path + self.projectName.text() + "/" + "online/from_online")
            os.makedirs(path + self.projectName.text() + "/" + "sound/audio_tracks")
            os.makedirs(path + self.projectName.text() + "/" + "sound/final_mix")
            os.makedirs(path + self.projectName.text() + "/" + "sound/music")
            os.makedirs(path + self.projectName.text() + "/" + "sources/docs")
            os.makedirs(path + self.projectName.text() + "/" + "sources/images")
            os.makedirs(path + self.projectName.text() + "/" + "sources/raw")
            os.makedirs(path + self.projectName.text() + "/" + "telecine/graded")
            os.makedirs(path + self.projectName.text() + "/" + "telecine/graded/non_graded")



        elif self.projectStyle.currentText() == "Motion Picture":
            path = "C:/temp/mpc/"
            os.mkdir(path + self.projectName.text())
            fw_code = self.projectCode.text()
            project_name = self.projectName.text()
            created_by = self.projectOwner.currentText()
            modified_time = str(datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y, %H:%M"))

            logPath = path + "/" + self.projectName.text() + "/" + self.projectName.text()+"_log.db"

            con_mp = sqlite3.connect(logPath)
            con_mp.execute("CREATE TABLE IF NOT EXISTS log (fw_code INT, project_name TXT, created_by TEXT, modified_time REAL)")
            con_mp.commit()
            con_mp.execute("INSERT INTO log (fw_code, project_name, created_by, modified_time) VALUES (?,?,?,?)", (fw_code, project_name, created_by, modified_time))
            con_mp.commit()
            con_mp.close()

            os.makedirs(path + self.projectName.text() + "/" +"_OLD")
            os.makedirs(path + self.projectName.text() + "/" +"3D/final_render")
            os.makedirs(path + self.projectName.text() + "/" +"3D/pre_render")
            os.makedirs(path + self.projectName.text() + "/" +"EDL/online")
            os.makedirs(path + self.projectName.text() + "/" +"EDL/telecine")
            os.makedirs(path + self.projectName.text() + "/" +"exports/high_res")
            os.makedirs(path + self.projectName.text() + "/" +"exports/low_res")
            os.makedirs(path + self.projectName.text() + "/" +"exports/sound")
            os.makedirs(path + self.projectName.text() + "/" +"exports/transfer")
            os.makedirs(path + self.projectName.text() + "/" +"offline/from_offline")
            os.makedirs(path + self.projectName.text() + "/" +"offline/omf_aaf")
            os.makedirs(path + self.projectName.text() + "/" +"online/from_online")
            os.makedirs(path + self.projectName.text() + "/" +"sound/audio_tracks")
            os.makedirs(path + self.projectName.text() + "/" +"sound/final_mix")
            os.makedirs(path + self.projectName.text() + "/" +"sound/music")
            os.makedirs(path + self.projectName.text() + "/" +"sources/docs")
            os.makedirs(path + self.projectName.text() + "/" +"sources/images")
            os.makedirs(path + self.projectName.text() + "/" +"sources/raw")
            os.makedirs(path + self.projectName.text() + "/" +"telecine/graded")
            os.makedirs(path + self.projectName.text() + "/" +"telecine/graded/non_graded")



        else:
            print "There some error!"


def create_project_window():
    create_project_window.win = startProjectWindow()
    create_project_window.win.setWindowTitle("1000Volt Project Manager: Create Project")
    create_project_window.win.show()
