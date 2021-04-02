#the key parameter can be used to sort complex objects
from operator import attrgetter, methodcaller, itemgetter


class Product():
    def __init__(self,name,price,weight,discount):
        self.name=name
        self.price=price
        self.weight=weight
        self.discount = discount

    def __repr__(self):
        return repr((self.name,self.price,self.weight))

    def discountPrice(self):
        return self.price-(self.price*self.discount)

prodList=[
    Product("widget",50,10,0.05),
    Product("dkey",40,12,0.02),
    Product("thef",30,15,0.09),
    Product("thewf",25,14,0.01)

]
#operator module functions provide easy ways to select fields
#attrgetter()retrieves a given attribute or property from an object
#itemgetter() retrieves an item at agiven index in a collection
#methodcaller() calls the given method on the object
print("using the attrgetter method:")
print(sorted(prodList,key=attrgetter("weight"),reverse=True))
print(sorted(prodList,key=methodcaller("discountPrice")))

inventory=[("widget",5),("dkey",3),("thef",7)]
print(sorted(inventory,key=itemgetter(1)))
