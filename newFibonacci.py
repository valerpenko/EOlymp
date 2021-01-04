


def calculateFibonacci(num):
    k = 0
    if 1 <= num <= 4:
        return 1
    else:
        k+=1
        return (calculateFibonacci(num - 1) + calculateFibonacci(num - 2)+ calculateFibonacci(num - 3) + calculateFibonacci(num - 4))

numbers = int(input())# input = 20
# k=0
list = [calculateFibonacci(x) for x in range(1,numbers + 1)]
print(list)

x, y, z = input().split()
for i in range(0, len(list)):
    print(list[int(x)])
    print(list[int(y)])
    print(list[int(z)])
    break