import geometry
def FindBestLine(allPoints):
 points=[]
 points.append(allPoints[0])
 points.append(allPoints[1])
 maxpoints=points.copy()
 while(True):
   # if (!inrange(points):
   if not range(points):
     point=branch(point)
   elif geometry.OnLine(points):
     points=grow(points)
     update(points, maxpoints)
   else:
     points=next(points)


