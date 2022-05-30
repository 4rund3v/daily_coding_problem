"""
["1", "2", "+"] -> 3
["1", "2", "3", "+", "-"] -> 1-5 -> -4

Initially empty, keep pushing the integers into the stack
when we encounter a symbol ( +, -, *, /) pop 2 and perform operation and add back to stack

"""

def evaluate_reverse_polish_notation(expression):
    """
    Time is O(n)
    Space: O(n)
    """
    symbols_map = {"+": "add", "-":"subtract", "/": "divide", "*": "multiply"}

    stack = []
    # using an array as a stack
    for char in expression:
        if char in symbols_map:
            num_2 = stack.pop()
            num_1 = stack.pop()
            res = 0
            if symbols_map[char] == "add":
                res = num_1+ num_2 
            elif symbols_map[char] == "subtract":
                res = num_1 - num_2
            elif symbols_map[char] == "divide":
                res = num_1 // num_2
            else:
                res = num_1 * num_2
            stack.append(res)
        else:
            stack.append(int(char))
    return stack.pop()


if __name__ == "__main__":
    test_cases = (
     ["1", "2", "3", "+", "-"],
     ["1", "2", "+"],
     ["5", "6", "4", "/", "+", "1", "-"],
    )
    for expression in test_cases:
        res = evaluate_reverse_polish_notation(expression=expression)
        print(f"[main] The evaluation of the expression {expression} is {res}")