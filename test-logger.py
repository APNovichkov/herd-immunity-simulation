import random
from virus import Virus
from logger import Logger
from person import Person
random.seed(42)

def test_logger_initialization():
    file_name = 'log_test.txt'
    logger = Logger(file_name)
    assert logger.file_name is 'log_test.txt'

def test_write_metadata():
    file_name = 'log_test.txt'
    logger = Logger(file_name)
    f = open(file_name, 'r')

    logger.write_metadata(100, 0.1, "Smallpox", 0.5, 0.5)

    lines = f.readlines()
    f.close()

    assert lines[1] == "100\t0.1\tSmallpox\t0.5\t0.5\n"


def test_log_interaction():
    file_name = 'log_test.txt'
    logger = Logger(file_name)

    person = Person(1,True,None,None)
    random_person = Person(2,True,None,None)

    f = open(file_name, 'r')

    logger.log_interaction(person,random_person,1,1,True)

    lines = f.readlines()
    f.close()

    assert lines[3] == "1 infects 2\n"

def test_log_infection_survival():
    file_name = 'log_test.txt'
    logger = Logger(file_name)
    person = Person(1,True,None,None)

    f = open(file_name, 'r')

    logger.log_infection_survival(person,True)

    lines = f.readlines()
    f.close()

    assert lines[4] == "1 survived the infection and is now vaccinated\n"

def test_log_time_step():
    file_name = 'log_test.txt'
    logger = Logger(file_name)

    f = open(file_name, 'r')

    logger.log_time_step(0)

    lines = f.readlines()
    f.close()
    assert lines[5] == "Time step 0 ended, beginning 1\n"