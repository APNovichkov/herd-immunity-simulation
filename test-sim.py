import random
import sys
from person import Person
from simulation import Simulation
from logger import Logger
from virus import Virus

random.seed(42)



def test_init():
    virus = Virus("SmallPox", 0.5, 0.5)

    sim = Simulation(100, 0.5, 10, virus)

    assert sim.population_size == 100
    assert sim.percent_vaccinated == 0.5
    assert sim.num_initial_infected == 10

def test_simulation_should_continue():
    virus = Virus("SmallPox", .5, .5)
    
    sim = Simulation(100, 0.5, 10, virus)
    
    person1 = Person(1, True, None, False)
    person2 = Person(2, False, None, True)

    sim.population = [person1, person2]

    assert sim.simulation_should_continue() is True

def test_is_person_infected():
    virus = Virus("SmallPox", 0.5, 0.5)

    person = Person(1,False,None,True)

    sim = Simulation(100, 0.5, 10, virus)

    assert sim.is_person_infected(person) is not None 
