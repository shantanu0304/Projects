import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
d=pd.read_csv(r'/Users/techie/Desktop/Datasets/headbrain.csv')
qx=[4510]
qy=[1550]
p=d.head(10)
q=d.tail(10)
r=np.array(p)
s=np.array(q)
R=list(r.flatten())
S=list(s.flatten())
T=R+S
t=np.array(T)
t=np.reshape(t,[20,4])
t=np.delete(t,1,1)
x=t[:,1]
x1=x[0:10]
x2=x[10:]
y=t[:,2]
y1=y[0:10]
y2=y[10:]
print(t)
plt.plot(x1,y1,'*g',x2,y2,'*r',qx,qy,'*')
#plt.show()
l=t[:,0]
f=np.delete(t,0,1)
print(f)
print(l)
kc=KNeighborsClassifier(n_neighbors=3)
trained=kc.fit(f,l)
res=trained.predict([[4512,1530],[3391,1120]])
print(res)





