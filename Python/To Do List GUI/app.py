from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window import Ui_MainWindow
from new_task import Ui_Dialog


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.add_new_task)
        self.done = []
        self.scheduled = []
        self.pushButton.clicked.connect(self.do_task)
        self.pushButton_2.clicked.connect(self.schedule_task)

    def do_task(self):
        task = self.listWidget.takeItem(self.listWidget.currentRow())
        if bool(task) != False:
            self.listWidget_2.addItem(task.text())

    def schedule_task(self):
        task = self.listWidget_2.takeItem(self.listWidget_2.currentRow())
        if bool(task) != False:
            self.listWidget.addItem(task.text())

    def add_task(self, task):
        if bool(task) == True:
            self.listWidget.addItem(task)

    def add_new_task(self):
        dlg = Dialog()
        dlg.ui.buttonBox.accepted.connect(
            lambda: self.add_task(dlg.ui.new_task_input.text())
        )
        dlg.exec()



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
