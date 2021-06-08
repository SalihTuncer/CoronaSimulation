# external imports which need to be installed
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QImage, QPixmap


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
