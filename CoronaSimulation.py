# -*- coding: utf-8 -*-

# package imports
from Simulation import Simulation
from UtilityManager import UtilityManager

if __name__ == '__main__':
    config = {}

    for line in open("corona_simulation.cfg", "r"):
        # remove spaces at the beginning and the end of the line
        line = line.strip()
        # we want to ignore the comments in the configuration-file
        if not line.startswith("#"):
            setting = line.split('=')
            config[setting[0].strip()] = float(setting[1])

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

    utils = UtilityManager()
    # save plot as file
    utils.plot_data(infection_history, incidence_values, config['population'])
    # convert all InfectionChains to a DataFrame and save it as a a .csv-file
    utils.analyze_as_data_frame(virus_chain)
    # save the config-file in the new directory, so we know what parameters we used
    utils.save_config_file()
