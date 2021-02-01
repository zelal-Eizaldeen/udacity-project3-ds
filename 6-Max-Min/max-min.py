def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    sorted_ints = set(ints)
    final_ints = list(sorted_ints)
    if len(final_ints) == 0:
        return
        
    if len(final_ints) == 1:
        return sorted_ints[0]
    min = final_ints[0]
    max = final_ints[0]
      
    for el in final_ints:
        if el < min:
            min = el
        if el > max:
            max = el
    return (min, max)


  

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l2 = []
print ("Pass" if ((None) == get_min_max(l2)) else "Fail")

l3 = [7, 1, 9, -2, 9, 1]
print ("Pass" if ((-2, 9) == get_min_max(l3)) else "Fail")