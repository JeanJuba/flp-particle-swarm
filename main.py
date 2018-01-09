import numpy as np
import pylab
import random as r


x_bound = 100
y_bound = 100
n_partic = 10
dept = 7

particles_x = []
particles_y = []

pbest = []
pbest_value = []

gbest = []
gbest_value = []

seven_cost = [[0, 0, 0, 5, 0, 0, 1], [0, 0, 0, 3, 0, 0, 1], [0, 0, 0, 2, 0, 0, 1],
         [0, 0, 0, 0, 4, 4, 0], [0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0]]

seven_area = [16, 16, 36, 9, 9, 9]


def read_data():
    pass


def randomize_start():
    for i in range(0, n_partic):
        x = np.random.rand(dept) * x_bound
        y = np.random.rand(dept) * y_bound
        print(len(x), len(y))
        particles_x.append(x)
        particles_y.append(y)


def find_pbest():
    for i in range(0, n_partic):



def find_gbest():
    pass

def generate_graph():
    subp = pylab.subplot()
    colors = np.random.rand(10)

    for i in range(0, dept):
        print(particles_x[0][i], particles_y[0][i])
        circle = pylab.Circle((particles_x[0][i], particles_y[0][i]), radius=2, fill=False, clip_on=False)
        subp.add_artist(circle)

    pylab.xlim(0, x_bound)
    pylab.ylim(0, y_bound)
    pylab.show()

randomize_start()
generate_graph()