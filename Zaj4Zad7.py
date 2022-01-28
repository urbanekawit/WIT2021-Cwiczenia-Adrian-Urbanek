def count_chars(x,d):
    y=len(x)
    z=0
    while z<y:
        d[x[z]]=len(x[z])
        z=z+1
    return(x,d)
x=input("Napisz cos: ")
d={}
print(count_chars(x,d))
