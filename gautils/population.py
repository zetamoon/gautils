from gautils.chromosome import Chromosome


class Population:
    """A batch of chromosomes to evolve"""
    def __init__(self, size, fitness):
        self.fitness = fitness
        self.size = size
        self.chromosomes = [Chromosome() for _ in range(size)]

    def selection(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass
