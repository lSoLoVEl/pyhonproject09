#คุณสมบัติเด่น OOP: Encapsulation (ตนคุย/ซ่อนไว้/ห้อหุ้ม)
#(ตนคุย/ซ่อนไว้/ห้อหุ้ม) data โดนใส่ __ ให้หน้าชื่อ data
class MyTestA:
    __data1 = 10
    data2 = 20

    def __init__(self,data3):
        self.__data3 = data3
    def showData(self):
        print(f'__data1 มีค่า {self.__data1}')
        print(f'data2 มีค่า {self.data2}')
        print(f'__data3 มีค่า {self.__data3}')
        print('------------------------------')


ob1 = MyTestA(30)
ob1.showData()
ob1.data2= 300
ob1.__data1 = 100
ob1.showData()

