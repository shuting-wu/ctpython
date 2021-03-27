# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:53:00 2021

@author: wushu
"""

n=1
m=100
i=5
import random
ans=random.randint(1,100)
guess=int(input("請輸入1-100整數"))
while guess!=ans:
    if i==1:
        print("沒有猜到")
        break
    elif guess<ans:
        print(guess,"到",m,"之間",i-1,"次機會")
        guess=int(input("請輸入1-100整數"))
        i-=1
    elif guess>ans:
        print(n,"到",guess,"之間",i-1,"次機會")
        guess=int(input("請輸入1-100整數"))
        i-=1
while guess==ans:    
    print("猜到了")
    break

