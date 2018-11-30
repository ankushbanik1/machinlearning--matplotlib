#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt


x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,0.2)

y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)


plt.subplot(2,1,1)
plt.plot(x1,y1,'o-')
plt.title('graph' )
plt.xlabel('x1')
plt.ylabel('amp(y1)')


plt.subplot(2,1,2)
plt.plot(x2,y2,'.+.')
plt.title('graph-2')
plt.xlabel('x2')
plt.ylabel('Amp(y2)')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




