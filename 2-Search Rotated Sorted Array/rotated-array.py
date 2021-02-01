def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
      return []
    end_index = len(input_list) - 1
    pivot = find_pivot(input_list, 0, end_index)
    # If we didn't find a pivot,  
    # then array is not rotated at all 
    if pivot == -1: 
        return binarySearch(input_list, 0, end_index, key); 
  
    # If we found a pivot, then first 
    # compare with pivot and then 
    # search in two subarrays around pivot 

    if input_list[pivot] == number:
      return pivot
    if input_list[0] <= number:
      return binarySearch(input_list, 0, pivot - 1, number)
    return binarySearch(input_list, pivot + 1, end_index, number)

# Function to get pivot
def find_pivot(input_list, low, high):
  # base cases
  if high < low:
    return -1
  if high == low:
    return low
  mid = (low + high) // 2
  if mid < high and input_list[mid] > input_list[mid + 1]:
    return mid
  if mid > low and input_list[mid] < input_list[mid - 1]:
    return (mid - 1)
  if input_list[low] >= input_list[mid]:
    return find_pivot(input_list, low, mid - 1)
  return find_pivot(input_list, mid + 1, high)

# Binary Search function
def binarySearch(input_list, low, high, number):
  if high < low:
    return -1
  mid = (low + high) // 2

  if number == input_list[mid]:
    return mid
  if number > input_list[mid]:
    return binarySearch(input_list, (mid + 1), high, number)
  return binarySearch(input_list, low, (mid - 1), number)


# TESTING
# Case 1: Empty Array
arr1 = []
number1 = 2
print ("Empty Array" if  ([] == rotated_array_search(arr1, number1)) else "Fail")


# Case 2:
arr2 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
number2 = 3
print("Index of the element is : ", rotated_array_search(arr2, number2))

# Case 3: NOT FOUND
arr3 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
number3 = 44
print ("NOT FOUND" if  (-1 == rotated_array_search(arr3, number3)) else "Fail")


# Case 4
arr4 = [6, 7, 8, 9, 10, 1, 2, 3, 4]
number4 = 6
print("Index of the element is : ", rotated_array_search(arr4, number4))
    
   