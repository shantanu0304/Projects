from sklearn.linear_model import LinearRegression

lr=LinearRegression()

f=[[1,10],[3,13],[5,17],[8,25],[13,29]]
l=[20,23,28,37,45]

trained=lr.fit(f,l)

res=trained.predict([[8,25],[10,70],[3,7],[5,15]])
print(res)
