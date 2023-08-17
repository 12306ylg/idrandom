import random
location=input("location:")
date=input("date:")
setround=input("round:")
save=open(idsave, mode='a')#以追加方式写入
while(round < setround):
 housiwei=(random.randint(1000, 9999))
 huodedesfz=(str(location),str(date),str(housiwei))
 save.write(huodedesfz)
 round=(round+1)
