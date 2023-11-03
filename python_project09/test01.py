def sumNumber():
    pass                        

# สร้าง class ใน python
class IotSAU :  
    #data/attribute/filed/property member เหมือนกับตัวแปร
    info1 = 20
    info2 = ''


    #method member เหมือนกันฟังก์ชัน
    def showHi(self):
        print('Hi...')

    def showInfo(self):
        print(self.info1, self.info1)
        self.showHi()

#สร้าง object
obA = IotSAU()
obB = IotSAU()
obC = IotSAU()

obA.info1 = 100
print(obA.info1 + obB.info1)  #120
obC.showInfo()
obA.showInfo()