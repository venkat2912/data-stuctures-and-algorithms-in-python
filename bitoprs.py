def setithbit(n,i):
    return n|1<<i
def checkithbit(n,i):
    return n & 1 << i
def clearithbit(n,i):
    return n & ~(1 << i)
def toggleithbit(n,i):
    return n ^(1 << i)
def removelastsetbit(n):
    return n &(n-1)
def powoftwo(n):
    return (n &(n-1)==0)
def countsetbitsway1(n):
    cnt=0
    while(n!=0):
        if n&1==1:
            cnt+=1
        n=n>>1
    return cnt
def countsetbitsway2(n):
    cnt=0
    while(n!=0):
        cnt+=1
        n=n&(n-1)

    return cnt
print(bin(5),bin(setithbit(5,1)))
print(bin(5),checkithbit(5,1))
print(bin(5),bin(clearithbit(5,0)))
print(bin(5),bin(toggleithbit(5,1)))
print(bin(5),bin(removelastsetbit(5)))
print(bin(5),powoftwo(4))
print(countsetbitsway1(5))
print(countsetbitsway2(5))
