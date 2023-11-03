#คุณสมบัติเด่น OOP: Inheritanec สืบทอด
#คือ คลาสหนึ่สิบทองอีกคลาสหนิ่ง (มีแม่ super/มีลูก sub)
#พ่อเป็นแม่ลูกกันแม่มีอะไรลูกมีด้วย
class TestA:
    data1=10
    data2=20

    def showSAU():
        print('Hi.....SAU')

class TestB(TestA):
    data3 = 30

    def showWOW():
        print('wow wow wow')
class TestC(TestA):
    dara4=40

class TestD(TestB):
    data5 = 50

ob1 = TestA()
ob2 = TestB()
ob3 = TestD()







#คุณสมบัติเด่น OOP: Polymorphismพ้องรูป
# คือ พฤติกรรมเดียวกัน แต่วิธีการต่างกัน (ต้องเป็นแม่ลูกกัน )
class Test2(TestA):
    data6=60

    #Polymorphism: Overding Method
    def showSAU():
        print('Hellp........SAU')

ob4 = TestZ()
