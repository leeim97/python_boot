# 가시성 : 정보 은닉
# 비공개 필드, 비공개 메서드
# 비공개 필드는 직접 접근가능한 메서드를 구현하여 사용하거나
# 데코레이터를 (@property) 사용하여 직접 사용


class Product():
    def __init__(self,name):
        self.name=name

class Inventory():
    def __init__(self):
        self.__items = []

    def addNewItem(self,product):
        if type(product) == Product:
            self.__items.append(product)
            print('new item added')
        else:
            print('error')

    def getNumberofitems(self):
        return len(self.__items)

    # 데코리에터 @property를
    # 사용하여 비공개 필드를 직접접근하여 사용
    @property
    def items(self):
        return self.__items

product1=Product('크리스피크림도넛')
myInvent = Inventory()
myInvent.addNewItem(product1)
print(myInvent.getNumberofitems())
print(myInvent.items)
