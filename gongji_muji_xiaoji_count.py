'''
求公鸡母鸡小鸡个数
'''
# a*5+b*3+c*(1/3)=100
# a+b+c=100
for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):
            if (a*5+b*3+c*(1/3)==100) and (a+b+c==100):
                print(a,b,c)
            else:
                continue