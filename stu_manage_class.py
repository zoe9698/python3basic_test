'''
学生管理类
'''


class MyStudent:
    path = 'd:/data.txt'

    #     print(path)
    def addStu(self):
        #         print(self.path)
        name = input("请输入姓名：")
        sno = input("请输入学号：")
        with open(self.path, 'a+') as f:
            f.write(str({'name': name, 'sno': sno}))
            f.write('\n')

    def readStu(self):
        with open(self.path, 'r') as f:
            print(f.read())

    def findStu(self, name):
        with open(self.path, 'r') as f:
            liststu = f.readlines()
        #         print(len(liststu))
        for stu in liststu:
            #             print(stu)
            stu = eval(stu)
            if stu['name'] == name:
                return stu['sno']

    def delStu(self, name):
        with open(self.path, 'r') as f:
            liststu = f.readlines()
        #         print(len(liststu))
        for stu in liststu:
            #             print(stu)
            stu = eval(stu)
            if stu['name'] == name:
                #                 print(liststu)
                liststu.remove(str(stu) + '\n')
                break

        with open(self.path, 'w') as f:
            for stu in liststu:
                f.writelines(str(stu))


mystu = MyStudent()
mystu.addStu()
mystu.addStu()
mystu.readStu()
sno = mystu.findStu('li')
sno
mystu.delStu('li')