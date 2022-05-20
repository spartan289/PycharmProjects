import re
def find_email(string):
    lst = re.findall('\S+@\S+', string)
    return lst
def find_year(string):
    lst = re.findall('\d{4}', string)
    return lst[-1]
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
#Entering string as email + year of birth
#Example: "email: abc@gmai.com, year: 2000"
string = input("Enter string: ")
base_price = int(input("Enter base price: "))
email = find_email(string)[0]
yob = int(find_year(string))
if leap_year(yob):
    discount = 0.18*base_price
else:
    discount = 0.10*base_price

product_price = base_price - discount + 0.15*base_price + 0.18*base_price + 0.05*base_price
interest = 0.14
processing_fee = 1000
monthly_payment = (product_price + processing_fee+ interest*product_price)/12
print("Email: ", email)
print("Birth year: ", yob)
print("Monthly payment: ", monthly_payment)



