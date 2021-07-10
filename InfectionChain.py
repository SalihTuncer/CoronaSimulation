# external libraries which need to be installed separately
import numpy as np

# internal python libraries
from pprint import pformat


class InfectionChain:
    # total number of viruses active in the chain
    infection_count: int
    # while this time, the virus chain is inactive
    incubation_time: int
    # whether the virus already has propagated
    propagated: bool

    """
    Creates an infection chain which will be grow with time appropriately.
    
    Every infection chain has its unique id. The amount of infected people from the chain depends on the chains before.
    The incubation time is a time limit where the virus can not spread. Only when this time has passed, the virus 
    can start to spread.
    
    Args:
        creation_date:  unique id so the chain can be traced back.
        _config: dictionary with all the configurations for the simulation.
        infection_count_start: amount of infected people when this chain has started.
    """

    def __init__(self, creation_date: int, _config: {str: str}, infection_count_start: int):
        self.id = creation_date
        self.lifetime = int(_config['duration_of_infection'])
        self.infection_count = infection_count_start
        self.incubation_time = _config['incubation_period']
        self.propagated = False

    """
    String representation of the object.
    
    Every python object, like in every other programming language too, can be printed. If we override the __repr__-
    method, we can decide what will be printed. That is what we did here. We print the whole configuration of the 
    infection chain which is not just pretty helpful for debugging, but also for representations in the command line.
    
    Returns:
       str.  the configuration
    """

    def __repr__(self) -> str:
        return '\nConfiguration of the virus:\n' + pformat(vars(self), indent=2, width=1) + '\n'

    """
    When one day in the simulation passes, this method is called.
    
    As long as incubation time is not passed, the virus chain can not propagate. If the chain has propagated, it is
    listed in the statistics, but has a limited lifetime. After the lifetime has passed, the chain is not listed
    anymore.
    """

    def day_ends(self):
        if self.incubation_time > 0:
            self.incubation_time -= 1
        # while incubation the virus will be inactive
        if not self.is_incubating() and self.lifetime > 0:
            if not self.is_propagated():
                self.propagate()
            self.lifetime -= 1

    """
    Propagation of the virus chain.
    
    The propagation is done here with a bit of randomness. This values are found out after a lot of experiments. 
    """

    def propagate(self):
        self.infection_count = int(self.infection_count * np.random.uniform(1.25, 1.45, 1)[0])
        self.propagated = True

    """
    Indicates whether the incubation time has passed or not.
    
    Returns:
       bool.  state of incubation
    """

    def is_incubating(self) -> bool:
        return self.incubation_time > 0

    """
    Indicates whether the lifetime of the virus chain is over.
    
    Returns:
       bool.  state of lifetime
    """

    def is_vanished(self) -> bool:
        return self.lifetime == 0

    """
    Indicates whether the virus chain has propagated or not.

    Returns:
       bool.  state of propagation
    """

    def is_propagated(self) -> bool:
        return self.propagated
