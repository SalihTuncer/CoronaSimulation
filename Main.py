# package imports

import os
# internal python libraries
from datetime import datetime

from Simulation import Simulation
from UtilityManager import UtilityManager


def main(config: {str: str}, config_viewer=None):
    gui = False
    if config_viewer:
        config_viewer.hide()
        gui = True

    simulation = Simulation(config)

    infection_history, virus_chain = simulation.simulate()
    # calculate inzidenz values
    incidence_values = simulation.get_incidence_values()
    # TODO: plot 7-day incidence value and total infections in the last seven days
    print(f'7-day incidence value: {simulation.get_seven_day_incidence():.2f}')
    print(f'total infections in the last 7 days: {simulation.get_seven_days_total_infections_count()}')
    print(f'total infections: {simulation.get_total_infections_count()}')
    print(f'mortality: {simulation.get_mortality()}')
    immunity_rate = (
            simulation.get_total_infections_count() / (config['population'] - simulation.get_mortality()) * 100)
    print(f'percentage immunity of population: {immunity_rate:.2f}%')

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
        config_viewer.results.add_values(new_dir)
