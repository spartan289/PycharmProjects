def anonymous(s,name):
    if len(s)<len(name):
        name = name[0:len(s)]
    else:
        i=0
        while len(name)!=len(s):
            name += name[i%len(name)]
            i+=1
    #length of string and name is same now
    i=0
    anonymize = ''
    while i<len(name):
        #finding the averge ascii value concatenating it to anonymize.
        anonymize += chr((ord(s[i])+ord(name[i]))//2)
        i+=1
    print(anonymize)
anonymous('helloefwefafvsdwefioefasc1321441oi21241$#%&2/~`?./<,2525','sagar2425')