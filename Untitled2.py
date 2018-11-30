#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt

ages =[23,45,8,22,45,55,77,34,55,76,21,33]

range=(0,100)


bins=10
plt.hist(ages,bins ,range,color='green',histtype='bar',rwidth=0.8)
plt.xlabel('ages')
plt.ylabel('bins')
plt.title('Histrogram plot')

plt.show()


# In[ ]:





# In[ ]:




