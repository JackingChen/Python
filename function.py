def double(x):
    """The function doubles a number"""
    # This is a comment

    return 2*x

""" This is also a comment"""

def a_or_an(name):
    """ This function put a or an in front of the input string"""

    if name[0] == 'a' or name[0] == 'e' or name[0] == 'i' or \
       name[0] == 'o' or name[0] == 'u' :
        return "an " + name
    elif len(name)>10:
        return "word too long"
    else :
        return "a "+ name
def even(num):
    """ The function is used to identify whether input number is even or odd"""
    if num % 2 ==0:
        return "true"
    else:
        return "false"
def absolute(num):
    if num<0:
        return -num
    else :
        return num
mylist = range(0,477,7)
newlist = [mylist[:4],mylist[4:19],mylist[9:32:2]]
S = [1,1,2,2,5,2,2,1,1]
def sum(mylist):
    #The function is to sum all of the content in a list
    total = 0
    for number in mylist:
        total += number ;
    return total


def count(L,x):
    """The function is to count how many times number x appears in the list L"""
    count=0
    for i in L:
        if x == i:
            count +=1
    return count

def sumsum(listlist):
    """ The function is used to sum all the content in a list of lists"""
    count=0
    for i in listlist:
        count = sum(i)
    return count
def harmonic(n):
    summation=0;
    for i in range(1,n):
        summation +=1/i
    return summation
def palindrome(L):
    #odd number of the list
    check =1;
    length = len(L)/2;
    length=int(length)
    if len(L)%2==0:
        for i in range(0,length):
            if(L[i] != L[-1-i]):
                check =0
    if check == 0:
            return "false"
    else:
            return "true"
def supercount(L,x):
    count_sum=0
    for lists in L:
        count_sum+=count(lists,x)
    return count_sum
def find(DNA, pattern):
    """ return the index of the pattern found in DNA"""
    IndexList=[]
    for i in range(0,len(DNA)):
        if DNA[i:i+len(pattern)]==pattern:
            IndexList.append(i)
    
def findcoding(DNA):
    """ find the part between "TAG""TAA""TGA" in a DNA series"""
    for i in len(DNA):
        #if the next 3 symbol are a codon
        if DNA[i:i+3]=="ATG":
            #The starting position of the next codon
            j=i+3
            while DNA[j:j+3] != "TAG" and\
                  DNA[j:j+3] != "TAA" and\
                  DNA[j:j+3] != "TGA":
                #move three positions to the next codon
                j=j+3
    return DNA[i:j+3]
