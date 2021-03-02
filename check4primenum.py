
def prime(num):
    for x in range(2,num//2+1):
        if num % x == 0:
            return False
    else:
        return True

for i in range (2,101):
    print(prime(i),i)