from turtle import*
angle =30
speed(0)
left(90)
def tree(trunkLength, currentDepth, maxiumDepth):
    forward(trunkLength)
    if(currentDepth<maxiumDepth):
        left(angle)
        tree(trunkLength/2,currentDepth+1,maxiumDepth)
        back(trunkLength/2)
        right(angle)
        tree(trunkLength/2,currentDepth+1,maxiumDepth)
        back(trunkLength/2)
        right(angle)
        tree(trunkLength/2,currentDepth+1,maxiumDepth)
        back(trunkLength/2)
        left(angle)
    if(currentDepth==0):
        back(trunkLength)
    return
