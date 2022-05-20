import cv2
def printthelowest(num):
    return (num//10)*10
angelina = cv2.imread('ash.jpg')
dim = (150,42)
angelina = cv2.resize(angelina,dim,interpolation=cv2.INTER_AREA)

for i in range(len(angelina)):
    for j in range(len(angelina[0])):
        ascii_char = printthelowest(sum(angelina[i][j])//6)
        if ascii_char<33:
            ascii_char=33
        if 127<=ascii_char<=160:
            if ascii_char<143:
                ascii_char=126
            else:
                ascii_char=161
        # a.write(chr(ascii_char))
        print(chr(ascii_char), end='')
    print()

