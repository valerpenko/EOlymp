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

def SupplyTest(city, region):  # True - all city water supplied     False - otherwise
    checklist = [0] * len(city)
    checklist[region] = 1
    fr = region
    while True: # fr != -1:
        checklist[fr] = 2
        for i in range(len(city)):
            if city[fr][i]:
                checklist[i] += 1
        try:
            fr = checklist.index(1)
        except ValueError:
            break
    try:
        checklist.index(0)
        return False
    except ValueError:
        return True

def GoodWaterPipes(city):  #True - for well water supplied city False - otherwise
        for activeRegion in range(len(city)):
            if not SupplyTest(city, activeRegion):
                return False
        return True

def CityWaterSupplyExist(srcCity):
    for region in range(len(srcCity)):
        newCity=Reconstruct(srcCity, region)
        if GoodWaterPipes(newCity):
            return True
    return False

city = DefinePipes()
if CityWaterSupplyExist(city):
    print(1)    #city is well water supplied
else:
    print(0)    #city is not water supplied
