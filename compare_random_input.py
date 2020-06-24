#产生一个随机数比较与输入数字大小

import random

rand = random.randint(0,100)
print(rand)
inpu = int(input("请输入："))
while(1):
    if inpu not in range(0,100):
        inpu = int(input("请输入："))
        continue
    else:
        if rand==inpu:
            print("相等")
        elif rand<inpu:
            print("大于随机数")
        else:
            print("小于随机数")
        break

