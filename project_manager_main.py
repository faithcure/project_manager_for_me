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