def calculateFibonacci(num):
    global k
    if 1 <= num <= 4:
            #return fibRepo[num-1]
            return 1
    else:
        if  num<=len(fibRepo):
            return fibRepo[num-1]
        else:
            fibRepo.append((calculateFibonacci(num - 1) + calculateFibonacci(num - 2)+ calculateFibonacci(num - 3) + calculateFibonacci(num - 4)))
            return fibRepo[num-1]

fibRepo=[1,1,1,1]
n = int(input())
indexes=[]
for i in range(n):
    indexes.append(int(input()))
for index in indexes:
    fib=calculateFibonacci(index)
    print(fib)

