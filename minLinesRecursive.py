def line_Equation(p1,p2):
    a=p1[1]-p2[1]
    b=p2[0]-p1[0]
    c=(p2[1]-p1[1])*p1[0]+(p1[0]-p2[0])*p1[1]
    return a,b,c
#def points_on_line(p1,p2,p3):
#    a1, b1, c1 = line_Equation(p1,p2)
#    a2, b2, c2 = line_Equation(p2, p3)
#    a1=a1/b1
#    c1=c1/b1
#    a2 = a2 / b2
#    c2 = c2 / b2
#    if a1==a2 and c1==c2:
#        return True
#    else:
#        return False
def points_on_line(points):
    a1, b1, c1 = line_Equation(points[0],points[1])
    a1 = a1 / b1
    c1 = c1 / b1
    for i in range(2,len(points)):
        a2, b2, c2 = line_Equation(points[0],points[i])
        a2 = a2 / b2
        c2 = c2 / b2
        if a1!=a2 or c1!=c2:
            return False
    return True
def min_lines(points,lines):
    if points_on_line(points):
        return lines
    else:
        if len(points)>2:
            min_=1000
            for i in range(len(points)):
                copy = points.copy()
                copy.pop(i)
                t=min_lines(copy,lines+1)
                if t<min_:
                    min_=t
            return min_
        else:
            return lines+1
points=[[6,3],[0,0],[3,15],[12,5]]
print(min_lines(points,1))