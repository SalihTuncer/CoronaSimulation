# external libraries which need to be installed separately
import numpy as np

# internal python libraries
from pprint import pformat


# Namen von Virus zu Infection_Chain umgeändert
class InfectionChain:
    # total number of viruses active in the chain
    infection_count: int
    # while this time, the virus chain is inactive
    incubation_time: int
    # whether the virus already has propagated
    propagated: bool

    def __init__(self, creation_date: int, _config, infection_count_start: int):
        self.id = creation_date
        self.lifetime = int(_config['duration_of_infection'])
        self.infection_count = infection_count_start
        self.incubation_time = _config['incubation_period']
        self.propagated = False

    def __repr__(self):
        return '\nConfiguration of the virus:\n' + pformat(vars(self), indent=2, width=1) + '\n'

    def day_ends(self):
        if self.incubation_time > 0:
            self.incubation_time -= 1
        # while incubation the virus will be inactive
        if not self.is_incubating() and self.lifetime > 0:
            if not self.is_propagated():
                self.propagate()
            self.lifetime -= 1

    # Infektionskette wird erst beachtet und simuliert, sobald die Inkubationszeit vorbei ist
    def propagate(self):
        self.infection_count = int(self.infection_count * np.random.uniform(1.25, 1.45, 1)[0])
        self.propagated = True

    def is_incubating(self):
        return self.incubation_time > 0

    def is_vanished(self):
        return self.lifetime == 0

    def is_propagated(self):
        return self.propagated
