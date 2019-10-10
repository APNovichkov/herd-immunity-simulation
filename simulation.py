import random
import sys
from person import Person
from logger import Logger
from virus import Virus

random.seed(42)


class Simulation(object):
    def __init__(self, population_size, percent_vaccinated, num_initial_infected, virus):
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.population = None
        self.population_size = population_size
        self.next_person_id = 0
        self.virus = virus

        self.num_initial_infected = num_initial_infected
        self.num_total_infected = 0
        self.num_current_infected = 0
        self.percent_vaccinated = percent_vaccinated
        self.num_dead = 0

        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)

        self.newly_infected = []

        self.NUM_PPL_TO_INTERACT_WITH = 10

        self.step_counter = 3

        self.logger.write_metadata(self.population_size, self.percent_vaccinated, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

    def create_population(self):
        people = []

        print("Creating population of size: " + str(self.population_size))

        for person_id in range(self.population_size):
            print("person_id: {}".format(person_id))

            if person_id < self.num_initial_infected:
                print("This person is infected!")
                person = Person(person_id, False, self.logger, True, self.virus)
                people.append(person)
            elif person_id >= self.num_initial_infected and person_id < (self.percent_vaccinated * self.population_size + self.num_initial_infected):
                print("This person is vaccinated")
                person = Person(person_id, True, self.logger, False, None)
                people.append(person)
            else:
                print("This person is neither vaccinated or infected")
                person = Person(person_id, False, self.logger, False, None)
                people.append(person)

        print("Done creating population")

        return people

    def simulation_should_continue(self):
        should_simulation_continue = False

        for person in self.population:
            if person.is_infected:
                should_simulation_continue = True

        if should_simulation_continue:
            for person in self.population:
                if person.is_alive:
                    should_simulation_continue = True
                    break

                if not person.is_vaccinated:
                    should_simulation_continue = True
                    break

        return should_simulation_continue

    def run(self):
        self.population = self.create_population()

        # TODO: Finish this method. To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        time_step_counter = 1

        while True:
            self.time_step()
            if self.simulation_should_continue():
                self.logger.log_time_step(time_step_counter)
                time_step_counter += 1
            else:
                self.logger.log_input_string("The simulation has ended after {} steps".format(time_step_counter))
                break

    

    # This function works!
    def time_step(self):
        # print("Single time step")
        interaction_counter = 0

        # Run through all people in population
        for person in self.population:
            # Check if person is infected and alive!
            if person.is_infected and person.is_alive:
                # print("Person {} thats infected is infecting".format(person._id))
                # Have that person interact with NUM_PPL_TO_INTERACT_WITH people
                while interaction_counter < self.NUM_PPL_TO_INTERACT_WITH:
                    # Get a random person from population
                    random_person = self.population[(random.randint(0, self.population_size - 1))]

                    # Check if that person is alive
                    if random_person.is_alive:
                        # Have current infected person interact with a random alive person
                        self.interaction(person, random_person)
                        interaction_counter += 1

                interaction_counter = 0

        # Check if every infected person in the population survived or died
        for person in self.population:
            if person.is_infected:
                person.did_survive_infection()

        # Infect newly infected
        self.infect_newly_infected()

    # This function is broken!
    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True

        # check if person is infected or vaccinated
        if not random_person.is_infected and not random_person.is_vaccinated:
            if random.random() < self.virus.repro_rate:
                # infect the person
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(person, random_person, False, False, True)
        else:
            # person is infected or vaccinated already
            self.logger.log_interaction(person, random_person, self.is_person_infected(random_person), random_person.is_vaccinated, False)

    def infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person_id in self.newly_infected:
            self.population[person_id].infection = self.virus
            self.population[person_id].is_infected = True

        self.newly_infected = []


    def is_person_infected(self, person):
        return person.infection is not None





def test_is_person_infected(self):
    sim = Simulation(pop_size, vacc_percentage, initial_infected, None)

    assert sim.is_person_infected == None



if __name__ == "__main__":
    params = sys.argv[1:]

    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])
    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()

if __name__ == "__main__":
    # params = sys.argv[1:]

    virus_name = "Smallpox"
    repro_rate = .5
    mortality_rate = .5
    pop_size = 100
    vacc_percentage = .1

    initial_infected = 10

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()


