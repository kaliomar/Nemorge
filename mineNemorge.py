import sys,os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QAction,qApp, QApplication, QWidget, QLineEdit,\
    QPushButton,QVBoxLayout, QHBoxLayout, QLabel,QFileDialog

from zipping_module import zipit
from rename_module import renameit


class Nemorge(QWidget):
    def __init__(self):
        super(Nemorge, self).__init__()
        self.link = QLineEdit(self)
        self.link.setPlaceholderText("Go to your path...")
        self.opn = QPushButton("Open")
        self.cpr = QPushButton("Rename")
        self.rnm = QPushButton("Compress")
        self.lbl = QLabel("Clean")

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout2.addStretch()

        h_layout1.addWidget(self.link)
        h_layout1.addWidget(self.opn)
        h_layout2.addWidget(self.cpr)
        h_layout2.addWidget(self.rnm)


        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addStretch()
        v_layout.addWidget(self.lbl)

        self.opn.clicked.connect(self.opn_file)
        self.cpr.clicked.connect(self.zipping)
        self.rnm.clicked.connect(self.renaming)

        self.setLayout(v_layout)

        self.show()

    def opn_file(self):
        try:
            path = QFileDialog.getExistingDirectory(self, 'select a file', '')
            if path:
                self.link.setText(path)
                self.lbl.setText('Valid')
            else:
                self.lbl.setText('Invalid')
        except:
            pass

    def zipping(self):
        try:
            work_path = self.link.text()
            os.chdir(work_path)
            zipit()
        except:
            pass

    def renaming(self):
        try:
            work_path = self.link.text()
            os.chdir(work_path)
            renameit()
        except:
            pass


class menubar(QMainWindow):
    def __init__(self):
        super(menubar, self).__init__()
        self.setWindowIcon(QIcon('image/programIcon.png'))
        self.statusBar().showMessage('')
        self.form_widget = Nemorge()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        # make a menu bar
        bar = self.menuBar()

        # make main menus
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # make actions of menus
        new_icon = QIcon('image/new-file.png')
        new_action = QAction(new_icon,'&New',self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('new file')

        opn_icon = QIcon('image/open-file.png')
        opn_action = QAction(opn_icon,'&Open',self)
        opn_action.setShortcut('Ctrl+O')
        opn_action.setStatusTip('open a file')

        sav_icon = QIcon('image/save-file.png')
        sav_action = QAction(sav_icon,'&Save',self)
        sav_action.setShortcut('Ctrl+S')
        sav_action.setStatusTip('save current work')

        qut_icon = QIcon('image/quit.png')
        qut_action = QAction(qut_icon,'&Quit',self)
        qut_action.setShortcut('Ctrl+Q')
        qut_action.setStatusTip('quit the program')

        find_action = QAction('find...',self)
        find_action.setShortcut('Ctrl+F')
        rplc_action = QAction('replace...',self)
        rplc_action.setShortcut('Ctrl+R')

        # put actions in their menus
        file.addAction(new_action)
        file.addAction(opn_action)
        file.addAction(sav_action)
        file.addSeparator()
        file.addAction(qut_action)
        find_menu = edit.addMenu('Find')
        find_menu.addAction(find_action)
        find_menu.addAction(rplc_action)

        # actions signals and slots
        file.triggered.connect(self.respond)

        self.setWindowTitle('Nemorge')
        self.resize(600,250)

        self.show()

    def respond(self,q):
        signal = q.text()
        if signal == '&New':
            self.form_widget.clr_text()
        elif signal == '&Save':
            self.form_widget.sv_file()
        elif signal == '&Open':
            self.form_widget.opn_file()
        elif signal == '&Quit':
            qApp.quit()




app = QApplication(sys.argv)
win = menubar()
sys.exit(app.exec_())



