import geometry
def Ind2Ponts(indices, allPoints):
    points=[]
    for i in indices:
        points.append(allPoints[i])
    return points
def branch(indices):
    indices.pop()
    indices[-1]+=1
    return indices
def grow(indices):
    indices.append(indices[-1]+1)
    return indices
def nextIndices(indices):
    indices[-1] += 1
    return indices
def maxUpdate(indices, maxIndices):
    if len(indices)>len(maxIndices):
        maxIndices=indices
    return maxIndices
def inrange(indices):
    if indices[-1]==len(allPoints):
        return False
    else:
        return  True
def FindBestLine(allPoints):
 indices=[]
 indices.append(0)
 indices.append(1)
 maxIndices=indices.copy()
 while(True):
   if not inrange(indices):
     indices=branch(indices)
   elif geometry.OnLine(Ind2Ponts(indices, allPoints)):
     indices=grow(indices)
     maxIndices=maxUpdate(indices, maxIndices)
   else:
     indices=nextIndices(indices)

allPoints=[[1,1],[2,2],[3,3],[2,4]]
FindBestLine(allPoints)
