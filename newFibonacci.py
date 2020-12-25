


def calculateFibonacci(num):
    if num > 1:
        return (calculateFibonacci(num - 1) + calculateFibonacci(num - 2))
                # + calculateFibonacci(num - 3) + calculateFibonacci(num - 4))
    else:
        return num

input = 20

list = [calculateFibonacci(x) for x in range(input)]
print(list)


