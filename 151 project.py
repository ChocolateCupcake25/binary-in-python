# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:15:26 2022

@author: Ziyah Virani
"""

import matplotlib.pyplot as plt

data = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0], 
        [0,0,1,0,0,0,0,0,0], 
        [0,0,1,0,0,1,0,0,0], 
        [0,0,1,0,0,1,0,0,0], 
        [0,0,1,1,1,1,1,0,0], 
        [0,0,0,0,0,1,0,0,0], 
        [0,0,0,0,0,0,0,0,0]
                          ]

plt.imshow(data, cmap= 'gray')
plt.show()
