# How the code 
# A string with dummy characters to handle even length palindrome.
#Iterate over the new string and consider it to be a center and expand from it in left and right direction till mirror characters from this center are same and keep incrementing array p[i] for it.
# now the right limit to which the palindrome eexist  has expanded is rightbound. 
# now for any unchecked character of string which lies in the bound will get its value from p[mirror]
#eg (N at 7 is 1 because N at 5 after calculation was and as we are in a palindrome so conditions around mirror elements will be same)
#Now for any i which is less than right bound expansion is done from i+p[i]+1 in right and i-p[i]+1 in left that is if we know it is a palidrome of three we check just beyond that and if
# it goes outside the rightbound then we get the new rightbound and also center shifts to the max value.


st=[#,N,#,B,#,N,#,N,#,B,#, R, $]
id=[0,1,2,3,4,5,6,7,8,9,10,11,12]
p= [0,1,0,3,0,1,4,1,0,1,0 ,1 ,0]
def manacher(s):
    num=len(s)
    if num<1:
        return s
    st = '#' + '#'.join(s) + '#'  
    n=len(st)
    p=[0]*n
    center=0
    rightboundary=0
    for i in range(n):

        mirroridx=center-(i-center)
        if (i<rightboundary):
            p[i]=min(rightboundary-i,p[mirroridx])
        right=i+(p[i]+1)
        left=i-(p[i]+1)
        #print(left,right)
        while right<n and left>=0 and st[left]==st[right]:
            #print(st[left],st[right])
            p[i]+=1
            right+=1
            left-=1
        if i+p[i]>rightboundary:
            center=i
            rightboundary=i+p[i]
    leng=max(p)
    #print(leng)
    idx=p.index(leng)
    #print(idx,p,st)
    return ''.join(st[idx-leng+1:idx+leng].split('#'))







print(manacher('babad'))


