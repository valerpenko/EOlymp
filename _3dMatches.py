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
    # returns
    # 1 match count for upgrade to build n_rest cubes
    # 2 count of remain cubes
    matches=0
    cubes_added=0
    matches += 8
    cubes_added += 1
    n_rest -= 1
    while n_rest>0 and cubes_added<width*height:
        distance=0
        matches+=5
        cubes_added+=1
        n_rest-=1
        for i in range(distance+1):
            matches += 3
            cubes_added += 1
            n_rest -= 1
        matches+=5
        cubes_added+=1
        n_rest-=1

        distance += 1
        for i in range(distance+1):
            matches += 3
            cubes_added += 1
            n_rest -= 1
    return matches, n_rest


#n=int(input())  #количество кубиков
l=[i for i in range(1,28)]
for n in l:
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
    print(n, " - ", m)


