#Patterns

def aababc():
    '''
    A
    A B
    A B C
    A B C D
    A B C D E

    '''
    n = int(input("Enter the Number of Lines: "))
    for i in range (65,65+n):
        for j in range(65,i+1):
            print(chr(j), end=" ")
        print()

aababc()
print()

def abacba():
    '''
    A
    B A
    C B A
    D C B A

    '''
    n = int(input("Enter the Number of Lines: "))
    for i in range (65,65+n):
        for j in range(i,64,-1):
            print(chr(j), end=" ")
        print()

abacba()
print()