print"enter the elements"
stack=list(input())
print(stack)

def check_forempty():
    if len(stack)==0:
       print("stack is empty")
       return

def add_stack():
    print"enter the elements of stack"
    stack.append(input())
    print(stack)
    return

def insert_stack():
    add=input("enter an element to add at first")
    stack.insert(0,add)
    print(stack)
    return

def insert_index():
    num=int(input("enter the index"))
    add=input("enter an element to add at index")
    stack.insert(num+1,add)
    print(stack)
    return

def insert_atlast():
    print"enter the elements at the end of stack"
    stack.append(input())
    print(stack)
    return

def pop():
    rem=input("enter the element tobe removed")
    stack.remove(rem)
    print(stack)

def islength():
    print("length of the string is:",len(stack))

    

if __name__ == '__main__':
    
    check_forempty()
    add_stack()
    insert_stack()
    insert_index()
    insert_atlast()
    pop()
    islength()
