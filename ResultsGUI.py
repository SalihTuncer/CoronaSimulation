# package imports
# internal python libraries
import csv
# external imports which need to be installed
from PyQt5.QtWidgets import QWidget, QLabel, QTableView
from PyQt5.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem

from Simulation import Simulation

"""
GUI which shows all the results of the simulation.

This class is technically a widget so it is a part of the QMainWindow. It includes two plots with the amount of
infections and the incidence values. Furthermore it is shown a table with the history of all virus chains. This can 
be helpful for deeper analyzes. Under the table are additional information like the actual incidence value, infections
in the last seven days, all infections, mortality and the percent immunity of the population.  
"""


class ResultsGUI(QWidget):
    """
    Only sets the title of the results window.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulation results")

    """
    Sets the window size depending on the width given from the config.  
    
    One of the special features of the GUI is the fitting of the window size. Every part of the GUI is given 
    in percentages depending on the x-coordinate or the y-coordinate. This leads to a dynamic resolution which 
    can be chosen from the user in the configurations.
    
    Args:
        x: window width.
    """

    def set_window_size(self, x: float):
        self.x = x
        self.y = round(self.x * (3 / 4))
        self.move(round(self.x * (5 / 16)), round(self.y * (1 / 12)))
        self.resize(self.x, self.y)

    """
    Plots and Tables are added to the GUI.
    
    On the left top the evolution of the cases will be shown. Below of it are the incidence values. On the right top 
    is the table with the history of the virus chains and below of it are the additional information.
    
    Args:
        dir_name: directory name which include the plots as .png-files.
    """

    def add_plots_and_table(self, dir_name: str):
        self.dir_name = dir_name

        self.add_image('Entwicklung_Infektionszahlen.png', round(self.x * (1 / 64)), round(self.y * (1 / 24)))
        self.add_image('Entwicklung_Inzidenzwerte.png', round(self.x * (1 / 64)), round(self.y * (8 / 15)))

        self.add_csv_as_table('virus_chain.csv', round(self.x * (9 / 16)), round(self.y * (1 / 10)))

    """
    Here the different text labels are added to the GUI. The variable names tell us already what information they
    include.
    
    Args:
        simulation: simulation class which include the information we need to show.
        population: amount of total population.
    """

    def add_labels(self, simulation: Simulation, population: float):
        # header for the table
        table_label = QLabel(self)
        table_label.move(round(self.x * (47 / 64)), round(self.y * (1 / 16)))
        table_label.resize(round(self.x * (3 / 16)), round(self.y * (3 / 160)))
        table_label.setText('Infektionsketten')

        info_label = QLabel(self)
        info_label.move(round(self.x * (45 / 64)), round(self.y * (9 / 16)))
        info_label.resize(round(self.x * (3 / 16)), round(self.y * (15 / 160)))
        info_label.setText('Additional information')

        incidence_label = QLabel(self)
        incidence_label.move(round(self.x * (36 / 64)), round(self.y * (10 / 16)))
        incidence_label.resize(round(self.x * (5 / 16)), round(self.y * (15 / 160)))
        incidence_label.setText(f'7-day incidence value: {simulation.get_seven_day_incidence():.2f}')

        infections_7_label = QLabel(self)
        infections_7_label.move(round(self.x * (36 / 64)), round(self.y * (11 / 16)))
        infections_7_label.resize(round(self.x * (5 / 16)), round(self.y * (15 / 160)))
        infections_7_label.setText(
            f'total infections in the last 7 days: {simulation.get_seven_days_total_infections_count()}')

        total_infections_label = QLabel(self)
        total_infections_label.move(round(self.x * (36 / 64)), round(self.y * (12 / 16)))
        total_infections_label.resize(round(self.x * (5 / 16)), round(self.y * (15 / 160)))
        total_infections_label.setText(f'total infections: {simulation.get_total_infections_count()}')

        mortality_label = QLabel(self)
        mortality_label.move(round(self.x * (36 / 64)), round(self.y * (13 / 16)))
        mortality_label.resize(round(self.x * (5 / 16)), round(self.y * (15 / 160)))
        mortality_label.setText(f'mortality: {simulation.get_mortality()}')

        immunity_rate = (
                simulation.get_total_infections_count() / (population - simulation.get_mortality()) * 100)

        immunity_label = QLabel(self)
        immunity_label.move(round(self.x * (36 / 64)), round(self.y * (14 / 16)))
        immunity_label.resize(round(self.x * (5 / 16)), round(self.y * (15 / 160)))
        immunity_label.setText(f'percentage immunity of population: {immunity_rate:.2f}%')

        self.show()

    """
        Adds an image depending on the name to the GUI at specific coordinates.
        
        Args:
            file_name: name of the plot.
            x: x-coordinate
            y: y-coordinate 
    """

    def add_image(self, file_name: str, x: float, y: float):
        width = round(self.x * (1 / 2))
        height = round(self.y * (5 / 12))
        image_label = QLabel(self)
        image_label.setScaledContents(True)
        image = QImage(self.dir_name + file_name)
        image_label.setPixmap(QPixmap.fromImage(image))
        image_label.setGeometry(x, y, width, height)

    """
        Adds a table depending on the name to the GUI at a specific coordinates.
        
        Args:
            file_name: name of the plot.
            x: x-coordinate
            y: y-coordinate 
    """

    def add_csv_as_table(self, file_name: str, x: float, y: float):
        # TODO: ignore first column of the .csv-file
        width = round(self.x * (63 / 160))
        height = round(self.y * (5 / 12))
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
