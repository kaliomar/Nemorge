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
        self.cpr = QPushButton("Compress")
        self.rnm = QPushButton("Rename")
        self.lbl1 = QLabel("Clean")
        self.lbl2 = QLabel(" ")

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout2.addStretch()
        h_layout3 = QHBoxLayout()

        h_layout1.addWidget(self.link)
        h_layout1.addWidget(self.opn)
        h_layout2.addWidget(self.rnm)
        h_layout2.addWidget(self.cpr)
        h_layout3.addWidget(self.lbl2)

        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addStretch()
        v_layout.addWidget(self.lbl1)

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
                self.lbl1.setText('Valid')
            else:
                self.lbl1.setText('Invalid')
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
        run = bar.addMenu('Run')

        # make actions of menus
        opn_icon = QIcon('image/open-file.png')
        opn_action = QAction(opn_icon,'&Open',self)
        opn_action.setShortcut('Ctrl+O')
        opn_action.setStatusTip('open a file')

        qut_icon = QIcon('image/quit.png')
        qut_action = QAction(qut_icon,'&Quit',self)
        qut_action.setShortcut('Ctrl+Q')
        qut_action.setStatusTip('quit the program')

        cpy_icon = QIcon('image/copy.png')
        cpy_action = QAction(cpy_icon, '&Copy',self)
        cpy_action.setShortcut('Ctrl+C')
        cpy_action.setStatusTip('copy current selected')

        cut_icon = QIcon('image/cut.png')
        cut_action = QAction(cut_icon, '&Cut',self)
        cut_action.setShortcut('Ctrl+X')
        cut_action.setStatusTip('cut current selected')

        pst_icon = QIcon('image/paste.png')
        pst_action = QAction(pst_icon, '&Paste',self)
        pst_action.setShortcut('Ctrl+V')
        pst_action.setStatusTip('paste from clipboard')

        comp_icon = QIcon('image/comp.png')
        comp_action = QAction(comp_icon, '&Compress',self)
        comp_action.setShortcut('Ctrl+R')
        comp_action.setStatusTip('Compress all uncompressed folders')

        renm_icon = QIcon('image/renm.png')
        renm_action = QAction(renm_icon,'&Rename',self)
        renm_action.setShortcut('Ctrl+N')
        renm_action.setStatusTip('Rename all folders and files')

        # put actions in their menus
        file.addAction(opn_action)
        file.addSeparator()
        file.addAction(qut_action)
        edit.addAction(cpy_action)
        edit.addAction(cut_action)
        edit.addAction(pst_action)
        run.addAction(comp_action)
        run.addAction(renm_action)


        # actions signals and slots
        file.triggered.connect(self.file_respond)
        edit.triggered.connect(self.edit_respond)
        run.triggered.connect(self.run_respond)


        self.setWindowTitle('Nemorge')
        self.resize(450,250)

        self.show()

    def file_respond(self,q):
        signal = q.text()
        if signal == '&Open':
            self.form_widget.opn_file()
        elif signal == '&Quit':
            qApp.quit()

    def edit_respond(self,q):
        signal = q.text()
        var = self.form_widget.link.text()
        if signal == '&Copy':
            qApp.clipboard().setText(var)
        elif signal == '&Cut':
            qApp.clipboard().setText(var)
            self.form_widget.link.clear()
        elif signal == '&Paste':
            self.form_widget.link.setText(qApp.clipboard().text())

    def run_respond(self,q):
        signal = q.text()
        if signal == '&Compress':
            self.form_widget.zipping()
        elif signal == '&Rename':
            self.form_widget.renaming()


app = QApplication(sys.argv)
win = menubar()
sys.exit(app.exec_())



