def nth_smallest(num,n):
    s=sorted(num)
    if n<=len(s):
        return s[n-1]
    else:
        return"list dont have elements"
num=[2,3,5,7,8,1,2,5]
n=3
r=nth_smallest(num,n)
print("nth smallest number ",r)
