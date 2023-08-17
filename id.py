# -*- coding: utf-8 -*-
import random
location=int(input("location:"))
date=int(input("date:"))
setround=int(input("round:"))
round=(0)
save=open("idsave", mode='a+', encoding="utf-8")#以追加方式写入
while round < setround :
       housiwei=(random.randint(1000, 9999))
       huodedesfz=("身份证号"+str(location)+str(date)+str(housiwei)+"\n")
       save.write(str(huodedesfz))
       print(huodedesfz)
       round=(round+1)
print("done")
