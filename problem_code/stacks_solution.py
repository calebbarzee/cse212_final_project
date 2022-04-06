def main():
    """
    In the previous example we saw how stacks function with a last in first out paradigm.
    Try to use this concept to call the functions in the correct order to spell the secret message.
    """
    my_stack = Stack()
    secret_message(my_stack)


def d_function(my_stack):
    my_stack.add_item("d")


def e_function(my_stack):
    my_stack.add_item("e")


def h_function(my_stack):
    my_stack.add_item("H")


def l_function(my_stack):
    my_stack.add_item("l")


def o_function(my_stack):
    my_stack.add_item("o")


def r_function(my_stack):
    my_stack.add_item("r")


def w_function(my_stack):
    my_stack.add_item("W")


def space_function(my_stack):
    my_stack.add_item(" ")


def secret_message(my_stack):
    # Solution code is provided below.
    d_function(my_stack)
    l_function(my_stack)
    r_function(my_stack)
    o_function(my_stack)
    w_function(my_stack)
    space_function(my_stack)
    o_function(my_stack)
    l_function(my_stack)
    l_function(my_stack)
    e_function(my_stack)
    h_function(my_stack)
    for i in reversed(range(len(my_stack.stack_items))):
        print(my_stack.remove_item())


class Stack():
    def __init__(self):
        self.stack_items = []

    def add_item(self, item):
        """
        This method adds an item to the end of our make believe stack.
        """
        self.stack_items.append(item)

    def remove_item(self):
        """
        This method returns and removes the top item on the stack.
        """
        top_item = self.stack_items[-1]
        self.stack_items.pop(-1)
        return top_item


if __name__ == "__main__":
    main()
