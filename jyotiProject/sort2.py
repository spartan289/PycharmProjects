#the key parameter can be used to sort complex objects
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
    Product("thef",30,15,0.02)

]
#use the key parameter to select a field to sort on
def prodsort(product):
    return product.price
print(sorted(prodList,key=prodsort))
#define a lambda function as the sorting key
print(sorted(prodList,key=lambda p:p.price))

#the key parameter can also call a method on the object
print(sorted(prodList,key=lambda p:p.discountPrice()))

