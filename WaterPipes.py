import copy
def DefinePipes():
    city = [[True,True,True,True],
            [False,True,True,True],
            [False,False,True,True],
            [False,False,False,True]]
    return city

def dcopy(oldList):
    newList=[]
    for el in oldList:
        newList.append(copy.deepcopy(el))
    return newList

def Reconstruct(city, regNum):
    newCity = dcopy(city)
    for i in range(len(newCity)):
        newCity[i][regNum],newCity[regNum][i]=newCity[regNum][i],newCity[i][regNum]
    return newCity

def SupplyTest(city, region):
    checklist = [0] * len(city)
    checklist[region] = 1
    fr = region
    while fr != -1:
        checklist[fr] = 2
        for i in range(len(city)):
            if city[fr][i]:
                checklist += 1
        fr = checklist.index(1)
    return checklist.index(0) != -1


def Pipes(city):
    for region in range(len(city)):
        #newCity = Reconstruct(city, region)
        testActive = True
        for activeRegion in range(len(city)):
            if not SupplyTest(city, activeRegion):
                testActive = False
                break
        if testActive:
            return True
    return False

city = DefinePipes()
if Pipes(city):
    print(1)
else:
    print(0)


print(Reconstruct(city, 1))
print(SupplyTest(city, 1))



# result = [list(x) for x in zip(*city)]
# print(result)