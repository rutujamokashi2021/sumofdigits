def getSum(n):
    digit = str(n)
    num = list(map(int,digit.strip()))
    return sum(num)
n = 12345
print(getSum(n))