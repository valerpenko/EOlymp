# connections = []
#
# def Pipeline(wellId1, wellId2):
#
#     wellId1 = wellId1
#     wellId2 = wellId2
#     connections.append((wellId1,wellId2))
#
# def swapPipes(con):
#     result = [(pipe[1], pipe[0]) for pipe in con]
#     return result
#
#
#v
# Pipeline(1, 2)
# Pipeline(1, 3)
# Pipeline(1, 4)
# Pipeline(2, 3)
# Pipeline(2, 4)
# Pipeline(3, 4)
#
# print(connections)
# print(swapPipes(connections))

connections = []

def Pipeline(distNum):
    temp1 = []
    temp2 = []
    for i in range(1, distNum + 1):
        temp1.append(i)
        temp2.append(i)
    for a in temp1:
        for b in temp2:
            if a != b and a < b:
                connections.append((a, b))
    #[(a, b) for a in temp1 for b in temp2 if a != b and a < b]

def swapPipes(con):
    result = [(pipe[1], pipe[0]) for pipe in con]
    return result

districtNum = int(input())

Pipeline(districtNum)
print(connections)
print(swapPipes(connections))
