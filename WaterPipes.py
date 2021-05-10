


def DefinePipes():
    city = [[True,True,True,True],
            [False,True,True,True],
            [False,False,True,True],
            [False,False,False,True]]
    return city

def Reconstruct():
    city = DefinePipes()
    newCity = [list(x) for x in zip(*city)]
    return newCity

# def SupplyTest():

def Pipes(city):
    for region in range(len(city)):
        newCity = Reconstruct(region)
        testActive = True
        for activeRegion in range(len(city)):
            if not SupplyTest(activeRegion):
                testActive = False
                break
        if testActive:
            return True
    return False



waterSupply = DefinePipes()
if Pipes(waterSupply):
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