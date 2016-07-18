
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from PyQt4 import QtGui
class Center(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.setWindowTitle("center")
        self.resize(250,150)
        self.center()
    def center (self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()#此处的geometry()首字母必须要小写，否则无法测试通过。
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
app = QtGui.QApplication(sys.argv)
qb = Center()
qb.show()
sys.exit(app.exec_())
