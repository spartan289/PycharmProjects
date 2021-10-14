def maximumMeetings(n,start,end):
    pair = zip(end,start)
    pair = sorted(pair)
    prev = pair[0][0]
    c=1
    for i in range(1,n):
        if pair[i][1]>prev:
            c+=1
            prev = pair[i][0]
    print(c)
maximumMeetings(6,[1,3,0,5,8,5],[2,4,6,7,9,9])
