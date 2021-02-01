def sqrt(number):
  if number is None:
    return None
  if number < 0:
    return -1
  if number == 0 or number == 1:
    return number
  start = 1
  end = number
  square_root = 1
  while(start <= end):
    mid = (start + end) // 2
    if ((mid ** 2) == number):
      return mid
    elif((mid ** 2) < number):
      start = mid + 1
      square_root = mid
    else:
      end = mid - 1
  return square_root


# TESTING
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("None Value, Please enter an integer value" if  (None == sqrt(None)) else "Fail")
print ("NO NEGATIVE VALUES, Please enter a positive integer value" if  (-1 == sqrt(-1)) else "Fail")




