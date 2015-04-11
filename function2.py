creatures = [ [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 1] ]
array = [ [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 1] ]
bigArray = [ 
[0, 1, 1, 1, 1, 0, 0, 0], 
[1, 0, 0, 0, 0, 1, 0, 1], 
[0, 0, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 1, 0, 1, 1], 
[0, 0, 0, 0, 0, 1, 0, 1], 
[1, 1, 1, 0, 0, 0, 1, 0], 
[1, 0, 1, 0, 0, 0, 0, 1]
]
start = [[1, 0, 0, 1], [0, 0, 0, 1], [1, 0, 0, 0], [1, 1, 1, 1]]
def change(array):
    """This function changes the 0's to 1's in an array"""
    row = len(array)
    column = len(array[1])

    for i in range(row):
        for j in range(column):
            if(array[i][j]==1):
                array[i][j]=0
            else:
                array[i][j]=1
    return array
                
def change(array,mutable='T'):
    """This function changes the 0's to 1's in an array"""
    row = len(array)
    column = len(array[1])

    for i in range(row):
        for j in range(column):
            array[i][j] = 1 - array[i][j]
                
    return

def change(array,mutable='F'):
    """This function changes the 0's to 1's in an array"""
    output = []

    row = len(array)
    column = len(array[0])
    for rows in range(row):
        newrow =[]
        for columns in range(column):
            newrow.append(1 - array[rows][columns])

        output.append(newrow)

    return output
def neighbors(array,rows,columns):
    """this returns the numbers of neighbors of a point"""
    row = len(array)
    column = len(array[0])
    count=0
    left_r = rows-1
    right_r = rows+2
    left_c =columns-1
    right_c =columns+2
    if(left_r < 0):
        left_r=0
    if(left_c < 0):
        left_c=0
    if(right_r > row):
        right_r=row
    if(right_c > column):
        right_c=column
    for i in range(left_r,right_r,1): 
        for j in range(left_c,right_c,1):
            if(i==rows and j==columns):
                continue
            else:
                if(array[i][j]==1):
                    count+=1
            #print (i , j  )
    return count
import copy
def nextgen(array):
    row = len(array)
    column = len(array[0])
    output=[]
    #output.extend(array)
    #print(start)
    #print(output)
    for i in range(row):
        array_o=[]
        for j in range(column):
            status = neighbors(array,i,j)
            if(array[i][j]==1 and (status >3 or status < 2)):
                array_o.append(0)
            elif(array[i][j]==0 and status ==3):
                array_o.append(1)
            else :
                array_o.append(array[i][j])
        output.append(array_o)
    #print(output)
    #print(start)
    return output
import time
def little_animation():
    sec =0
    while sec<10:
        print("\n"*100)
        print(sec)
        time.sleep(1)
        sec+=1

