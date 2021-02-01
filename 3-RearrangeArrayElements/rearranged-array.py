def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    for num in input_list:
        if num is None:
            return "NO None value"
    if len(input_list) == 0:
        return "Empty List"
    
    sorted_array = mergesort(input_list)
    rearrange_digits_output(sorted_array)
    return sorted_array
def rearrange_digits_output(sorted_array):
    output = []

    mid = len(sorted_array) // 2
    left = sorted_array[:mid]
    right = sorted_array[mid:]
   
    left_strings = [str(integer) for integer in left]
    left_string = "".join(left_strings)
    left_integer = int(left_string)
    output.append(left_integer)

    right_strings = [str(integer) for integer in right]
    right_string = "".join(right_strings)
    right_integer = int(right_string)
    output.append(right_integer)
    print('Max Sum is: {}'.format(output))

   
def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

    # TESTING
test_list_0 = []
test_list_none = [None]
test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
test_list_4 = [4, 6, 2, 5, 9, 8]

print('{}'.format(rearrange_digits(test_list_0)))
print('{}'.format(rearrange_digits(test_list_none)))

print('{} Sorted to {}'.format(test_list_1, rearrange_digits(test_list_1)))
print('{} Sorted to {}'.format(test_list_2, rearrange_digits(test_list_2)))
print('{} Sorted to {}'.format(test_list_3, rearrange_digits(test_list_3)))
print('{} Sorted to {}'.format(test_list_3, rearrange_digits(test_list_4)))