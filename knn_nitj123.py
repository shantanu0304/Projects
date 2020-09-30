from sklearn.neighbors import KNeighborsClassifier

f=[[65,5],[80,3],[58,4],[40,7],[70,1]]
l=['good','good','bad','bad','bad']

kc=KNeighborsClassifier(n_neighbors=1)
trained=kc.fit(f,l)

res=trained.predict([[70,1],[75,5],[65,5],[90,1]])

print(res)
