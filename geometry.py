def Line(p1,p2):
#уравнение прямой Ax+By+C=0
    return  A,B,C
def OnLine(points):
    A,B,C=Line(points[0],points[1])
    for i in range(2,len(points)):
        A1, B1, C1 = Line(points[0], points[i])
        # 2 3 5    4 6 10
        k=С1/C
        A=A*k
        B=B*k
        C=C*k
        if A!=A1 or B!=B1:
            return False
    return True

