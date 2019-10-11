import random
import sys
from person import Person
from simulation import Simulation
from logger import Logger
from virus import Virus

random.seed(42)


def test_is_person_infected():
    virus = Virus('SmallPox', 0.7, 0.2)

    sim = Simulation(100, .5, virus, 1)
    assert sim.population == 100
    assert sim.vacc_percentage == .5
    assert sim.virus.name == 'SmallPox'
    assert sim.initial_infected == 1