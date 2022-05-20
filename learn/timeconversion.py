def timeConversion(s):
    # Write your code here
    hr = s[0:2]
    mi = s[3:5]
    sec = s[6:8]
    zone = s[8:10]

    if hr == '12' and zone == 'AM':
        hr = '00'
        return hr+':'+mi+':'+sec
    if zone == 'AM':
        return s[0:8]
    if zone == 'PM' and hr!='12':
        hr = str(int(hr) + 12)

        return hr+':'+mi+':'+sec
    else:
        return hr+':'+mi+':'+sec





if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
