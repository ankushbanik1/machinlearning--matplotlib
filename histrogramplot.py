import matplotlib.pyplot as plt

ages=[12,45,87,9,34]
binss=10
range=(0,100)

plt.hist(ages,binss,range,histtype='bar',color=['r'],rwidth=0.7)
plt.title('histrogram')
plt.xlabel('ages')
plt.ylabel('binss')
plt.show()