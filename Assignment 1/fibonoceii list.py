def fibonacci_upto(limit):
    f=[]
    a.b=0,1
    while a<=limit:
        f.append(a)
        a.b=b,a+b
    return f
limit=100
fn=fibonacci_upto(limit)
print(fn)
