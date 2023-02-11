
import random
import numpy as np
import game
import numpy as np
import random
import time
import graph
POPULATION_SIZE = 100


class Individual(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''

        return population()

def mate(one,two):

    child_chromosome = []
    # child=[]
    # for key, weight in top_three:
    #     # tuple to list
    #     child.append(weight)

    model1_weights= one
    model2_weights= two

    for gp1, gp2 in zip(model1_weights, model2_weights):  
        # random probability
        prob = random.random()
        print(prob)
        if prob < 0.55:
            child_chromosome.append(gp1)
        else:
            child_chromosome.append(gp2)
    #   mutation 
    for i in range(len(child_chromosome)):
        for j in range(len(child_chromosome[i])):
          child_chromosome[i][j] += np.random.normal(0, 0.1)
          return child_chromosome

def populata():
        w1=np.random.randn(6, 12).astype(np.float32)
        w2=np.random.randn(12, 16).astype(np.float32)
        w3=np.random.randn(16, 8).astype(np.float32)
        w4=np.random.randn(8, 4).astype(np.float32)
        # pop= [w1,np.random.randn(8).astype(np.float32),
              # w2,np.random.randn(3).astype(np.float32)]
        pop = [w1,np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=np.float32),
                w2,np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=np.float32),
                w3,np.array([0., 0., 0., 0., 0., 0., 0., 0.], dtype=np.float32),
                w4,np.array([0., 0., 0., 0.], dtype=np.float32)]
        return pop 

# def populata():
#         w1=np.random.randn(6, 8).astype(np.float32)
#         w4=np.random.randn(8, 4).astype(np.float32)
#         # pop= [w1,np.random.randn(8).astype(np.float32),
#               # w2,np.random.randn(3).astype(np.float32)]
#         pop = [w1,np.array([0., 0., 0., 0., 0., 0., 0., 0.], dtype=np.float32),
#                 w4,np.array([0., 0., 0., 0.], dtype=np.float32)]
#         return pop 
def main():

    global POPULATION_SIZE
    generation = 1
    found = False
    generatiion_dic={}
    result_dict={}
    best_select={}
    population = []

    for _ in range(50):
        population.append(populata())

    while not found:
    # for x in range(3):
        fitness=[]
        for c in population:
            result = game.game(c,generation)
            result_dict[result[0]]=result[1]

        new_generation = []
        sorted_dic = sorted(result_dict.items(), key=lambda x: x[0], reverse=True)
        sorted_dic = sorted_dic[:10]
        for key, value in sorted_dic:
            print(f'key - {key}')
            fitness.append(key)
            new_generation.append(value)
            with open('file.txt', 'a') as file:
                    file.write(str(key))
                    file.write('\n')
            if key >1000:
                found=True
                break


        # s = int((10*POPULATION_SIZE)/100)
        
        s = int((90*POPULATION_SIZE)/100)


        for _ in range(40):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = mate(parent1,parent2)
            new_generation.append(child)
        

        population = new_generation

        print(f"Generation: {generation}")
        with open('file.txt', 'a') as file:
            file.write('Generation : ')
            file.write(str(generation))
            file.write('\n\n')


        generation += 1
        graph.graph(generation,max(fitness))
        # time.sleep(2)



if __name__ == '__main__':
    main()