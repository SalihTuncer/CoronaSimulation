# package imports
from Simulation import Simulation
from UtilityManager import UtilityManager

# external python libraries
from PyQt5.QtWidgets import QMainWindow

# internal python libraries
from datetime import datetime
import os


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
