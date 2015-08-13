import matplotlib.pyplot as plt

x = [ [6], [8], [10], [14], [18] ]
y = [ [7], [9], [13], [17.5], [18] ]

plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.plot(x, y, 'k.')
plt.axis([0, 25, 0, 25])

plt.grid(True)
plt.show()
