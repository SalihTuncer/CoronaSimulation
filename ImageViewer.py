# external imports which need to be installed
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QImage, QPixmap

# internal python libraries
import sys


class ImageViewer(QMainWindow):
    def __init__(self, x, y, width, height, file_name):
        super().__init__()

        self.imageLabel = QLabel(self)
        self.imageLabel.setScaledContents(True)
        self.setWindowTitle("Image Viewer")
        self.resize(width, height)
        self.move(x, y)

        image = QImage(file_name)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))
        self.imageLabel.setGeometry(0, 0, width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    image_1 = ImageViewer(100, 100, 800, 640,
                          '08_06_2021_16_59_00/Entwicklung_Infektionszahlen.png')
    image_2 = ImageViewer(1000, 100, 800, 640,
                          '08_06_2021_16_59_00/Entwicklung_Inzidenzwerte.png')
    image_1.show()
    image_2.show()
    sys.exit(app.exec_())
