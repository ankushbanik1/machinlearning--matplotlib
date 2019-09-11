import matplotlib.pyplot as plt 


x=[12,23,43,2,45,11]
y=[76,23,44,33,21,2]

plt.scatter(x,y,label='^^',color='green',marker='^',s=95)
plt.xlabel('x')
plt.ylabel('y')

plt.title('x-y-graph')
plt.legend()
plt.show()