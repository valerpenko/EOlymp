
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

#numbers = int(input())
k=0
fibRepo=dict()
input = 40
list = [calculateFibonacci(x) for x in range(1,input + 1)]
print(list)
print(k)

