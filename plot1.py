import matplotlib.pyplot as plt


x=[1,2,3,4,6,7]
y=[2,7,9,22,1,7]

tick_label=['2001','2002','2003','2004','2005','2006']
plt.bar(x,y,tick_label=tick_label,width=0.7,color=['green','blue'])
plt.xlabel=('x')
plt.ylabel=('y')
plt.title('plt')
plt.show()


