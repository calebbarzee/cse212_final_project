def main():
    """In this stack data structure example we'll be using an python list that we'll treat like a stack. 

    It's important to note that in python you can reference the last index in a list with "[-1]".
    Another way of doing this is by using the len() method Ex. "[len(stack)-1]"
    """

    # initialize the stack
    new_stack = []
    # add an item to the stack
    # remember you can only add and remove a value from the top of the stack
    new_stack.append("item 1")
    print("item 1 added")
    # add multiple items to the stack
    for i in range(2, 10):
        new_stack.append(f"item {i}")
        print(f"item {i} added")
    # pull an item from the stack
    print(f"{new_stack[-1]} removed")
    new_stack.pop(-1)
    # pull the rest of the items from the stack
    for i in reversed(range(len(new_stack))):
        print(f"{new_stack[i]} removed")
        new_stack.pop(i)


if __name__ == "__main__":
    main()
