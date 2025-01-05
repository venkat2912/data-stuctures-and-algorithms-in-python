#this code is better than dictionary of a element size hash map at places where you need to process a freq array, esp if 1<a[i]<10^9 because dic fails on codeforces and a hash of n size is not feasible.
def freqtab(arr):
    #arr = list(map(int, input().split()))
    arr.sort()
    ele = arr[0]
    fq = []
    n=len(arr)
    # print(arr)
    cn = 0
    for i in range(n):
        if arr[i] == ele:
            cn += 1
        else:
            fq.append([ele,cn])
            ele = arr[i]
            cn = 1
    fq.append([ele,cn])
    return fq
arr=[1,1,1,1,1,2,2,2,2,2,3,3,3,3]
print(freqtab(arr))
