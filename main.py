# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Structures.Stacks.ArrayStack import ArrayStack


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def balanced_parentheses(expr: str):
    left ="{[("
    right = "}])"
    stack = ArrayStack()
    for char in expr:
        if char in left:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            else:
                if right.index(char) != left.index(stack.pop()):
                    return False
    return stack.is_empty()




if __name__ == '__main__':
    expr = "[]([{[({()})]}])"
    print(balanced_parentheses(expr))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
