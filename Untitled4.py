import matplotlib.pyplot as plt


activities=['eat','sleep','play','run']
slices= [1,2,3,4]

color=['r','b','g','y']

plt.pie(slices,labels=activities,colors=color, startangle=90,shadow=True, explode=[0.0,0,0,1],autopct='%01.2f%%')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




