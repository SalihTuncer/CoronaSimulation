# external imports which need to be installed
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# internal python libraries
import sys
import csv


class TableViewer(QMainWindow):
    def __init__(self, x, y, width, height, file_name):
        super().__init__()

        self.move(x, y)
        self.resize(width, height)
        self.setWindowTitle('Infection chains')

        self.model = QStandardItemModel(self)

        self.tableView = QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.resize(width, height)

        # read .csv-file in
        with open(file_name, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    list_view = TableViewer(1750, 100, 630, 950, '08_06_2021_16_59_00/virus_chain.csv')
    list_view.show()
    sys.exit(app.exec_())
