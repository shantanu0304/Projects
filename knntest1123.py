from sklearn.neighbors import KNeighborsClassifier

f=[[50,0],[40,2],[60,1],[70,2],[85,5]]
l=['bad','bad','bad','good','good']

knnc=KNeighborsClassifier(n_neighbors=3)
knnct=knnc.fit(f,l)
print(knnct)
res=knnct.predict([[70,0]])
print(res)
