# coding: utf-8

from __future__ import print_function

import numpy
import scipy
import matplotlib.pyplot as plt

print("numpy version {}".format(numpy.__version__))
print("scipy version {}".format(scipy.__version__))

fig, ax = plt.subplots()
ax.plot([1,5], [1,5], "k:")
fig.savefig("what.png")
