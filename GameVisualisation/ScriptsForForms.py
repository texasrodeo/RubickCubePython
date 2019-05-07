
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QEvent, pyqtSignal, QObject



def set_color(self, color):
    self.setAutoFillBackground(True)
    appearance = self.palette()
    appearance.setColor(QPalette.Normal, QPalette.Window, QColor(color))
    self.setPalette(appearance)
    self.color = color

def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:

                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                    return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked