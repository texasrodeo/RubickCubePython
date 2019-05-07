from GameVisualisation.MainForm import mainForm
from PyQt5.Qt import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainf = mainForm()
    mainf.show()
    sys.exit(app.exec())