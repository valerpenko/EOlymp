import math
# def matchesForUpgrade(n_rest,width,height):
#     # returns
#     # 1 match count for upgrade to build n_rest cubes
#     # 2 count of remain cubes
#     matches=0
#     for row in range(height):
#         for col in range(width):
#             if row==0:
#                 if col==0:
#                     matches+=8
#                 else:
#                     matches+=5
#             else:
#                 if col==0:
#                     matches+=5
#                 else:
#                     matches+=3
#             n_rest-=1
#             if n_rest==0:
#                 return matches, 0
#     return matches, n_rest
def matchesForUpgrade(n_rest,width,height):
    # trying to build 1 layer of cubes under width x height plateu
    # returns
    # 1 match count for upgrade to build n_rest cubes
    # 2 count of remain cubes
    matches=8
    cubes_added = 1
    n_rest -= 1
    if cubes_added==width*height or n_rest==0:
        return matches, n_rest
    distance=0
    while cubes_added<width*height:
        matches+=5
        cubes_added+=1
        n_rest-=1
        if cubes_added==width*height or n_rest==0:
            return matches, n_rest
        #=====================
        for i in range(distance):
            matches += 3
            cubes_added += 1
            n_rest -= 1
            if cubes_added==width*height or n_rest==0:
                return matches, n_rest
        #====================
        matches+=5
        cubes_added+=1
        n_rest-=1
        if cubes_added==width*height or n_rest==0:
            return matches, n_rest
        #======================
        distance += 1
        for i in range(distance):
            matches += 3
            cubes_added += 1
            n_rest -= 1
            if cubes_added==width*height or n_rest==0:
                return matches, n_rest
        #======================
    return matches, n_rest


n=int(input())  #количество кубиков
# l=[i for i in range(1,66)]
m_prev=0
k=math.floor(math.pow(n,1./3.))
m_kcube=3*(k+1)*(k+1)*k
m_level=0
m_back=0
m_facade=0
n_rest=n-k*k*k
if n_rest>0:  # next level
    m_level, n_rest= matchesForUpgrade(n_rest, k, k)
    if  n_rest>0: #   next back
        m_back, n_rest = matchesForUpgrade(n_rest, k, k+1)
        if  n_rest>0: # next facade
            m_facade, n_rest = matchesForUpgrade(n_rest, k+1, k + 1)
m=m_kcube+m_level+m_back+m_facade
#print(m)
print(m)
m_prev=m


