# This challenge is about Biology.

# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.

# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosome, and it can also mutate the same way Chromosomes can.
# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and a environement parameter that sets the probability for its DNA to mutate.
# Instantiate a number of Organims and let them mutate until one gets to a DNA is only made of 1s. Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).
import random


class Gene:

    def __init__(self, state):
        self.state = state

    def change_state(self, new_state):
        self.state = new_state



class Chromosome:

    def __init__(self, genes):
        self.genes = genes

    def mutate(self):
        mutated_genes = []
        for gene in self.genes:
            gene.change_state(random.randint(0, 1))
            mutated_genes.append(gene)
        self.genes = mutated_genes

    def code(self):
        code = ''
        for gene in self.genes:
            code += str(int(gene.state))
        return code


class DNA:

    def __init__(self, chromosomes):
        self.chromosomes = chromosomes

    def mutate(self):
        mutated_chromosomes = []
        for chromosome in self.chromosomes:
            chromosome.mutate()
            mutated_chromosomes.append(chromosome)
        self.chromosomes = mutated_chromosomes

    def code(self):
        code = ''
        for chromosome in self.chromosomes:
            code += chromosome.code()
        return code


class Organism:

    def __init__(self, dna, env_param=0.1):
        self.dna = dna
        self.env_param = env_param

    def mutate(self):
        if random.random() <= self.env_param:
            self.dna.mutate()

    def code(self):
        print(self.dna.code())
        return self.dna.code()


org1 = Organism(DNA([Chromosome([Gene(random.randint(0, 1)) for i in range(10)]) for j in range(10)]), 1)
while '0' in org1.code():
    org1.mutate()
    org1.code()
