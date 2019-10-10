class Logger(object):

    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    def __init__(self, file_name):
        self.file_name = file_name

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
        else:
            f.write("{} died from infection\n".format(person._id))

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

def test_logger_initialization(self):
    file_name = 'Smallpox_simulation_pop_30_vp_0.5_infected_1.txt'
    logger = Logger(file_name)
    assert logger.file_name == 'Smallpox_simulation_pop_30_vp_0.5_infected_1.txt'

def test_write_metadata(self):
    file_name = 'Smallpox_simulation_pop_30_vp_0.5_infected_1.txt'
    logger = Logger(file_name)


def test_log_interaction(self):
    file_name = 'Smallpox_simulation_pop_30_vp_0.5_infected_1.txt'
    logger = Logger(file_name)

def test_log_infection_survival(self):
    file_name = 'Smallpox_simulation_pop_30_vp_0.5_infected_1.txt'
    logger = Logger(file_name)

def test_log_time_step(self):
    file_name = 'Smallpox_simulation_pop_30_vp_0.5_infected_1.txt'
    logger = Logger(file_name)
