import sys
import os
from PySide import QtGui
from PySide.QtCore import *
from PySide.QtGui import *

class WorkSpaceUtility(QtGui.QWidget):

    def __init__(self):
        super(WorkSpaceUtility, self).__init__()

        self.initUI()

    def initUI(self):

        # Treelist View
        self.tvFolders = QtGui.QTreeWidget(self)
        self.tvFolders.setHeaderLabel('Folders')
        self.tvFolders.setSortingEnabled(True)
        self.tvFolders.resize(300,300)
        self.tvFolders.move(0,0)

        # Add TEMP folders for testing
        self.addItem('Audio', self.tvFolders.invisibleRootItem())
        item = self.addItem('Workspaces', self.tvFolders.invisibleRootItem())
        self.addItem('0010', item)
        vid = self.addItem('Video', self.tvFolders.invisibleRootItem())
        self.addItem('0020', vid)
        self.addItem('0010', vid)
        shot = self.addItem('0050', vid)
        self.addItem('0050_10', shot)
        asset = self.addItem('0050_20', shot)
        self.addItem('donuts', asset)
        self.addItem('0050_30', shot)
        self.addItem('0040', vid)

        # Print Treeview
        bnPrintInfo = QtGui.QPushButton('Print Info', self)
        bnPrintInfo.resize(280,40)
        bnPrintInfo.move(10, 310)
        bnPrintInfo.clicked.connect(self.PrintInfo)

        self.resize(300, 360)
        self.center()

        self.setWindowTitle('Workspace Utility')
        self.show()

    def PrintInfo(self):
        count = self.tvFolders.topLevelItemCount()

        for x in xrange(count):
            name = self.tvFolders.invisibleRootItem().child(x).text(0)
            childcnt = self.tvFolders.invisibleRootItem().child(x).childCount()

            print name,childcnt
        # print var

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addItem(self, name, parent):
        self.tvFolders.expandItem(parent)
        item = QTreeWidgetItem(parent)
        item.setText(0, name)
        #It is important to set the Flag Qt.ItemIsEditable
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled | Qt.ItemIsEditable)

        item.setIcon(0,self.style().standardIcon(QStyle.SP_DirIcon))
        return item

def main():

    app = QtGui.QApplication(sys.argv)
    ex = WorkSpaceUtility()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()