def mod2division(divident,divisor):
    pick = len(divisor)
    tmp = divident[0:pick]
    while pick <len(divident):
        if tmp[0]=='1':
            tmp = xor(divisor,tmp)+divident[pick]
        else:
            tmp = xor('0'*pick,tmp)+divident[pick]

        pick+=1
    if tmp[0]=='1':
        tmp = xor(divisor,tmp)
    else:
        tmp = xor('0'*pick,tmp)
    checkword = tmp
    return checkword
def xor(a,b):
    result = []
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
def encodeData(data,key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2division(appended_data,key)
    codeword = data+remainder
    print("verfiy", mod2division(key,key))
    print("CRC ", remainder)
    print("Encoded Data (Data+remainder) : ",codeword)
data = "100100"
key = "1101"
encodeData(data,key)

