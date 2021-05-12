while(True):
    s=input()
    s="'"+s+"'"
    print('{% static '+s+' %}')