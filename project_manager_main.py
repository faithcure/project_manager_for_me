"""
This is mainWindow for project managment system. Like the create project coming from in this main window.
Created By: Fatih Mehmet UNAL
- fatihunal@gmail.com
- fatihmehmet.unal@1000volt.com
"""

import create_new_project
import user_settings
import create_new_user
from PySide.QtGui import *
from PySide.QtCore import *
import sys
import os

class project_manager_central_widget(QWidget):
    def __init__(self):
        super(project_manager_central_widget, self).__init__()


        self.projectTabs = QTabWidget()
        self.projectTabs.addTab(advSystem(), "Advertisiment")
        self.projectTabs.addTab(backUp(), "Backup")

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.projectTabs)
        self.setLayout(self.mainLayout)

class advSystem(QWidget):#Advertisiment Control System Class
    def __init__(self, parent = None):
        super(advSystem, self).__init__(parent)

        self.advProject_info = QGroupBox("Project Info: ")
        self.advProject_info.setFixedHeight(110)

        self.adv_project_employee = QGroupBox("Personal section: ")
        self.adv_project_employee.setFixedHeight(90)

        self.advList = QListWidget()
        self.advList.setAlternatingRowColors(1)
        list = ["proje1", "proje2", "proje3","proje4"]
        self.advList.setFixedWidth(220)
        self.advList.addItems(list)

        self.subProject = QListWidget()
        self.subProject.setFixedWidth(220)


        self.searchAdvList = QLineEdit()
        self.searchAdvList.setFixedWidth(220)
        self.searchAdvList.setPlaceholderText("Find: ")

        self.createNewProject = QPushButton("New Project")

        self.projectType  = QLabel("Project Type: Advertisiment")
        self.projectPath  = QLabel("Path: X:/deneme/bir/yol/on/path")
        self.projectStartingDate  = QLabel("Pipeline: 12-24-2018, 16:22")
        self.deadlineDate  = QLabel("Deadline: 05-12-2018, 16:22")
        self.projectManager = QLabel("Manager Name: Fatih UNAL")
        self.projectName = QLabel("ProjectName: Cok Guzel Hareket Bunlar")
        self.fw_Code = QLabel("FW_Code: #12521")
        self.projectDescrp = QLabel("Description: Project Aciklamasi buraya gelecek")

        self.logo = QPixmap("img/projectManagement_icon_logo.png")
        self.logoLabel =QLabel()
        self.logoLabel.setPixmap(self.logo)

        self.addPersonal = QPushButton("Add Personal")
        self.addPersonal.setFixedWidth(150)

        self.opOne = QLabel("Nuke: Fatih UNAL")
        self.opTwo = QLabel("Fushion: Okan DUZALAN")
        self.opThree = QLabel("Flame: OSUBU")

        self.progressProject = QProgressBar()
        self.progressProject.setValue(15)

        self.advMainLayout = QHBoxLayout()

        self.advListLayout = QVBoxLayout()



        self.newOperationGrp = QHBoxLayout()
        self.advProject_boxes_layout = QVBoxLayout()
        self.adv_project_employee_Grp = QHBoxLayout()
        self.newOperationGrpLeftLayout = QVBoxLayout()
        self.newOperationGrpRightLayout = QVBoxLayout()
        self.newOperationGrpLogoLayout = QVBoxLayout()
        self.adv_project_employee_Grp.addWidget(self.addPersonal)
        self.adv_project_employee_Grp.addWidget(self.opOne)
        self.adv_project_employee_Grp.addWidget(self.opThree)
        self.adv_project_employee_Grp.addWidget(self.opTwo)
        self.newOperationGrp.addLayout(self.newOperationGrpLeftLayout)
        self.newOperationGrp.addLayout(self.newOperationGrpRightLayout)
        self.newOperationGrp.addLayout(self.newOperationGrpLogoLayout)
        self.newOperationGrpLeftLayout.addWidget(self.projectType)
        self.newOperationGrpLeftLayout.addWidget(self.projectPath)
        self.newOperationGrpLeftLayout.addWidget(self.projectStartingDate)
        self.newOperationGrpLeftLayout.addWidget(self.deadlineDate)
        self.newOperationGrpRightLayout.addWidget(self.projectManager)
        self.newOperationGrpRightLayout.addWidget(self.projectName)
        self.newOperationGrpRightLayout.addWidget(self.projectDescrp)
        self.newOperationGrpRightLayout.addWidget(self.fw_Code)
        self.newOperationGrpLogoLayout.addWidget(self.logoLabel)

        self.advListLayout.addWidget(self.advList)
        self.advListLayout.addWidget(self.subProject)
        self.advListLayout.addWidget(self.searchAdvList)
        self.advListLayout.addWidget(self.createNewProject)

        self.advMainLayout.addLayout(self.advListLayout)
        self.advProject_boxes_layout.addWidget(self.advProject_info)

        self.advProject_boxes_layout.addWidget(self.adv_project_employee)
        self.advMainLayout.addLayout(self.advProject_boxes_layout)
        self.advProject_boxes_layout.addWidget(self.progressProject)

        self.advProject_info.setLayout(self.newOperationGrp)
        self.adv_project_employee.setLayout(self.adv_project_employee_Grp)
        self.setLayout(self.advMainLayout)


