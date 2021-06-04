# def DefinePipes():
#     city = [[True,True,True,True],
#             [False,True,True,True],
#             [False,False,True,True],
#             [False,False,False,True]]
#     return city
#
# def Reconstruct(city, regNum):
#     newCity = DefinePipes()
#     temp = newCity[regNum]
#     column = []
#     for row in city:
#         column.append(row[regNum])
#     newCity[regNum] = column
#     # newCity[regNum + 1] = temp
#     return newCity
#
# def SupplyTest(region):
#
#
# def Pipes(city):
#     for region in range(len(city)):
#         newCity = Reconstruct(city, region)
#         testActive = True
#         for activeRegion in range(len(city)):
#             if not SupplyTest(activeRegion):
#                 testActive = False
#                 break
#         if testActive:
#             return True
#     return False
#
# city = DefinePipes()
# if Pipes(city):
#     print(1)
# else:
#     print(0)
#
#
# # city = [[True,True,True,True],
# #         [False,True,True,True],
# #         [False,False,True,True],
# #         [False,False,False,True]]
#
#
# # def reconstruct(city, regNum):
# #     newCity = city
# #     temp = newCity[regNum]
# #     column = []
# #     for row in city:
# #         column.append(row[regNum])
# #     newCity[regNum] = column
# #     newCity[regNum + 1] = temp
# #     return newCity
#
#
#
# # def reconstruct(city, regNum):
# #     newCity = city
# #     for i in range(len(newCity[regNum])):
# #         for j in range(len(newCity)):
# #             newCity[i][j], newCity[j][i] = newCity[j][i], newCity[i][j]
# #             return newCity
# #
# # print(reconstruct(city,0))
#
# # result = [list(x) for x in zip(*city)]
# # print(result)