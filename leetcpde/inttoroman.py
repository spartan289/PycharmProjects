def inttoroman(nums):
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romanliterals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    i=0
    str = ''
    while i<len(values):
        if values[i]<=nums:
            nums-=values[i]
            str+=romanliterals[i]
        else:
            i+=1
    return str
print(inttoroman(2355))