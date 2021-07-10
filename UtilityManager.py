# external libraries which need to be installed separately
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# internal python libraries
from shutil import copyfile

"""
This class is responsible for plotting data, saving dataFrames and copying config-files.
"""


class UtilityManager:
    path: str
    new_dir: str

    """
    The arguments are needed later on in the methods. 
    
    Args:
        path: total path of application.
        new_dir: directory name where files will be saved/copied.
    """

    def __init__(self, path: str, new_dir: str):
        self.path = path
        self.new_dir = new_dir

    """
    Outputs a plot depending on the number of infections and the incidence values.
    
    Args:
        _infection_history: development of the virus chains
        _incidence_values: development of the incidence values 
        population: total population
    """

    def plot_data(self, _infection_history: np.ndarray, _incidence_values: np.ndarray, population: float):
        x_infection = np.arange(len(_infection_history))
        x_infection = x_infection // 7

        x_incidence = np.arange(len(_incidence_values))
        x_incidence = x_incidence * 7

        plt.subplots()
        plt.plot(x_infection, _infection_history, marker='.', label='Infektionszahlen')
        plt.xlabel('Tage')
        plt.ylabel('Anzahl Infektionen')
        plt.title(f'Entwicklung der Infektionszahlen bei einer Population von {int(population):,d}')
        plt.savefig(self.new_dir + 'Entwicklung_Infektionszahlen.png')
        plt.subplots()
        plt.plot(x_incidence, _incidence_values, marker='.', label='Inzidenzwerte')
        plt.title(f'Entwicklung der Inzidenzwerte bei einer Population von {int(population):,d}')
        plt.ylabel('Inzidenzwert')
        plt.xlabel('Tage')
        plt.savefig(self.new_dir + 'Entwicklung_Inzidenzwerte.png')

    """
    Forms all InfectionChain classes into DataFrames (tables) in order to then save them in .csv files.
    
    Args:
        _virus_chain: includes all virus chains as objects
    """

    def analyze_as_data_frame(self, _virus_chain: np.ndarray):
        #
        df = pd.DataFrame([vars(chain) for chain in _virus_chain])
        # print(df.to_string(index=False))
        df.to_csv(self.new_dir + 'virus_chain.csv')

    """
    Copies the config-file in the new directory so we know what parameters we have used.
    """

    def save_config_file(self):
        copyfile(self.path + '/corona_simulation.cfg', self.new_dir + 'corona_simulation.cfg')
