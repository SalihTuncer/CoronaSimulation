# package imports
# external libraries which need to be installed separately
import numpy as np
# internal python libraries
from pprint import pformat

from InfectionChain import InfectionChain

"""
This is the heart of the whole application. This is where the simulation happens.
"""


class Simulation:
    """
    Contact per person will be calculated depending of the extended circle of friends.

    Args:
        _config: includes all the configurations of the simulation.
    """

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

    """
    String representation of the object.
    
    If we override the __repr__-method, we can decide what will be printed.
    
    Returns:
       str.  the configuration
    """

    def __repr__(self) -> str:
        return '\nConfiguration of the simulation:\n' + pformat(vars(self), indent=2, width=1) + '\n'

    """
    Simulates every day until the time is over.
    
    Every day needs to be simulated seperately for every infection chain. So we iterate over every day and every
    chain and let a day pass with virus.day_ends(). When we create a new infection chain, we put that one into our 
    numpy array which is used like a database. At the end we return the infection history and all viruses as numpy
    arrays which can then be further processed.
    
    Returns:
        np.ndarray:  infection history.
        np.ndarray:  all virus chains.         
    """

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

    """
    Indicates how many people are infected in total.
    
    Returns:
       int.  amount infections in total.
    """

    def get_total_active_infections_count(self) -> int:
        return sum([virus.infection_count for virus in self._viruses if virus.lifetime > 0])

    """
    Indicates how many people are infected right now.
    
    Returns:
       int.  amount active infections.
    """

    def get_total_infections_count(self) -> int:
        return sum([virus.infection_count for virus in self._viruses])

    """
    Indicates the the incidence-value depending on population and active infections.
    
    Returns:
       np.ndarray.  incidence values
    """

    def get_incidence_values(self) -> np.ndarray:
        return np.array([(virus.infection_count * 100000) / self._config['population'] for virus in self._viruses])

    """
    Indicates how many people have passed away through the virus.
    
    Returns:
       int.  mortality.
    """

    def get_mortality(self) -> int:
        return int(sum([virus.infection_count for virus in self._viruses]) * self._config['death_rate'])

    """
    Indicates the 7-day incidence-value. 
    
    Returns:
        int.  incidence value.
    """

    def get_seven_day_incidence(self) -> int:
        return (self._viruses[-1].infection_count * 100000) / self._config['population']

    """
    Indicates the amount of infections in the last seven days.
    
    Returns:
        int.  amount of total infections.
    """

    def get_seven_days_total_infections_count(self) -> int:
        return self._viruses[-1].infection_count

    """
    Distributes the infection numbers realistically over the days so as not to show a linear development.
    
    Returns:
        np.ndarray.  distribution.     
    """

    def spread_infection_history(self) -> np.ndarray:

        spread = np.zeros(len(self._infection_history) * 7)

        for i, infection_count in enumerate(self._infection_history):
            spread[i * 7:(i + 1) * 7] = infection_count / 7

        return spread
