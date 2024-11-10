def abs_diff_between_sum_and_sum_of_squares(a:int, b:int) -> int:
    '''
    Given two integers, find the absolute difference between 
    their sum and the sum of their squares.
    Eg. 
    a, b = 2,3 
    sum is 5
    sum of squares is 13 
    absolute difference is 8

    Args:
        a - int : The first integer.
        b - int : The second integer.

    Returns:
        int: absolute difference between the sum and the sum of squares
    '''

    # sum of 2 numbers
    sum_ab = a+b

    # sum of squares
    sum_sq = a**2+b**2

    # absolute value
    abs_diff = abs(sum_ab-sum_sq)

    # return
    return abs_diff


def swap_except_middle_three(s: str) -> str:
    '''
    Given an odd-length string, 
    swap the parts before and after the middle three characters,
    while keeping the middle three characters in place.

    Assume the string has at least 5 characters.

    Examples:
        "firstabclast1" -> "last1abcfirst"
        "abcdefghi" -> "ghidefabc"

    Args:
        s (str): The input string of odd length.

    Returns:
        str: The modified string with the parts swapped.
    '''

    # middle substring calc
    mid = len(s)//2 

    # get start and end index of the middle part of the string
    mid_start , mid_end = mid - 1 , mid+2

    # get new string
    new_string = s[mid_end:] + s[mid_start:mid_end] + s[: mid_start]

    # return
    return new_string


def interleave_lists(list1, list2, list3):
    '''
    Given three lists of same length, 
    interleave them together and return the interleaved list.

    Example:
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [(1,1),(2,2),(3,3)]
        output = [1, 'a', (1,1), 2, 'b', (2,2), 3, 'c', (3,3)]

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        list3 (list): The third list.

    Returns:
        list: A list containing interleaved elements from all three lists.
    '''
    
    # empty list
    interleaved_list = []

    # itreate over each of the list
    for i in range(len(list1)):
        # add one element form each list at the current index to interleaved list
        interleaved_list.extend([list1[i], list2[i], list3[i]])

    # return
    return interleaved_list


def has_more_than_5_unique_digits(num: int) -> bool:
    '''
    Determine if a given integer has more than 5 unique digits.

    Args:
        num (int): The input integer.

    Returns:
        bool: True if the integer has more than 5 unique digits, otherwise False.
    '''
    
    # convert num to string
    num_to_str = str(abs(num))

    # set co0onversion
    unique_val = set(num_to_str) 

    # check for 5 or more uniques values / boolean check
    ans = len(unique_val)>5

    # return ans
    return ans


def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
    '''
    Given an initial position of a point moving in a cartesian plane with a constant velocity, 
    find the the final position of the point after a given time. 

    Hint: final position = intial position + velocity * time

    Args:
        pos - tuple[int]: A tuple representing the position vector (x1, y1).
        vel - tuple[int]: A tuple representing the velocity vector (vx, vy).
        time - int: time of movement.

    Returns:
        tuple[int]: A tuple representing the displacement (dx, dy).
    '''
    
    # get final x position
    final_x = pos[0] + vel[0] * time

    # get final_y
    final_y = pos[1] + vel[1] * time

    # return tuple
    return (final_x, final_y)

def remove_keys_not_in_list(d: dict, l: list) -> None:
    '''
    Remove keys from a dictionary that are not present in a given list.
    The function modifies the dictionary in place and does not return anything.

    Note: 
        Modifying a dict while iterating over it will give an error in python. 
        So, make a copy of the dict keys and then iterate over it.

    Args:
        d (dict): The dictionary to modify.
        l (list): The list of keys to keep in the dictionary.

    Returns:
        None
    '''
    key_list = list(d.keys())

    for k in key_list:
        if k not in l:
            del d[k]



