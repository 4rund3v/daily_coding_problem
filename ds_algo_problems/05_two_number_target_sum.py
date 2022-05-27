def target_sum(arr, target):
    res = []
    if len(arr) <= 1:
        return []
    # Brute force was T-O(n^2) S-O(1)
    # Set/hash approach is T-O(n) S-O(n)
    # Sort and Two pointer is T-O(nlog(n)) S-O(1)
    elem = 0
    items_considered = set([])
    for elem in arr:
        remaining = target - elem
        if remaining in items_considered:
            return [remaining, elem]
        items_considered.add(elem)
    return []


if __name__ == "__main__":
    test_cases = (
            ([], 1),
            ([1], 0),
            ([1, 3, 100], 130),
            ([-1, 3, 2, 4, 87, 78, 90], 86),
            )
    for arr, target in test_cases:
        res = target_sum(arr, target)
        print(f"[main] The arr and the target is : {arr}->{target} -> target_sum {res}")
