class Stats(object):
    def __init__(self, population_size):
        self.population_size = population_size
        self.infection_num = 0
        self.death_num = 0
        self.saved_by_vaccination = 0

    def increment_infection_num(self):
        self.infection_num += 1
        pass

    def increment_death_num(self):
        self.death_num += 1
        pass

    def increment_saved_by_vaccination(self):
        self.saved_by_vaccination += 1
        pass

    def print_stats(self):
        print("Total population size: {}".format(self.population_size))
        print("Total infected by virus: {}".format(self.infection_num))
        print("Percent infected by virus: {}%".format(self.infection_num / self.population_size * 100))
        print("Total deaths from virus: {}".format(int(self.death_num)))
        print("Percent of people that died from virus: {}%".format(self.death_num / self.population_size * 100))
        print("Total interactions where a person was saved by vaccination: {}".format(self.saved_by_vaccination))
        print("Percent of interactions where a person was saved by vaccination: {}%".format(self.saved_by_vaccination / self.population_size * 100))
