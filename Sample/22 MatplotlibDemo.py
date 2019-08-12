import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim=[0, 5], ylim=[0, 10], title='MatPlotLib Demo',
       ylabel='Y', xlabel='X')
plt.show()
