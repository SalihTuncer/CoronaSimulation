# external libraries which need to be installed separately
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# internal python libraries
from shutil import copyfile


class UtilityManager:
    path: str
    new_dir: str

    def __init__(self, path: str, new_dir: str):
        self.path = path
        self.new_dir = new_dir

    def plot_data(self, _infection_history: np.ndarray, _incidence_values: np.ndarray, population: float):
        # gibt einen Plot aus in Abhängigkeit der Anzahl der Infektionen und der Inzidenz-Werte
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

    def analyze_as_data_frame(self, _virus_chain: np.ndarray):
        # formt alle Infection_Chain-Klassen in DataFrames (Tabellen) um, um sie daraufhin in .csv-Dateien zu speichern

        df = pd.DataFrame([vars(chain) for chain in _virus_chain])
        # print(df.to_string(index=False))
        df.to_csv(self.new_dir + 'virus_chain.csv')

    def save_config_file(self):
        # copy the config in the new directory so we know what parameters we used
        copyfile(self.path + '/corona_simulation.cfg', self.new_dir + 'corona_simulation.cfg')
