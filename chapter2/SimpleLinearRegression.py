import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = [ [6], [8], [10], [14], [18] ]
y = [ [7], [9], [13], [17.5], [18] ]

model = LinearRegression()
model.fit(x,y)
print 'A 12" pizza should cost: $%.2f' % model.predict([12])[0]

plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.plot(x, y, 'k.')
plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()
