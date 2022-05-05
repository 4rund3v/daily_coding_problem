"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
 Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

def get_minimum_steps(point_a, point_b):
    """
    Get the minimum steps from a point to another,
     given only 1 step can be taken in each direction 
    """
    x_distance = abs(point_a[0] - point_b[0])
    y_distance = abs(point_a[1] - point_b[1])
    return max(x_distance, y_distance)


def steps_to_reach(steps_array):
    total_steps = 0
    for index in range(len(steps_array)-1):
        min_steps = get_minimum_steps(point_a=steps_array[index], point_b=steps_array[index+1])
        print(f'[steps_to_reach] The number of steps from {steps_array[index]} to {steps_array[index+1]} is {min_steps}')
        total_steps += min_steps
    return total_steps


if __name__ == "__main__":
    # steps = [(0,0), (1,1), (1,2)]
    steps = [(3, 0), [5, 2], [2, 1]]
    min_steps = steps_to_reach(steps_array=steps)
    print(f"[main] The number of steps for the path [{steps}] is --> {min_steps}")