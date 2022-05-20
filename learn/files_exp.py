#  Define a class Product that stores information about products manufactured by a company. The
# class should contain the following data members:
# • name–Name of the Product
# • material– Material with which Product is made of ‘Metal’ or ‘Plastic’.
# • costPrice– Cost of the Product in rupees. Include assert statement to ensure that the cost
# is between 25 and 250.
# • discount– Deduction in cost of the Product. It is equal to 20% of costPrice if the
# material is ‘Metal’ and 10% for ‘Plastic’.
# • count - number of objects created for Product class. Add appropriate statements in the code
# to increment the value of count by 1, when an object is created. Use assert statement to check
# that count is always greater than equal to 0.
# The class should support the following methods:
# • _init_() for initializing data members.
# • sellingPrice() which computes and displays selling price where selling price is calculated
# as difference of costPrice and discount
# • display() which displays the information about the product.
# Also write Python statements for the following:
# • Create a product ‘Plate’ of ‘Metal’ having costPrice as 170. Display the value of
# count.
# • Create a product ‘Spoon’ of ‘Plastic’ having costPrice as 26. Display the value of
# count.
# • Compute and display the selling price of ‘Plate’ and ‘Spoon’. Display the value of
# count

class Product:
    count = 0
    def __init__(self, name, material, costPrice):
        self.name = name
        self.material = material
        assert costPrice >= 25 and costPrice <= 250, "Cost Price should be between 25 and 250"
        self.costPrice = costPrice
        if material == "Metal":
            self.discount = costPrice * 0.2
        else:
            self.discount = costPrice * 0.1
        Product.count += 1
        assert Product.count >= 0
    def sellingPrice(self):
        print(self.costPrice - self.discount)
        return self.costPrice - self.discount
    def display(self):
        print("Name: ", self.name)
        print("Material: ", self.material)
        print("Cost Price: ", self.costPrice)
        print("Discount: ", self.discount)
        print("Selling Price: ")
        self.sellingPrice()

prd1 = Product("Plate", "Metal", 170)
prd1.display()
print("Count: ", Product.count)
prd2 = Product("Spoon", "Plastic", 26)
prd2.display()
print("Count: ", Product.count)
prd1.sellingPrice()
prd2.sellingPrice()
print("Count: ", Product.count)
