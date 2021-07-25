# Factorial (132p)

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def recur_factorial(n):
    if n == 1:
        return 1
    else:
        return n*recur_factorial(n-1)
    
n = int(input())
print("단일 팩토리얼 : ", factorial(n))
print("재귀 팩토리얼 : ", recur_factorial(n))