class AddCal:

    def __init__(self):
        self.result=0

    def adder(self,num):
        self.result +=num
        return self.result

myadder=AddCal()
myadder.adder(10)
print(myadder.result)
myadder.adder(20)
print(myadder.result)
myadder.adder(30)
print(myadder.result)