# external imports which need to be installed
from PyQt5.QtWidgets import QWidget, QLabel, QTableView
from PyQt5.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem

# internal python libraries
import csv


class ResultsGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulation results")
        self.move(500, 100)
        self.resize(1600, 1200)

    def add_values(self, dir_name):
        self.dir_name = dir_name

        self.add_image('Entwicklung_Infektionszahlen.png', 25, 50, height=500)
        self.add_image('Entwicklung_Inzidenzwerte.png', 25, 640, height=500)

        self.add_csv_as_table('virus_chain.csv', 900, 120)
        # header for the table
        table_label = QLabel(self)
        table_label.move(1175, 75)
        table_label.resize(300, 30)
        table_label.setText('Infektionsketten')

        self.show()

    def add_image(self, file_name, x, y, width=800, height=640):
        image_label = QLabel(self)
        image_label.setScaledContents(True)
        image = QImage(self.dir_name + file_name)
        image_label.setPixmap(QPixmap.fromImage(image))
        image_label.setGeometry(x, y, width, height)

    def add_csv_as_table(self, file_name, x, y, width=630, height=950):
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
