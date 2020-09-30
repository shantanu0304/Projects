import numpy as np
import matplotlib.pyplot as plt

x=np.random.randint(50,1000,10)
y=np.random.randint(50,160,10)

p=np.random.randint(50,1000,10)
q=np.random.randint(50,160,10)

plt.plot(x,y,x,y,'*g',p,q)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('time vs temp')
plt.text(x[0],y[0],'Start')
plt.text(x[-1],y[-1],'End')
plt.show()
