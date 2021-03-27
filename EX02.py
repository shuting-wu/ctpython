# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:34:39 2021

@author: wushu
"""

import random
k=[]
for i in range(1,8):
    num=random.randint(1,100)
    k.append(num)
    k.sort()
print(k)
find=int(input("請輸入要尋找的值"))

mid=int((len(k)-1)/2)
while True:
    if find==k[mid]:
        print([find])
        print("找到了")
        break
    elif find>k[mid]:
        del k[:mid+1]
        print(k)
        mid=int((len(k)-1)/2)
    elif find<k[mid]:
        del k[mid:]
        print(k)
        mid=int((len(k)-1)/2)

        
