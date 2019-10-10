import random
from virus import Virus
from logger import Logger
random.seed(42)


class Person(object):

    def __init__(self, _id, is_vaccinated, logger, is_infected, infection=None):
        self._id = _id
        self.is_alive = True
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_infected = is_infected
        self.logger = logger

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean
        did_survive = None

        if random.random() > self.infection.mortality_rate:
            # Survives
            self.is_vaccinated = True
            self.infection = None
            self.is_infected = False
            did_survive = True
        else:
            # Dies
            self.is_infected = False
            self.infection = None
            self.is_alive = False
            did_survive = False

        self.logger.log_infection_survival(self, did_survive)

        return did_survive

    def infect(self, virus):
        self.is_infected = True
        self.infection = virus

