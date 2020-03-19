from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog
from PyQt5.QtGui import QPixmap
import sys
from PIL.ImageQt import ImageQt
from PIL import Image
from design import Ui_Form as Design
from random import randint


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        count = QInputDialog.getInt(self, 'Form', 'Количество цветов:', 1, 1, 99)[0]
        alls = []
        for i in range(count):
            alls.append(QLabel())
            image = Image.new("RGBA", (906, 655 // count), (randint(0, 255), randint(0, 255), randint(0, 255), 255))
            alls[-1].setPixmap(QPixmap.fromImage(ImageQt(image)))
            self.gridLayout.addWidget(alls[-1], i, 0, 1, 1)


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())