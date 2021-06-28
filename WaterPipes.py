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
    #temp = newCity[regNum]
    for i in range(len(newCity)):
        newCity[i][regNum],newCity[regNum][i]=newCity[regNum][i],newCity[i][regNum]
    return newCity

def SupplyTest(newCity,region):
    checklist = []
    count = 0
    #newCity = Reconstruct(city, region)
    for row in newCity:
        for item in row:
            if item == region and item == True:
                count+=1
        if count > 1:
            checklist.append(True)
        else:
            break
    return checklist


def Pipes(city):
    for region in range(len(city)):
        newCity = Reconstruct(city, region)
        testActive = True
        for activeRegion in range(len(city)):
            if not SupplyTest(activeRegion):
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


print(Reconstruct(city, 2))
print(SupplyTest(2))



# result = [list(x) for x in zip(*city)]
# print(result)