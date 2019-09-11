{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "x=np.arange(0,2*np.pi,0.01)\n",
    "\n",
    "y1=np.sin(x)\n",
    "y2=np.cos(x)\n",
    "\n",
    "plt.plot(x,y1,label='sin')\n",
    "plt.plot(x,y2,label='cos')\n",
    "\n",
    "plt.title('plot')\n",
    "plt.legend()\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
