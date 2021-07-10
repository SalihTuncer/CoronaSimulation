# package imports
import os
# external python libraries
from PyQt5.QtWidgets import QMainWindow
# internal python libraries
from datetime import datetime

from Simulation import Simulation
from UtilityManager import UtilityManager

"""
This is where the application is started.

The Simulation will be started with the configurations, a directory will be created in the current path where the
application is started and the results will be added to the directory. If the application is in the GUI mode, it will
show the results in a specific GUI. Otherwise the results will be just added to the directory. This depends on the mode.

Args:
    config: includes all the configurations of the simulation.
    config_viewer: GUI for the configuration.
    --mode: gui starts a GUI | cmd starts a command line tool
"""


def main(config: {str: str}, config_viewer: QMainWindow = None):
    gui = False
    if config_viewer:
        config_viewer.hide()
        gui = True

    simulation = Simulation(config)

    infection_history, virus_chain = simulation.simulate()
    # calculate inzidenz values
    incidence_values = simulation.get_incidence_values()

    # current path
    path = os.getcwd()
    # use time as unique folder name
    time_right_now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    new_dir = path + '/' + time_right_now + '/'
    # create directory
    os.mkdir(new_dir)

    utils = UtilityManager(path, new_dir)
    # save plot as file
    utils.plot_data(infection_history, incidence_values, config['population'])
    # convert all InfectionChains to a DataFrame and save it as a a .csv-file
    utils.analyze_as_data_frame(virus_chain)
    # save the config-file in the new directory, so we know what parameters we used
    utils.save_config_file()

    if gui:
        config_viewer.results.add_plots_and_table(new_dir)
        config_viewer.results.add_labels(simulation, config['population'])
