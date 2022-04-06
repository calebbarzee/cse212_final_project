# STACKS

---

## What is a Stack?

Stacks are a common data structure in computer programming. Their name also gives us an indication as to what their function is. A stack is a last in first out data structure. This means that the most recently placed item on the stack will be the next used. Just like you would imagine a person would access items in a physical stack. Let's imagine a stack of vinyl records on a table. It is most convenient to grab the top vinyl off of the stack and not the bottom. A stack data structure is similar. The top item is the only accessible item in the stack. Going back to the vinyl record analogy, lets imagine we place a new vinyl on the stack. This vinyl now becomes the top of the stack and is the most accessible. This is an illustration of the last in first out principle. The most recently placed item on the stack will be the top and thus only accessible item on the stack.

## What advantages does a Stack offer?

Stacks are simple data structures, and thus are fairly easy to understand.

Stacks also have good performance in storing and accessing items. This is due to the limited functionality for storing and accessing. Because of the last in first out structure, you can only place a value to the end of a stack and access the end of the stack. This causes both operations to be O(1) in computational effeciency.

## Example

Stacks are used in many ways, one of the most common use cases is the fuction call stack. This is the memory structure used to represent what the order of execution will be. When running the example program notice the order in which functions are called and executed. The print statements help illustrate the call stack principle.

[Stacks Example](example_code/stacks_example.py)

## Problem to Solve

[Stacks Problem](problem_code/stacks_problem.py)
