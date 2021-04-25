def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, number):
    if len(stack) == size:
        print("Stack Overflow")
        return
    stack.append(number)


def pop(stack):
    if isEmpty(stack):
        print("Stack Underflow")
        return
    return stack.pop()


def peek(stack):
    if isEmpty(stack):
        print("Stack Is Empty")
        return
    else:
        n = len(stack)
        print("Peek Element is:", stack[n - 1])


def display(stack):
    print(stack)


stack = createStack()
size = int(input("Enter The Size Of Stack"))
print("Menu\n1.push(p)\n2.pop(o)\n3.peek(e)")

choice = 1
while choice != 'q':
    print("Enter Your Choice")
    ch = input()
    choice = ch.lower()
    if choice == 'p':
        push(stack, int(input("Enter Input Value")))
        display(stack)
    elif choice == 'o':
        pop(stack)
        display(stack)
    elif choice == 'e':
        peek(stack)
    else:
        print("Enter Proper Choice Or q to Quit")
