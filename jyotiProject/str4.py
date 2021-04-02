
from string import Template
import datetime
#using template strings

the_str="the quick brown $animal $action over the lazy dog"
the_template=Template(the_str)
output_str=the_template.substitute(animal="fox",action="jumped")
print(output_str)
args={
    "animal":"cow",
    "action":"walked"
}
output_str=the_template.substitute(args)
print(output_str)

#using str.format()
foo="foo"
bar=123
print("output:{}, {}".format(foo,bar))
print("output {1}, {0}".format(foo,bar))
print("output {var1}, {var2}".format(var1=foo,var2=bar))
print("output:{var2:x},{var2:X},{var1}".format(var1=foo,var2=bar))


#using interpolation with f-strings in python 3.6
product="widget"
price=19.99
tax=0.07
nyd=datetime.datetime(2019,1,1)
print(f"{product} has a {price},with tax {tax:.2%}the total is {round(price+(price*tax),2)}")
print(f"but only on {nyd: %B %d %Y}")
