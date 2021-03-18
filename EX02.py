# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:53:22 2021

@author: wushu
"""

n=int(input("請輸入一個起始值"))
m=int(input("請輸入一個終值"))
for i in range(n,m+1): 
    for a in range(2,i):
        if i%a==0:
            break
        elif i%a!=0:
            continue
            print(i,"是質數")
    if i%4==0:
        print(i,"是4的倍數")
    else:
        print(i,"不是4的倍數")
