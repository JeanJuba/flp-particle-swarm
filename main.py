import numpy as np
import pylab
import random as r
from scipy.spatial import distance
from copy import copy


class Department:

    def __init__(self, index=None, x=0, y=0, radius=None):
        self.x = x
        self.y = y
        self.radius = radius
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

global_best = None

cost = [[0, 0, 0, 5, 0, 0, 1], [0, 0, 0, 3, 0, 0, 1], [0, 0, 0, 2, 0, 0, 1],
              [0, 0, 0, 0, 4, 4, 0], [0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0]]

area = [16, 16, 32, 9, 9, 9, 9]
penalty = 5000


def initialize_data(part=[], area=[]):
    """
    Randomly starts the data according to predefined variables.
    :param part: 
    :return: 
    """

    for particles_index in range(0, particle_number):
        line = []
        for dept_index in range(0, department_number):
            dept = Department(dept_index,
                              r.uniform(0 + area[dept_index]/2, x_bound - area[dept_index]/2),
                              r.uniform(0 + area[dept_index]/2, y_bound - area[dept_index]/2), area[dept_index])
            line.append(dept)
        particula = Particle(particles_index, line.copy, None)
        part.append(particula)
    return part


def find_particle_best(part=[], pbest=[]):
    """
     Uses the cost matrix to find the best cost of each particle.
        The cost of each particle is given by the sum of the distance multiplied by the cost between 2 departments.
         Penalties can be given if certain conditions are not met.
    :param part: 
    :param pbest: 
    :return: 
    """
    for particle_index, particle in enumerate(part):
        particle_value = 0
        for dept1 in particle.departments():
            for dept2 in particle.departments():
                if dept1.index != dept2.index:
                    euclidean_distance = distance.euclidean((dept1.x, dept1.y), (dept2.x, dept2.y))
                    particle_value += euclidean_distance * cost[dept1.index][dept2.index]

                    if euclidean_distance < dept1.radius/2 + dept2.radius/2:
                        particle_value += 50

        particle.total_cost = particle_value

        if len(pbest) < particle_index + 1:
            pbest.append(copy(particle))
        elif particle_value < pbest[particle_index].total_cost:
            pbest[particle_index] = copy(particle)


def find_global_best(particle_best=[]):
    """
     Searches for the best particle best to make it the global best.   
    :param particle_best: 
    :return: 
    """

    best_found = None
    for particle in particles_best:
        if best_found is None:
            best_found = copy(particle)
        elif particle.total_cost < best_found.total_cost:
            best_found = copy(particle)
    print('\nBest found: ', best_found)
    return best_found


def get_better(p=[]):
    for part in p:
        for dept in part.departments():
            if bool(r.getrandbits(1)):
                #rand_x = r.randint(0, department_number - 1)
                #rand_y = r.randint(0, department_number - 1)

                dept.x = r.uniform(0 + dept.radius/2, x_bound - dept.radius/2)
                dept.y = r.uniform(0 + dept.radius/2, y_bound - dept.radius/2)
            else:
                pass


def print_particle_best(particles_list=[]):
    for part in particles_list:
        print(part)


def show_graph(global_b=[]):
    subplot = pylab.subplot()
    pylab.xlim(0, x_bound)
    pylab.ylim(0, y_bound)

    for dep in global_b.departments():
        print("x = %d,  y = %d, radius = %d" % (dep.x, dep.y, dep.radius))
        circle = pylab.Circle((dep.x, dep.y), radius=dep.radius, fill=False)
        subplot.add_artist(circle)

    pylab.show()

particles = initialize_data([], area)

for counter in range(0, 20):
    find_particle_best(particles, particles_best)
    result = find_global_best(particles_best)
    get_better(particles)
show_graph(result)
