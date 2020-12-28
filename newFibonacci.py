


def calculateFibonacci(num):

    if 1 <= num <= 4:
        return 1
    else:
        k+=1
        return (calculateFibonacci(num - 1) + calculateFibonacci(num - 2)+ calculateFibonacci(num - 3) + calculateFibonacci(num - 4))

input = 20
k=0
list = [calculateFibonacci(x) for x in range(1,input)]
print(list)


