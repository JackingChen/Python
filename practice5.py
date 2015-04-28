def power(x,y):
    ans =0
    if(y>0):
        ans = x*power(x,y-1)
    else:
        ans = 1
    return ans
def member(item,L):
    if(not L):
        return False
    else:
        list1 =L[0]
        if(item==list1):
            return True
        else:
            return member(item,L[1:])
        
