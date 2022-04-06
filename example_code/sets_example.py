def main():
    """
    Python has a built in set data structure so we will be using that for this example.
    If you have questions about python's set data structures refer to their official online documentation.

    """

    # To initialize a set data structure in python simply assign a variable to type set()
    my_set = set()

    # add an item to the set

    # Remember a set is unordered and does not allow duplicates.
    # These attributes of a set can be advantageous if used in the correct circumstance.
    my_set.add("item 0")
    print(f"current contents of the set are: {my_set}")
    # add multiple items to the set
    for i in range(1, 10):
        my_set.add(f"item {i}")
    print(f"current contents of the set are: {my_set}")
    # notice that although the items were added in numerical ascending order,
    # the set does not maintain this order.

    # lookup an item in the set
    if "item 0" in my_set:
        print("item 0 was found in set")
    else:
        print("item 0 was not found in set")
    # remove an item from the set
    my_set.remove("item 0")
    print(f"current contents of the set are: {my_set}")
    # try looking up 0 again in the set
    if "item 0" in my_set:
        print("item 0 was found in set")
    else:
        print("item 0 was not found in set")
    # remove the rest of the items from the set
    for i in range(1, 10):
        my_set.remove(f"item {i}")
    print(f"current contents of the set are: {my_set}")


if __name__ == "__main__":
    main()
