from PyQt5.QtWidgets import QMainWindow,  QDesktopWidget,  QAction, qApp
from GameVisualisation.ScriptsForForms import set_color, clickable
from PyQt5.QtGui import QIcon, QFont
from GameVisualisation.PlayingContainer import playingField
from GameVisualisation.LabelForLegend import myLabel
from GameVisualisation.InfoForm import infoForm
from GameVisualisation.SettingsForm import settingsForm
from GameFiles.Game import game
from GameFiles.FiliUtils import createXMLFile, readXMLFile

class mainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 600)
        self.center()
        set_color(self, "wheat")
        self.setWindowTitle("Game")
        self.btn = None
        self.game_started = False
        self.set_tool_bar()
        self.set_start_window()
        self.set_load_window()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def set_tool_bar(self):
        s = QIcon('resources/exit.png')
        exitAction = QAction(QIcon('GameVisualisation/resources/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        saveAction = QAction(QIcon('GameVisualisation/resources/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.save_to_file)
        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(saveAction)
        infoAction = QAction(QIcon('GameVisualisation/resources/info.png'), 'Info', self)
        infoAction.triggered.connect(self.show_info)
        infoAction.setShortcut('Ctrl+I')
        self.toolbar = self.addToolBar('Settings')
        self.toolbar.addAction(infoAction)


    def set_start_window(self):
        if self.btn is None:
            self.btn = myLabel(self)

            self.btn.set_text_color("black")
            self.btn.setFont(QFont("Times", 20, QFont.StyleItalic))
            self.btn.setText("Start new game")
            self.btn.resize(self.btn.sizeHint())
            width = self.width()
            self.btn.move(self.width() / 2 - self.btn.width() / 2, self.height() / 2 - self.btn.height() / 2)
        else:
            self.btn.setParent(None)

            self.btn = self.QLabel_my(self)
            self.btn.set_color("black")
            self.btn.setFont(QFont("Times", 20, QFont.StyleItalic))
            self.btn.setText("Start")
            self.btn.resize(self.btn.sizeHint())
            width = self.width()
            self.btn.move(self.width() / 2 - self.btn.width() / 2, self.height() / 2 - self.btn.height() / 2)
        clickable(self.btn).connect(self.start_game)

    def set_load_window(self):
        btn = myLabel(self)
        btn.set_text_color("black")
        btn.setFont(QFont("Times", 20, QFont.StyleItalic))
        btn.setText("Load game")
        btn.resize(btn.sizeHint())
        btn.move(self.width() / 2 - btn.width() / 2, self.height() / 2 - btn.height() / 2 + 40)
        clickable(btn).connect(self.load_game)

    def start_game(self):
        settingForm = settingsForm(self)
        settingForm.show()
        settingForm.difficulty_to_send[int].connect(self.set_diff_start_game)



    def load_game(self):
        args = readXMLFile("saved_game.xml")
        self.game = game(args = args)
        self.playingf = playingField(self.game)
        self.setCentralWidget(self.playingf)
        self.game_started = True


    def save_to_file(self):
        file_name = "saved_game.xml"
        createXMLFile(self.game, file_name, self)

    def show_info(self):
        infoform = infoForm(self)
        infoform.show()

    def set_diff_start_game(self, value):
        self.game = game(difficulty=value)
        self.playingf = playingField(self.game)
        self.setCentralWidget(self.playingf)
        self.game_started = True