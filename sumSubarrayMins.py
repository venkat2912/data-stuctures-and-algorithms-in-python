# when looking for nse if search for strictly smaller element while when looking for prev smallest element we look for equal or smaller
    # consider a array 2 5 6 7 8 9 2
    # 2 
    #2 5 
    # 2 5 6
    # 2 5 6 7 
    # 2 5 6 7 8 
    # 2 5 6 7 8 9 
    # 2 5 6 7 8 9 2 even this 2 will be taken as it is not the smaller one
    #now
    # 9 2
    # 8 9 2
    # 7 8 9 2
    # 6 7 8 9 2
    # 6 7 8 9 2
    # 5 6 7 8 9 2 till this array all is good but after that
    # 2 5 6 7 8 9 2 this is a repetition and thus to avoid this when looking back we will stop at the equal element and not go for the smallest further.
mod=10**9+7
def nextsmallelement(arr,n):
    nse = [0] * n
    #pse = [0] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()

        if len(st) == 0:
            nse[i] = n
            st.append(i)


        else:
            nse[i] = st[-1]
            st.append(i)
    return nse
def prevsmallesteqelement(arr,n):
    pse = [0] * n
    st = []

    for i in range(n):
        while st and arr[i] < arr[st[-1]]:
            st.pop()

        if len(st) == 0:
            pse[i] = -1
            st.append(i)


        else:
            pse[i] = st[-1]
            st.append(i)
    return pse    

def sumSubarrayMins(arr):
    n = len(arr)
    nse = nextsmallelement(arr,n)
    pse = prevsmallesteqelement(arr,n)
    ans = 0
    # print(pse,nse)
    for i in range(n):
        ans += ((i - pse[i]) * (nse[i] - i)) * arr[i]
    return ans % mod
print(sumSubarrayMins([3,1,2,4]))




