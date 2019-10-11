import random
from virus import Virus
from logger import Logger
from person import Person
random.seed(42)

''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    # virus = Virus("Dysentery", 0.7, 0.2)
    
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
    assert person.is_vaccinated is False
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
    assert person.infection is None
    assert person.is_alive is True


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    logger = Logger('log_test.txt')
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, logger, None, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person.is_alive is True
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        # assert ...
        assert person.is_vaccinated is True
        assert person.is_infected is False
    else:
        assert person.is_alive is False
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert ...
        assert person.is_vaccinated is False
        assert person.is_infected is virus
