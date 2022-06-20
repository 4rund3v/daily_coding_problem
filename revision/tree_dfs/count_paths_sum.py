"""

Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

"""




def count_paths_matchin_sum(root, target_sum):
    paths = []

    def helper(node,target_sum, current_path, paths):
        if node is None:
            return
        current_path.append(node.val)
        temp_sum = 0
        for i in range(len(current_path)- 1, -1, -1):
            temp_sum += current_path[i]
            if temp_sum == target_sum:
                paths.append(current_path[i:len(current_path)-1])
        # find the sums of subtrees
        helper(node.left, target_sum, current_path, paths)
        helper(node.right, target_sum, current_path, paths)        
        # backtracking
        current_path.pop()
        return
    helper(root, target_sum, [], paths)
    return len(paths)



