class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    ebola_virus = Virus("Ebola", 0.7, 0.2)
    assert ebola_virus.name == "Ebola"
    assert ebola_virus.repro_rate == 0.7
    assert ebola_virus.mortality_rate == 0.2

    smallpox_virus = Virus("Smallpox", .06, .17)
    assert smallpox_virus.name == "Smallpox"
    assert smallpox_virus.repro_rate == .06
    assert smallpox_virus.mortality_rate == .17
