# package imports
from InfectionChain import InfectionChain

# external libraries which need to be installed separately
import numpy as np

# internal python libraries
from pprint import pformat


class Simulation:

    def __init__(self, _config: {str: str}):

        self._config = _config

        # we document our virus chain
        self._infection_history = []
        # we document the infection counts
        self._viruses = []

        # we assume that a person meets every friend two times per year
        # a person meets another person after 'contact_per_person'-days
        self.contact_per_person = 1.75 * round(365 / (2 * self._config['extended_circle_of_friends']))
        # representation of simulation will be printed in the terminal so it looks pretty sick
        print(self)

    # is called when user tries to print the object
    def __repr__(self) -> str:
        return '\nConfiguration of the simulation:\n' + pformat(vars(self), indent=2, width=1) + '\n'

    def simulate(self) -> (np.ndarray, np.ndarray):

        # we add the time of the duration of the infection so we let the virus die at the rest of the time
        for day in range(0, int(self._config['simulation_duration'])):
            # initiate virus
            if day % self.contact_per_person == 0:

                if day == 0:
                    self._viruses.append(
                        InfectionChain(int(day // self.contact_per_person), self._config,
                                       int(self._config['infection_count_start'])))
                else:
                    self._viruses.append(
                        InfectionChain(int(day // self.contact_per_person), self._config,
                                       self._viruses[-1].infection_count))

            for idx, virus in enumerate(self._viruses):
                virus.day_ends()
            self._infection_history.append(self.get_total_active_infections_count())

        return self.spread_infection_history(), np.array(self._viruses)

    # gibt Anzahl aller bisherigen Infektionen aufsummiert zurück
    def get_total_active_infections_count(self) -> int:
        return sum([virus.infection_count for virus in self._viruses if virus.lifetime > 0])

    # gibt Anzahl aktiver Infektionen zurück
    def get_total_infections_count(self) -> int:
        return sum([virus.infection_count for virus in self._viruses])

    # kalkuliert Inzidenz-Wert in Abhängigkeit der Bevölkerung und der aktiven Infektionszahlen
    def get_incidence_values(self) -> np.ndarray:
        return np.array([(virus.infection_count * 100000) / self._config['population'] for virus in self._viruses])

    # gibt Anzahl verstorbener Menschen zurück
    def get_mortality(self) -> int:
        return int(sum([virus.infection_count for virus in self._viruses]) * self._config['death_rate'])

    # gibt die 7-Tages-Inzidenz zurück
    def get_seven_day_incidence(self) -> int:
        return (self._viruses[-1].infection_count * 100000) / self._config['population']

    # gibt Infektionszahlen der letzten sieben Tage zurück
    def get_seven_days_total_infections_count(self) -> int:
        return self._viruses[-1].infection_count

    # verteilt die Infektionszahlen realistisch über die Tage, um keine lineare Entwicklung darzustellen
    def spread_infection_history(self) -> np.ndarray:

        spread = np.zeros(len(self._infection_history) * 7)

        for i, infection_count in enumerate(self._infection_history):
            spread[i * 7:(i + 1) * 7] = infection_count / 7

        return spread
