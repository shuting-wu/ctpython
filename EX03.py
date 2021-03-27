# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:36:09 2021

@author: wushu
"""

money=int(input("請輸入獲利金額"))
if money <=100000:
    print(money*0.1)
elif money>100000 and money<200000:
    print(100000*0.1+((money-100000)*0.07))
elif money>200000 and money<400000:
    print(100000*0.1+100000*0.07+((money-200000)*0.03))    
    
   