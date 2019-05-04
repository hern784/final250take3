import numpy as np
import numpy
import matplotlib.pyplot as plt


b = np.loadtxt('daytime.txt', delimiter=',')
X = b[:,0]
X = np.expand_dims(X, axis=1)
new_col = np.ones((92,1))
X = np.concatenate((new_col,X),axis=1)

XT = numpy.transpose(X)
R1 = np.dot(XT,X)
R2 = numpy.linalg.inv(R1)
R3 = np.dot(R2,XT)
W = np.dot(R3,b[:,1])
print(W)
H = np.dot(W,XT)

plt.close()  
plt.plot(b[:,0], b[:,1], "bo")
x = b[:,0]
y_prediction = W[0] + W[1]*x
plt.plot(x,y_prediction,color = "g")
plt.ylabel('cost of electric unit of (kWh) per day')
plt.xlabel('temperature in Farenheit')
plt.title('daytime electric bill for 2018 based on highest temperature')
plt.show()
