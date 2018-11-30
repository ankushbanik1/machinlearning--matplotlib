#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,5,7,9,6]

tick_label=['one','two','three','four','five']
plt.bar(x,y,tick_label=tick_label, width=0.7,color=['blue','green'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('plot 1')

plt.show()


# In[ ]:




