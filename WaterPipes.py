def DefinePipes():
    city = [[True,True,True,True],
            [False,True,True,True],
            [False,False,True,True],
            [False,False,False,True]]
    return city

def Reconstruct(city, region):
    newCity = [list(x) for x in zip(*city)]   # different way
    return newCity

# def SupplyTest():

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


# city = [[True,True,True,True],
#         [False,True,True,True],
#         [False,False,True,True],
#         [False,False,False,True]]
#
# result = [list(x) for x in zip(*city)]
# print(result)