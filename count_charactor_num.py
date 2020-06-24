'''
求字符串中大小写字母，数字个数
'''
def stat_str(string):
    small = 0
    big = 0
    num = 0
    for ch in string:
        if ch<='z' and ch>='a':
            small=small+1
        elif ch<='Z' and ch>='A':
            big=big+1
        elif ch<='9' and ch>='0':
            num=num+1
        else:
            continue
    return small,big,num
stat_str('zZ9')