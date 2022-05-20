#determine whether a righ angled triangle can be formed with the given sides
def squares3(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    else:
        return False

def countA(s):
    cnt = 0
    for i in range(len(s)):
        if s[i]=='A':
            cnt += 1
    return cnt
def oddsum(s):
    sum = 0
    for i in s:
        if i%2 != 0:
            sum += i
    return sum
print(oddsum([1, 2, 3, 1, 4]))
# We are given a list called student_data, consisting of dictionaries, with each dictionary having two keys, “name” which is a string and “rollno” which is an integer.
# Write a function sort_dict(student_data), which returns a new list sorted by roll number.

def sort_dict(student_data):
    return sorted(student_data, key=lambda x: x['rollno'])
print(sort_dict([{"name": "a", "rollno": 3}, {"name": "b", "rollno": 2}, {"name": "c", "rollno": 1}]))

class LinearEquation:
    def __init__(self,a=1,b=1,c=0):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def __str__(self):
        if self.b<0:
            return str(self.a)+'x - '+str(-self.b)+'y = '+str(self.c)
        return str(self.a)+'x + '+str(self.b)+'y = '+str(self.c)
    def __repr__(self):
        if self.b<0:
            return str(self.a)+'x - '+str(-self.b)+'y = '+str(self.c)
        return str(self.a)+'x + '+str(self.b)+'y = '+str(self.c)

    def isparallel(self, other):
        if self.a * other.b == self.b * other.a :
            if self.b * other.c != self.c * other.b :
                return True
        return False
    def intersects(self, other):
        if self.a * other.b != self.b * other.a :
            return True
        return False
    def overlaps(self,other):
        if self.a * other.b == self.b * other.a :
            if self.b * other.c == self.c * other.b :
                return True
        return False

    def __add__(self, other):
        return LinearEquation(self.a + other.a, self.b  + other.b, self.c + other.c)
a = LinearEquation(1, -1, 1);
print(str(a))
assert str(a) == '1.0x - 1.0y = 1.0';
assert repr(a) == '1.0x - 1.0y = 1.0';
a = LinearEquation(1, 2, 3);
b = LinearEquation(12, 4, 16);
c = a + b;
assert c.a == 13;
assert c.b == 6;
assert c.c == 19
print(c)

def strip_string(arg: str):
    ans = ''

    for i in arg:
        if i.isalnum() or i == '_' or i == '/':
            ans += i
        else:
            ans += '_'
    # remove consecutive underscores
    res = ''
    iterate = 0
    for i in ans:
        if i != '_':
            res += i
        elif i=='_' and iterate == 0:
            res += i
            iterate = 1
        elif i == '_' and res[-1] != '_':
            res += i
    return res
print(strip_string("     Ab 4/5        (t) ")     )