
# def calculateFibonacci(num):
#     global k
#     k = k+1
#     if 1 <= num <= 4:
#         return 1
#     else:
#         return (calculateFibonacci(num - 1) + calculateFibonacci(num - 2)+ calculateFibonacci(num - 3) + calculateFibonacci(num - 4))
#
# #numbers = int(input())
# input = 40
# k=0
# list = [calculateFibonacci(x) for x in range(1,input + 1)]
# print(list)
# print(k)

def calculateFibonacci(num):
    if 1 <= num <= 4:
        return 1
    else:
        return (calculateFibonacci(num - 1) + calculateFibonacci(num - 2)+ calculateFibonacci(num - 3) + calculateFibonacci(num - 4))

numbers = int(input())

list = [calculateFibonacci(x) for x in range(1,numbers + 1)]
# print(list)

search = input().split()
for num in search:
    print(list[int(num)])
