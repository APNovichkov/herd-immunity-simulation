import random
from virus import Virus
from logger import Logger
random.seed(42)


class Person(object):

    def __init__(self, _id, is_vaccinated, logger, is_infected, infection=None):
        self._id = _id
        self.is_alive = True
        self.is_vaccinated = None
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


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True, None, None)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False, None, None)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person._id == 2
    assert person.is_vaccinated is None
    assert person.infection is None
    assert person.is_alive is True


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, None, virus)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...

    assert person._id == 3
    assert person.is_vaccinated is False
    assert person.infection is virus
    assert person.is_alive is True


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, None, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person.is_alive is True
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        # assert ...
        assert person.is_vaccinated is True
        assert person.is_infected is None
    else:
        assert person.is_alive is False
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert ...
        assert person.is_vaccinated is False
        assert person.is_infected is virus
