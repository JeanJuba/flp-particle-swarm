import numpy as np
import pylab
import random as r
from scipy.spatial import distance
from copy import copy


class Department:

    def __init__(self, index=None, x=0, y=0):
        self.x = x
        self.y = y
        self.index = index

    def __repr__(self):
        return 'x %s,   y %s' % (self.x, self.y)


class Particle:

    def __init__(self, index=None, department_list=[], value=None):
        self.departments = department_list
        self.total_cost = value
        self.index = index

    def __repr__(self):
        return 'Index %d  | Cost %d' % (self.index, self.total_cost)


x_bound = 100
y_bound = 100
particle_number = 100
department_number = 7

particles = []

particles_best = []

global_best_x = None
global_best_y = None
global_best_value = None

seven_cost = [[0, 0, 0, 5, 0, 0, 1], [0, 0, 0, 3, 0, 0, 1], [0, 0, 0, 2, 0, 0, 1],
              [0, 0, 0, 0, 4, 4, 0], [0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0]]

seven_area = [16, 16, 32, 9, 9, 9, 9]
penalty = 5000


def initialize_data(part=[]):
    for particles_index in range(0, particle_number):
        line = []
        for dept_index in range(0, department_number):
            dept = Department(dept_index, np.random.random(1)[0], np.random.rand(1)[0])
            line.append(dept)
        particula = Particle(particles_index, line.copy, None)
        part.append(particula)
    return part


def find_particle_best(part=[], pbest=[]):
    for particle_index, particle in enumerate(part):
        print('\npart====')
        particle_value = 0
        for dept1 in particle.departments():
            for dept2 in particle.departments():
                if dept1.index != dept2.index:
                    euclidean_distance = distance.euclidean((dept1.x, dept1.y), (dept2.x, dept2.y))
                    print(euclidean_distance)
                    particle_value += euclidean_distance * seven_cost[dept1.index][dept2.index]

        print('Particle Value: %d' % particle_value)
        particle.total_cost = particle_value

        if len(pbest) < particle_index + 1:
            print('Primeiro loop')
            pbest.append(copy(particle))
        elif particle_value < pbest[particle_index].total_cost:
            pass


def find_global_best(particle_best = []):
    best_found = None
    for particle in particles_best:
        if best_found is None:
            best_found = copy(particle)
        elif particle.total_cost < best_found.total_cost:
            best_found = copy(particle)
    print('\nBest found: ', best_found)


def get_better():
    pass


def print_particle_best(particles=[]):
    for part in particles:
        print(part)


particles = initialize_data()
find_particle_best(particles, particles_best)
print_particle_best(particles_best)
find_global_best(particles_best)
