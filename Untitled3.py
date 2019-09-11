#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[2,3,7,9,4,3,9,16,32]
plt.scatter(x,y,label='star', color='green', marker="*" ,s=95 )

plt.xlabel('x')
plt.ylabel('y')

plt.title('scatter-graph')
plt.legend()
plt.show()


# In[ ]:




