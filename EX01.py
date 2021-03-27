# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:21:41 2021

@author: wushu
"""

import random
data=[]

for i in range(1,7):
     if len(data)<6:
         n=random.randint(1,49)
     elif len(data)==6:
         break
     if data.count(n)==0:
         data.append(n)
     elif data.count(n)!=0:
         i-=1
data.sort() 
print(data)
