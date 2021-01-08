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

def swapPipes(con):
    result = [(pipe[1], pipe[0]) for pipe in con]
    return result

def Pipeline(distNum):
    for i in range(1, distNum + 1):
        if i != i + 1 and i < i + 1:
                connections.append((i, i + 1))
    #[connections.append((i, i + 1)) for i in range(1, distNum + 1) if i != i + 1 and i < i + 1]

districtNum = int(input())

Pipeline(districtNum)
print(connections)
print(swapPipes(connections))
