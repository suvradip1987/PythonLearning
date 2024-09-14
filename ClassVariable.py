class Test:
    number =10

    def printNumber(self):
        print(self.number)
        print(Test.number)
        self.number = 15

    def setNumber(self, num):
        self.number = num


t1 = Test()
t2 = Test()

t1.setNumber(15)
t1.printNumber()