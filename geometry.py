def Line(p1,p2):
# уравнение прямой Ax+By+C=0
    A = p1[1] - p2[1]
    B = p2[0] - p1[0]
    C = p1[0] * p2[1] - p2[0] * p1[1]
    return  A,B,C
def OnLine(points):
    A,B,C = Line(points[0],points[1])
    for i in range(2,len(points)):
        A1, B1, C1 = Line(points[0], points[i])
        # 2 3 5    4 6 10
        if  A!= 0:
            k = A1 / A
        else:
            k = B1 / B
        A=A*k
        B=B*k
        C=C*k
        if A!=A1 or B!=B1:
            return False
    return True
