import pylab
from scipy.spatial import distance
import numpy as np

plt = pylab.subplot()

c1_coord = [4, 2]
c2_coord = [10, 2]

c1 = pylab.Circle(c1_coord, radius=3)

c2 = pylab.Circle(c2_coord, radius=3)
print(distance.euclidean(c1_coord, c2_coord))
##plt.add_artist(c1)
##plt.add_artist(c2)

pylab.xlim(0, 20)
pylab.ylim(0, 20)

pylab.plot([0, 1, 2, 3, 10, 20], [0, 4, 5, 6, 15, 20], 'bo-',  [1, 3, 5], [3, 5, 7], '--')
pylab.show()



