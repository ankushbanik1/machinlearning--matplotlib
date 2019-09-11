import matplotlib.pyplot as plt 
# import sklearn

active=['red','blue','green','black']
slice=[1,2,3,4]
color=['r','b','y','black']

plt.pie(slice,labels=active,colors=color,startangle=90,shadow=True)

plt.xlabel('x')
plt.ylabel('y')
plt.show()