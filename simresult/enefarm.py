import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt

con_m = np.array([500, 450, 400, 350, 400, 450, 500, 550, 550, 500, 450, 450])
gen_m = np.array([450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 450])

con_y = np.sum(con_m)
gen_m = np.sum(gen_m)
short_y = 1000
surp_y = 500
exc_y = 1400

plt.figure()
xvals = range(len(con_m))

plt.plot(3,2,'o')
#plt.bar(xvals, con_m, width = 0.5)

print(xvals)

