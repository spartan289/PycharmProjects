#use the bisection functions to maintain a list in sorted order
import bisect

values=[5,7,20,25,31,36,43,47,49,67,90]

#exercise the left and right bisection routines
print(bisect.bisect(values,25))
print(bisect.bisect_left(values,25))
print(bisect.bisect_right(values,25))
#use insort to insert new items
bisect.insort(values,25)
#print(values)
#bisect can be used as an array lookup using breakpoints
breakpoints = [60,70,80,90]
gradeletters = 'FDCBA'
scores=[81,87,67,68,71,85,90]



def calcGrade(score):
    #use  the bisect function to identify cutoff points for the letter grades
    i=bisect.bisect(breakpoints,score)
    return gradeletters[i]
results = [calcGrade(score)for score in scores]
print(results)