class backUp(QWidget):#BACKUP FILES CONTROL CENTER.
    def __init__(self, parent = None):
        super(backUp, self).__init__(parent)

        self.filterGroup = QGroupBox("Filter: ")
        self.filterGroup.setFixedSize(220, 175)
        self.folderOpGroup = QGroupBox("Connection: ")
        self.folderOpGroup.setFixedSize(220, 175)
        self.logo= QPixmap("img/recovery_icon_logo.png")
        self.logoLabel =QLabel()
        self.logoLabel.setPixmap(self.logo)
        self.infoLabel = QLabel()
        self.infoLabel.setText("You don't delete or remove \n any folder from this application.")
        self.backupLastModified = QLabel()
        self.backupLastModified.setText("Last Connection: 12-14-2018, 16:24")
        self.filterByCoordLabel = QLabel("Filter By Coordinator: ")
        self.filterByCoord = QComboBox()
        coords = ["coord1","coord2","coord3"]
        self.filterByCoord.addItems(coords)
        self.searchInList = QLineEdit()
        self.searchInList.setPlaceholderText("Find by words: ")
        self.finishedWork = QCheckBox("Finished Job(s)")
        self.suspendedWork = QCheckBox("Suspended Job(s)")
        self.awaitingJobs = QCheckBox("Awaiting Job(s)")
        self.exploreBackupFolder = QPushButton("Open in Explorer")
        self.connectBackUP = QPushButton("Connect Drive")

        self.detailSelectedProject = QTableWidget(1,6)
        self.detailSelectedProject.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)
        title = ["Project Name", "FW Code", "Coordinator", "Last Modification", "Status", "Project Type"]
        self.detailSelectedProject.setHorizontalHeaderLabels(title)
        self.filterGroupLayout = QVBoxLayout()
        self.folderOpGroupLayout = QVBoxLayout()
        self.filterGroupLayout.addWidget(self.filterByCoordLabel)
        self.filterGroupLayout.addWidget(self.filterByCoord)
        self.filterGroupLayout.addWidget(self.searchInList)
        self.filterGroupLayout.addWidget(self.finishedWork)
        self.filterGroupLayout.addWidget(self.suspendedWork)
        self.filterGroupLayout.addWidget(self.awaitingJobs)
        self.folderOpGroupLayout.addWidget(self.connectBackUP)
        self.folderOpGroupLayout.addWidget(self.exploreBackupFolder)

        self.folderOpGroupLayout.addWidget(self.backupLastModified)
        self.backupMainLayout = QHBoxLayout()
        self.listBackFilesLayout = QVBoxLayout()
        self.listBackFilesLayout.addWidget(self.logoLabel)
        self.listBackFilesLayout.addWidget(self.infoLabel)
        self.listBackFilesLayout.addWidget(self.filterGroup)
        self.listBackFilesLayout.addWidget(self.folderOpGroup)
        self.backupMainLayout.addLayout(self.listBackFilesLayout)
        self.backupMainLayout.addWidget(self.detailSelectedProject)
        self.filterGroup.setLayout(self.filterGroupLayout)
        self.folderOpGroup.setLayout(self.folderOpGroupLayout)
        self.setLayout(self.backupMainLayout)



class project_manager_main_window(QMainWindow):
    def __init__(self):
        super(project_manager_main_window, self).__init__()
        self.setCentralWidget(project_manager_central_widget())

        topMenuBar = self.menuBar()
        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("ESC")
        exitAction.triggered.connect(self.close)

        newProject = QAction("&New Project", self)
        newProject.triggered.connect(create_new_project.create_project_window)
        newProject.setShortcut("ctrl+N")

        settingsApp = QAction("&Settings", self)

        newUSer = QAction("&New User", self)
        newUSer.triggered.connect(create_new_user.start_create_project_window)

        settingUser = QAction("&User Settings", self)
        settingUser.triggered.connect(user_settings.start_user_settings)

        webSite = QAction("&Web Site", self)
        webSite.triggered.connect(self.goToSite)

        userManual = QAction("&Manual", self)
        about = QAction("&About", self)

        fileMenu = topMenuBar.addMenu("&File")
        userMenu = topMenuBar.addMenu("&Accounts")
        helpMenu = topMenuBar.addMenu("&Help")

        fileMenu.addAction(newProject)
        fileMenu.addAction(settingsApp)
        fileMenu.addAction(exitAction)

        userMenu.addAction(newUSer)
        userMenu.addAction(settingUser)

        helpMenu.addAction(webSite)
        helpMenu.addAction(userManual)
        helpMenu.addAction(about)


    def goToSite(self):
        """
        Going to 1000 Volt main web site url function!
        :return:
        """
        url = QUrl("http://1000volt.com.tr/")
        if not QDesktopServices.openUrl(url):
                QMessageBox.warning(self, 'Open Url', 'Could not open url')

def start_main_window():
    app = QApplication(sys.argv)
    project_win = project_manager_main_window()
    project_win.setWindowTitle("1000Volt: Project Manager v1.0")
    project_win.setFixedSize(1280 ,720)
    project_win.show()
    app.exec_()
start_main_window()