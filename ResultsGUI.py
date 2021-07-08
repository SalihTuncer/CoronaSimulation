# external imports which need to be installed
from PyQt5.QtWidgets import QWidget, QLabel, QTableView
from PyQt5.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem

# internal python libraries
import csv


class ResultsGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation results")

    def set_window_size(self, x):
        self.x = x
        self.y = round(self.x * (3 / 4))
        self.move(round(self.x * (5 / 16)), round(self.y * (1 / 12)))
        self.resize(self.x, self.y)

    def add_values(self, dir_name):
        self.dir_name = dir_name

        self.add_image('Entwicklung_Infektionszahlen.png', round(self.x * (1 / 64)), round(self.y * (1 / 24)))
        self.add_image('Entwicklung_Inzidenzwerte.png', round(self.x * (1 / 64)), round(self.y * (8 / 15)))

        self.add_csv_as_table('virus_chain.csv', round(self.x * (9 / 16)), round(self.y * (1 / 10)))
        # header for the table
        table_label = QLabel(self)
        table_label.move(round(self.x * (47 / 64)), round(self.y * (1 / 16)))
        table_label.resize(round(self.x * (3 / 16)), round(self.y * (3 / 160)))
        table_label.setText('Infektionsketten')

        self.show()

    def add_image(self, file_name, x, y):
        width = round(self.x * (1 / 2))
        height = round(self.y * (5 / 12))
        image_label = QLabel(self)
        image_label.setScaledContents(True)
        image = QImage(self.dir_name + file_name)
        image_label.setPixmap(QPixmap.fromImage(image))
        image_label.setGeometry(x, y, width, height)

    def add_csv_as_table(self, file_name, x, y):
        # TODO: ignore first column of the .csv-file
        width = round(self.x * (63 / 160))
        height = round(self.y * (10 / 12))
        model = QStandardItemModel(self)
        table_view = QTableView(self)
        table_view.setModel(model)
        table_view.horizontalHeader().setStretchLastSection(True)
        table_view.resize(width, height)
        table_view.move(x, y)

        # read .csv-file in
        with open(self.dir_name + file_name, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QStandardItem(field)
                    for field in row
                ]
                model.appendRow(items)
