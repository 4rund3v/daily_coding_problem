'''
Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits.
The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. 
The code list contains groups of fruits. 
  > Both the order of the groups within the code list and the order of the fruits within the groups matter. 
    However, between the groups of fruits, any number, and type of fruit is allowable. 
  > The term "anything" is used to allow for any type of fruit to appear in that location within the group.
- - - 
Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the following purchases would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana
Write an algorithm to output 1 if the customer is a winner else output 0.
Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.
Output
** Return an integer 1 if the customer is a winner else return 0.
Note
 'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group.
 'anything' has to be something, it cannot be "nothing."
 'anything' must represent one and only one fruit.

** If secret code list is empty then it is assumed that the customer is a winner.

Example 1:
Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [orange, apple, apple, banana, orange, banana]
Output: 1
Explanation:
codeList contains two groups - [apple, apple] and [banana, anything, banana].
The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.
Example 2:
Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [banana, orange, banana, apple, apple]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in order of groups but group [banana, orange, banana] is not following the group [apple, apple] in the codeList.
Example 3:
Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [apple, banana, apple, banana, orange, banana]
Output: 0
Explanation:
The customer is not a winner as the customer has added the fruits in an order which is not following the order of fruit names in the first group.
Example 4:
Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]
Output: 0
Explanation:
The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.
'''


def check_winning_criteria(code_list: list, shopping_cart: list) -> int:
    """
    @param code_list: The code list indicating the groups and the order of items.
    @param shopping_cart: The customer shopping cart containing the items.
    @return int: 1 if the order matches the critera/ 0 otherwise.

    Conditions:
       > Return 1 when the code list is empty.
       > match the groups with the items and retain the order
    """
    is_winner = 0
    if not code_list:
        is_winner = 1
        return is_winner
    group_count = len(code_list)
    item_count = len(shopping_cart)
    
    if item_count < group_count:
        return is_winner
    
    group_index = 0
    cart_index = 0

    while group_index < group_count and cart_index + len(code_list[group_index]) <= item_count:
        print(f"[check_winning_criteria] The group under consideration is :: {group_index}->{code_list[group_index]}")
        group_matched = True
        for index, group_item in enumerate(code_list[group_index]):
            print(f"[check_winning_criteria] The group_item under consideration is :: {index}->{group_item}")
            if shopping_cart[ cart_index +  index ]  != group_item and group_item != 'anything':
                group_matched = False
                break
        if group_matched:
            print(f"Group matched : [{code_list[group_index]}] -> cart index is {cart_index}")
            cart_index += len(code_list[group_index])
            group_index += 1
        else:
            cart_index += 1
    is_winner = 1 if group_index == group_count else 0
    return is_winner
    


if __name__ == "__main__":
    test_cases = [(
        [['apple', 'apple'], ['apple', 'apple', 'banana']],
        ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
            ), 
        (
        [['apple', 'apple'], ['banana', 'anything', 'banana']],
        ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
            )]
    for test_case in test_cases:
        code_list, shopping_cart =  test_case
        print(f"[main] The code list is ::: {code_list}")
        print(f"[main] The shopping cart is ::: {shopping_cart}")
        is_winner = check_winning_criteria(code_list, shopping_cart)
        print(f"[main] The result is :: {is_winner}")
    print("End of Program")
