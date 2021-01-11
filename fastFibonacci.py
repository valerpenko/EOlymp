
def calculateFibonacci(num):
    global k
    k = k + 1
    #k = 0
    if 1 <= num <= 4:
        if num in fibRepo.keys():
            return fibRepo[num]
        else:
            fibRepo[num]=1
            return 1
    else:

        if num in fibRepo.keys():
            return fibRepo[num]
        else:
            fibRepo[num]=(calculateFibonacci(num - 1) + calculateFibonacci(num - 2)+ calculateFibonacci(num - 3) + calculateFibonacci(num - 4))
            return fibRepo[num]

def digitLimil(lim):
    string = str(lim)
    if len(string) <= 2008:
        return True
k=0
fibRepo=dict()
#inp = 40
inp = int(input())
list = [calculateFibonacci(x) for x in range(1,inp + 1)]
# print(list)
# print(k)

countList = {count:fibNum for count, fibNum in enumerate(list,1)}
print(countList)

n = int(input())
search = input().split()[:n]
#search = input().split()
for num in search:
    print(countList[int(num)])

