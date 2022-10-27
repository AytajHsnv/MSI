"""
This is the template for coding tasks in exercise sheet 1.

Everywhere you see "YOUR CODE", it means a playground for you :P

WARNING: do not rename variables as this will break the tests.
=============================================================================================================================

Through this exercise, you will get to know the basic usage of NumPy and Matplotlib, i.e. frequently used functions/methods.
Because it is the starting point, we thought some referrences to the official documentation will ease the process.

PRECAUTION: you don't need to read through every details in the documentation, that is way too overkill. In most cases, 
grasp a rough idea of how to call a function/method with minimal arguments, and you are good to start writing your own code! 
Many typically offer some examples, which are even more intuitive. As for optional parameters, you can return to them later 
when the minimal use case cannot fulfill your demand.


We are dealing with vectors and matrices in this course, so you will need a NumPy array to store these kind of data.
Beside the classic "np.array()" function, a few functions by specifying a shape can sometimes be very handy:
    <https://numpy.org/doc/stable/reference/routines.array-creation.html#from-shape-or-value>

After you have your arrays, you can apply operators (+, -, *, /, =, ** as exponent) to them at ease. NumPy also provides 
various methods for more advanced operations, for example, the mean value:
    <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html>
Of course, you don't have to use it. There is always more than one solution to a problem.

Quite often, you want to do something with only a part of the array, such as, a single element, a specific row/column, 
a few rows/columns, etc. This is achieved by properly indexing and slicing:
    <https://numpy.org/doc/stable/user/basics.indexing.html#basic-indexing>


After the calculation, it is the exciting moment to show them off in the plots!

The "plt.figure()" function (code already written for this exercise) will create and/or switch to a plot. Then you can call 
various Pyplot functions to draw on the plot.

To draw a line:
    <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html>

To draw a histogram:
    <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html>

Optionally, you can also add title / xlabel / ylabel / legend to make your plot fancier.


Have fun!
"""


import matplotlib.pyplot as plt
import numpy as np


Nmax = 1000 # number of samples
M = 200  # number of experiments

# load exercise data
data = np.load("exercise1_dataset.npz")
u = data['u']
i = data['i']


## (a)
# YOUR CODE: calculate the values
# ===============================
# "None" is just to pass the syntax check. Replace them with your code. Don't need to stick to a single line.
# (The same holds for all the following cases)
R_SA_single = np.zeros((Nmax,1))
R_LS_single = np.zeros((Nmax,1))
R_EV_single = np.zeros((Nmax,1))

for k in range(0,Nmax):
    R_SA_single[k,0] = np.array(np.mean(u[:k+1,0]/i[:k+1,0]))
    R_LS_single[k,0] = np.array(np.mean(u[:k+1,0]*i[:k+1,0])/np.mean(i[:k+1,0]**2))
    R_EV_single[k,0] = np.array(np.mean(u[:k+1,0])/np.mean(i[:k+1,0]))


plt.figure(1)
# YOUR CODE: draw on the plot 
plt.plot(R_SA_single, "r", label = "R_SA_single")
plt.plot(R_LS_single, "g", label = "R_LS_single")
plt.plot(R_EV_single, "b", label = "R_EV_single")
plt.legend()

## (b)
# YOUR CODE: calculate the values
R_SA = np.zeros((Nmax,M))
R_LS = np.zeros((Nmax,M))
R_EV = np.zeros((Nmax,M))

for j in range(M):
    for k in range (Nmax): 
        R_SA[k,j] = np.mean(u[:k+1,j]/i[:k+1,j])
        R_LS[k,j] = np.mean(u[:k+1,j]*i[:k+1,j])/np.mean(i[:k+1,j]**2)
        R_EV[k,j] = np.mean(u[:k+1,j])/np.mean(i[:k+1,j])

plt.figure(2)
plt.plot(R_SA, "r")

plt.legend()

plt.figure(3)
plt.plot(R_LS, "g")
plt.legend()

plt.figure(4)
plt.plot(R_EV, "b")
plt.legend()

## (c)
# YOUR CODE: calculate the values
R_SA = np.array(R_SA)
R_SA_mean = np.mean(R_SA, axis=1)
R_LS = np.array(R_LS)
R_LS_mean = np.mean(R_LS, axis=1)
R_EV = np.array(R_EV)
R_EV_mean = np.mean(R_EV, axis=1)

plt.figure(5)
# YOUR CODE: draw on the plot 
plt.title("Mean of resistance")
plt.plot(R_SA_mean, "r", label = "R_SA_mean")
plt.plot(R_LS_mean, "b", label = "R_LS_mean")
plt.plot(R_EV_mean, "g", label = "R_EV_mean")
plt.legend()
## (d)
# YOUR CODE: calculate the values
R_SA_Nmax = R_SA[Nmax-1, :]
R_LS_Nmax = R_LS[Nmax-1, :]
R_EV_Nmax = R_EV[Nmax-1, :]

plt.figure(6)
plt.hist(R_SA_Nmax, bins = 25)

plt.figure(7)
plt.hist(R_LS_Nmax, bins = 25)
# YOUR CODE: draw on the plot 

plt.figure(8)
plt.hist(R_EV_Nmax, bins = 25)
# YOUR CODE: draw on the plot 


# show all plots
# ===============
# If you don't see any plots but also no errors, it is very likely because a non-interactive backend is chosen by default.
# One possible solution you can try is to manually select another backend via "matplotlib.use()" function at the beginning.
# Here gives more details: <https://matplotlib.org/stable/users/explain/backends.html>
plt.show()
