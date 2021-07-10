# package imports
import Main
# external imports which need to be installed
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton

from ResultsGUI import ResultsGUI

"""
GUI with options which can be adjusted. 

This class is the main window of the GUI application. Here you can change the configurations
of the simulation which otherwise would have had to be changed by the config-file. This saves
time and is user-friendly.

Args: 
    QMainWindow: inherits all the functions from the library-object.
"""


class ConfigGUI(QMainWindow):
    """
    Initializes the GUI with default values, labels and buttons.

    The configuration decides what the default values of the GUI will be.
    """

    def __init__(self):
        super().__init__()

        self.results = ResultsGUI()
        self.results.hide()

        self.setGeometry(600, 300, 640, 480)
        self.setWindowTitle('Corona Simulator')

        self.default_config = {'incubation_period': 5,
                               'duration_of_infection': 14,
                               'death_rate': 0.0275,
                               'extended_circle_of_friends': 42,
                               'simulation_duration': 200,
                               'infection_count_start': 8,
                               'population': 80000000,
                               'window_width': 1000
                               }

        self.input_config = {}

        y_pos = 60

        self.labels = []
        self.inputs = []
        # initialize Labels  and LineEdits
        for _ in range(len(self.default_config)):
            self.labels.append(QLabel(self))
            self.labels[-1].move(70, y_pos)
            self.labels[-1].resize(300, 30)

            self.inputs.append(QLineEdit(self))
            self.inputs[-1].move(350, y_pos)
            self.inputs[-1].resize(150, 30)
            print(self.inputs[-1].text())
            y_pos += 40

        self.fill_text()

        start_sim = QPushButton('start simulation', self)
        start_sim.move(320, y_pos + 40)
        start_sim.resize(200, 30)
        start_sim.clicked.connect(self.on_click)

        default = QPushButton('default settings', self)
        default.move(100, y_pos + 40)
        default.resize(170, 30)
        default.clicked.connect(self.fill_text)

    '''
    Fills the empty labels and inputs with the values of the configuration.
    '''

    def fill_text(self):
        for i, (key, value) in enumerate(self.default_config.items()):
            self.labels[i].setText(key)
            self.inputs[i].setText(str(value))

    '''
    Starts the simulation with the values in the input-fields.
    '''

    def on_click(self):
        for i in range(len(self.labels)):
            self.input_config[self.labels[i].text()] = float(self.inputs[i].text())
        self.results.set_window_size(self.input_config['window_width'])
        Main.main(self.input_config, self)
