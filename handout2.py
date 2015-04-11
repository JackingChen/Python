import time
def neighbors(array,rows,columns):
    """this returns the numbers of neighbors of a point"""
    row = len(array)
    column = len(array[0])
    count=0
    #the situation on the first and last of row, column. 
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
def nextgen(array):
    row = len(array)
    column = len(array[0])
    output=[]
    #output.extend(array)
    #print(start)
    #print(output)
    for i in range(len(array)):
        array_o=[]
        for j in range(len(array[i])):
            status = neighbors(array,i,j)
            if(array[i][j]==0):
                if(status == 3):
                    array_o.append(1)
                else:
                    array_o.append(0)
            else :
                if(status<2 or status>3):
                    array_o.append(0)
                else:
                    array_o.append(1)
        output.append(array_o)
    #print(output)
    #print(start)
    return output
def print_life(array):
    output=""
    row = len(array)
    column = len(array[0])
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if(array[i][j]==0):
                output = output+" "
            else:
                output = output+"#"
        output = output + "\n"
    output = output + "\n"
    print(output)
def check_edge(array):
    row = len(array)
    column = len(array[0])
    if(row>50 or column>50):
        return array
    change_u=0
    change_r=0
    change_d=0
    for i in range(column):
        if(array[0][i]==1):
            change_u = 1
    for i in range(row):
        if(array[i][column-1]==1):
            change_r = 1
    for i in range(column):
        if(array[row-1][i]==1):
            change_d = 1
    if(change_u==1):
        array.insert(0,[0]*column)
    if(change_r==1):
        for i in range(row):
            array[i].append(0)
    if(change_d==1):
        array.append([0]*column)
    return array
def life(array,years):
    print("\n"*100)
    print("The initial generation")
    
    print_life(array)
    time.sleep(1)
    #extend array and assign to output
    output = array[:]
    for i in range(len(array)):
        array[i].append(0)
    output.append([0]*len(array[0]))
    output.insert(0,[0]*len(array[0]))
    #print(output)
    #print(len(output))
    #start next generation
    for i in range(1,years+1,1):
        #check if expand is needed
        output = check_edge(output)
        output = nextgen(output)
        print("\n"*100)
        print("Generation %d:" % i)
        print_life(output)
        time.sleep(0.1)
    print(len(output))
    print(len(output[0]))
    return output
start = [
[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0], 
[0, 1, 1, 1, 0], 
[0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0]
]
tumbler = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
face = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
glider_gun = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
 0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,\
 0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,\
 0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
[0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,\
 0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,\
 0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,\
 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,\
 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,\
 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
"""
x = [0]*38
for i in range(20):
    glider_gun.append(x)
print(x)"""
#life(start, 10)
#life(tumbler, 60)
#life(face, 60)
life(glider_gun, 500)
#print (a)
