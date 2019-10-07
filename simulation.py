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
        self.population = self._create_population()
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

        self.NUM_PPL_TO_INTERACT_WITH = 100

    def _create_population(self):
        people = []

        for person_id in range(self.population_size):
            if person_id < self.initial_infected and person_id < self.percent_vaccinated * self.population_size:
                people.append(Person(person_id, True, self.virus))
            elif person_id < self.initial_infected:
                people.append(Person(person_id, False, self.virus))
            elif person_id < self.percent_vaccinated * self.population_size:
                people.append(Person(person_id, True, None))
            else:
                people.append(Person(person_id, False, None))

        return people

    def _simulation_should_continue(self):
        should_simulation_continue = False

        for person in self.population():
            if person.is_alive:
                should_simulation_continue = True
                break

            if not person.is_vaccinated:
                should_simulation_continue = True
                break

        return should_simulation_continue

    def run(self):
        self.population = _create_population()

        # TODO: Finish this method. To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        time_step_counter = 0

        while _simulation_should_continue():
            self.time_step()
            time_step_counter += 1

        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

        pass

    def time_step(self):
        interaction_counter = 0

        for person in self.population():
            if person.infection is not None and person.is_alive:
                while interaction_counter < NUM_PPL_TO_INTERACT_WITH:
                    random_person = self.population.get(randint(0, self.population_size - 1))
                    if random_person.is_alive:
                        interaction(person, random_person)
                        interaction_counter += 1

        _infect_newly_infected()
        pass

    def interaction(self, person, random_person):
        assert person.is_alive == True
        assert random_person.is_alive == True

        if not is_person_infected(random_person) and not random_person.is_vaccinated:
            # random_int = randint(0,1)
            if random(0, 1) < random_person.infection.repro_rate:
                self.newly_infected.append(random_person._id)

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        pass

    def _infect_newly_infected(self):
        for person_id in self.newly_infected:
            self.population.get(person_id).infection = self.infection

        self.newly_infected = []
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass

    def is_person_infected(person):
        return person.infection is not None


if __name__ == "____-main__":
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
    repro_num = .06
    mortality_rate = .2
    pop_size = 10000
    vacc_percentage = .5

    initial_infected = 5

    virus = Virus(name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
