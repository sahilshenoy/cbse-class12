#Menu Driven for Pushing and Poping in a stack containing Book Details

def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False


def Push(stk,item):
    stk.append(item)
    top = len(stk)-1


def Pop(stk):
    if isEmpty(stk):
        print("Underflow!!")
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = 0
        else:  
            top = len(stk)
            print("Popped item is " + str(item))

def Display(stk):
    if isEmpty(stk):
        print("Underflow!!")
    else:
        top = len(stk) -1
        print("Elements in the stack are: ")
        for i in range(top,-1,-1):
            print(str(stk[i]))


# Menuing it up (MAIN)
stk = eval(input("Enter the Stack in the form of List: "))
print("1. PUSH")
print("2. POP")
print("3. DISPLAY")
top = 0

while True:
    n = int(input("Enter the opertion you want to perform: "))

    if n == 1:
        x = input("Enter the thing which you want to append: ")
        Push(stk,x)
    elif n == 2:
        Pop(stk)
    elif n == 3:
        Display(stk)
    else:
        print("Wrong Choice!!")

    choice = input("Whether you want to continue or not!! (y/n): ")
    if choice == 'y':
        continue
    else:
        break