import numpy as np
import pylab


class FLP:

    def __init__(self):
        self._x_bound = 100
        self._y_bound = 100
        self._n_partic = 10
        self._dept = 7

        self._particles_x = []
        self._particles_y = []

        self._pbest_x = []
        self._pbest_y = []
        self._pbest_value = []

        self._gbest_x = None
        self._gbest_y = None
        self._gbest_value = None

        self._seven_cost = [[0, 0, 0, 5, 0, 0, 1], [0, 0, 0, 3, 0, 0, 1], [0, 0, 0, 2, 0, 0, 1],
                      [0, 0, 0, 0, 4, 4, 0], [0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 0, 0]]

        seven_area = [16, 16, 36, 9, 9, 9]

    def read_data(self):
        pass

    def randomize_start(self):
        for i in range(0, self._n_partic):
            x = np.random.rand(self._dept) * self._x_bound
            y = np.random.rand(self._dept) * self._y_bound
            print(len(x), len(y))
            self._particles_x.append(x)
            self._particles_y.append(y)

    def find_pbest(self):

        for i in range(0, self._n_partic):
            temp_value = 0
            for j in range(0, self._dept):
                for k in range(0, self._dept):
                    temp_value += np.linalg.norm(self._particles_x[i][j] - self._particles_x[i][k]) * self._seven_cost[j][k]
                    temp_value += np.linalg.norm(self._particles_y[i][j] - self._particles_y[i][k]) * self._seven_cost[j][k]

            if len(self._pbest_x) < i + 1:
                self._pbest_x.append(self._particles_x[i])
                self._pbest_y.append(self._particles_y[i])
                self._pbest_value.append(temp_value)
            else:
                pass
        print('pbest: ', self._pbest_value)


    def find_gbest(self):

        for index, value in enumerate(self._pbest_value):
            if self._gbest_value is None:
                self._gbest_x = self._pbest_x[index]
                self._gbest_y = self._pbest_y[index]
                self._gbest_value = value
            elif value < self._gbest_value:
                self._gbest_x = self._pbest_x[index]
                self._gbest_y = self._pbest_y[index]
                self._gbest_value = value

            print('gbest: ', self._gbest_value)


    def generate_graph(self, gbest_index=0):
        subp = pylab.subplot()

        for i in range(0, self._dept):
            print(self._particles_x[gbest_index][i], self._particles_y[gbest_index][i])
            circle = pylab.Circle((self._particles_x[gbest_index][i], self._particles_y[gbest_index][i]), radius=2, fill=False, clip_on=False)
            subp.add_artist(circle)

        pylab.xlim(0, self._x_bound)
        pylab.ylim(0, self._y_bound)
        pylab.show()


flp = FLP()
flp.randomize_start()
flp.find_pbest()
flp.find_gbest()
flp.generate_graph()