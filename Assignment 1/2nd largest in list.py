a=[12,21,34,43,13]
u=list(set(a))
u.sort()
if len(u)>=2:
    s=u[-2]
    print("SECOND LARGEST NUMBER IS",s)
else:
    print("LIST DONT HAVE")
