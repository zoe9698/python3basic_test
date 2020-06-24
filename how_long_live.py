'''
计算活了多少天，还剩多少天
'''
from datetime import date


class Mydate:
    '''
    参数格式：20200101
    '''
    today = datetime.date.today()

    #     print(today)

    def live(self, birthday):
        #         y = int(input("出生年份："))
        #         m = int(input("出生月份："))
        #         d = int(input("出生日份："))
        y = int(birthday[0:4])
        m = int(birthday[4:6])
        d = int(birthday[6:8])
        birthday = datetime.date(year=y, month=m, day=d)

        diffday = self.today - birthday
        return diffday.days

    def die(self, birthday, finalage):
        y = int(birthday[0:4])
        m = int(birthday[4:6])
        d = int(birthday[6:8])
        birthday = datetime.date(year=y, month=m, day=d)
        finalday = datetime.date(year=y + finalage, month=m, day=d)
        totalday = finalday - birthday

        birthday = datetime.date(year=y, month=m, day=d)
        preday = self.today - birthday

        diffday = totalday - preday
        return diffday.days


my = Mydate()
liveday = my.die("20000608", 80)
print(liveday)