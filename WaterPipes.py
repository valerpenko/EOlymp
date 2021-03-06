def DefinePipes():
    # city = [[True,True,True,True],
    #         [False,True,True,True],
    #         [False,False,True,True],
    #         [False,False,False,True]]
    citySize=int(input())
    city = [[False for i in range(citySize)] for j in range(citySize)]
    for i in range(citySize):
        lst=input().split()
        rowNum=int(lst.pop(0))
        for el in lst:
            city[rowNum][int(el)-1]= True
    return city

def Reconstruct(city, regNum):
    newCity=[]
    for row in range(len(city)):
        newCity.append([])
        for col in range(len(city)):
            newCity[row].append(city[row][col])

#    newCity = dcopy(city)
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

# Ctrl - D or Ctrl - Z
def DataInput():
    citySize =int(input())
    temp = []
    while True:
        try:
            line =input().split()
        except EOFError:
            break
        temp.append(line)
    pipeline = [list(map(int,i)) for i in temp]
    return citySize, pipeline


# DataInput()
# print(DataInput())
city = DefinePipes()
if CityWaterSupplyExist(city):
    print(1)    #city is well water supplied
else:
    print(0)    #city is not water supplied
