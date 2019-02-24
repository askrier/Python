#%% Imports
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

#%% Define function and independent range
def f(x):
    return x ** 5 + 100 * np.cos(2 * x)

xp = np.linspace(-4, 4, 1000)

#%% Create and clear figure with two rows of plots
fig, (ax1, ax2) = plt.subplots(2, 1, num=1, clear=True)

#%% Create and clear figure with two rows of plots
fig, (ax1, ax2) = plt.subplots(2, 1, num=1, clear=True)

#%% Plot function in top half
ax1.plot(xp, f(xp), 'k-')
ax1.set(xlabel='x', ylabel='(f(x))')
ax1.grid(1)

#%% Plot sign of function in bottom half
ax2.plot(xp, np.sign(f(xp)), 'k-')
ax2.set(xlabel='x', ylabel='sign(f(x))')
ax2.grid(1)

#%% Fix overlap issues and save
plt.tight_layout()
plt.savefig('br_2_plot.png') #for Sakai if needed
plt.savefig('br_2_plot.eps') #for LaTeX if needed

#%% Find roots
rt1 = opt.brentq(f, -1, 0)
rt2 = opt.brentq(f, 0, 1)
rt3 = opt.brentq(f, 2, 3)

print('{:.2e} {:.2e} {:.2e}'.format(rt1, rt2, rt3))

#%% Find min and max
minloc1 = opt.fminbound(f, -2, -1)
minval1 = f(minloc1)
print("{:.2e} {:.2e}".format(minloc1, minval1))
minloc2 = opt.fminbound(f, 1, 2)
minval2 = f(minloc2)
print("{:.2e} {:.2e}".format(minloc2, minval2))

maxloc1 = opt.fminbound(lambda x: -f(x), -3, -2)
maxval1 = f(maxloc1)
print('{:.2e} {:.2e}'.format(maxloc1, maxval1))
maxloc2 = opt.fminbound(lambda x: -f(x), -1, 1)
maxval2 = f(maxloc2)
print('{:.2e} {:.2e}'.format(maxloc2, maxval2))