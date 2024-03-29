from stats import Stats

class Logger(object):

    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    def __init__(self, file_name, stats):
        self.file_name = file_name
        self.stats = stats

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        f = open(self.file_name, "w+")

        f.write("Population Size\tPercent Vaccinated\tVirus Name\tMortality Rate\tRepro Rate\n")
        f.write("{}\t{}\t{}\t{}\t{}\n".format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))
        f.write("--------------------------------------------------------------------------------------------------\n")

        f.close()

    def log_interaction(self, person, random_person, random_person_sick=None, random_person_vacc=None, did_infect=None):
        f = open(self.file_name, "a+")

        if did_infect:
            f.write("{} infects {}\n".format(person._id, random_person._id))
        elif random_person_sick:
            f.write("{} did not infect {} because {} is already sick\n".format(person._id, random_person._id, random_person._id))
        elif random_person_vacc:
            f.write("{} did not infect {} because {} is vaccinated\n".format(person._id, random_person._id, random_person._id))
        else:
            f.write("{} did not infect {} because {} got lucky\n".format(person._id, random_person._id, random_person._id))

        f.close()

    def log_infection_survival(self, person, did_survive):
        f = open(self.file_name, "a+")

        if did_survive:
            f.write("{} survived the infection and is now vaccinated\n".format(person._id))
            self.stats.increment_saved_by_vaccination()
        else:
            f.write("{} died from infection\n".format(person._id))
            self.stats.increment_death_num()

        f.close()

    def log_time_step(self, time_step_number):
        f = open(self.file_name, "a+")

        f.write("Time step {} ended, beginning {}\n".format(time_step_number, time_step_number + 1))

        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.
        '''

        f.close()

    def log_input_string(self, input_string):
        f = open(self.file_name, 'a+')
        f.write(input_string + "\n")
        f.close()

def test_logger_initialization():
    file_name = 'log_test.txt'
    logger = Logger(file_name)
    assert logger.file_name == 'log_test.txt'

def test_write_metadata():
    file_name = 'log_test.txt'
    logger = Logger(file_name)
    f = open(file_name, 'r')

    logger.write_metadata(100, 0.1, 'Smallpox', 0.5, 0.5)

    lines = f.readlines()
    f.close()

    assert lines[1] == '100\t0.1\tSmallpox\t0.5\t0.5\n'


def test_log_interaction():
    file_name = 'log_test.txt'
    logger = Logger(file_name)

    f = open(file_name, 'r')

    logger.log_interaction()

def test_log_infection_survival():
    file_name = 'log_test.txt'
    logger = Logger(file_name)

    f = open(file_name, 'r')

    logger.log_interaction(1, None)

    lines = f.readlines()
    f.close()

    assert lines

def test_log_time_step():
    file_name = 'log_test.txt'
    logger = Logger(file_name)

    f = open(file_name, 'r')

    logger.log_time_step(0)

    lines = f.readlines()
    f.close()
    assert lines[20] == 'Time step 0 ended, beginning 1'
