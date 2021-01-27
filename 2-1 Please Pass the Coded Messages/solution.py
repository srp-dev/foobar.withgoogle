#!/usr/bin/python
from collections import Counter

"""
Provides solution() function that takes a list parameter and finds the largest number
that can be made from some or all of the digits in input list and is divisible by 3.
If it is not possible to make such a number, returns 0 as the solution. 
Each element in the input list is used only once if selected to be part of the solution.
"""

"""
Declaration of required variables

reminder_combo_map
  maps the reminder (sum % 3) with a list of all possible digit combinations that need to be removed (for reminders 1 and 2)
  each combination itself is a list containing all possible combinations of digits to remove in the order of priority
"""


reminder_combo_map = {
  1: [ [1], [4], [7], [2,2], [2,5], [2,8], [5,2], [5,5], [5,8], [8,2], [8,5], [8,8] ],
  2: [ [2], [5], [8], [1,1], [1,4], [1,7], [4,1], [4,4], [4,7], [7,1], [7,4], [7,7] ]
}


def solution(list_of_digits):
  """Returns the largest number that can be made from some or all of the digits in input list and is divisible by 3
     Returns 0 if it is not possible to make such a number

  list_of_digits:  the list of numbers between 0-9
  """

  try:
    ## Input validation
    if not isinstance(list_of_digits, list):
      raise TypeError("input must be a list")

    for digit in list_of_digits:
      if not isinstance(digit, int):
        raise TypeError( ' "{}" is not a recognized input value'.format(digit))
      if digit > 10 or digit < 0:
        raise ValueError(' "{}" is not a number between 0-9'.format(digit))

    # Sort in descending order, calculate reminder when divided by 3
    sorted_list = sorted(list_of_digits, reverse=True)
    modulo3 = sum(sorted_list) % 3
    
    if modulo3 != 0:
      # Find and remove digits that can reduce the reminder to 0 when divided by 3
      combination = _find_items_to_remove(Counter(sorted_list), modulo3)
      _remove_digits_from_list(sorted_list, combination)

    return _list_as_number(sorted_list)

  except:
    raise

def _find_items_to_remove(digits_counter, reminder):
  """Returns an item in the reminder_combo_map based on the reminder value and matching available digits in the input list
     Returns None if no match is found
     
  digits_counter: Counter object representing the occurence of each digit in the input list

  reminder: the reminder value obtained by adding all digits in the list and dividing it by 3 
  """

  try:
    all_combinations = reminder_combo_map.get(reminder)

    for combination in all_combinations:
      match_found = False
      digits_counter_c = digits_counter.copy()

      for item in combination:
        
        occurence = digits_counter_c.get(item, 0)

        if occurence < 1:
          match_found = False
          break

        digits_counter_c[item] = occurence - 1
        match_found = True


      if match_found:
        return combination
  except:
    raise

def _remove_digits_from_list(list_of_digits, combination):
  """Modifies the input list by removing items from the list based on the combination provided
     
  list_of_digits: Counter object representing the occurence of each digit in the input list

  combination:  an entry from reminder_combo_map[1] or reminder_combo_map[2] used as a reference to remove the digits
  """

  try:
    if combination is not None and len(combination) > 0:
      for digit in combination:
        list_of_digits.remove(digit)
  except:
    raise

def _list_as_number(list_of_digits):
  """private helper function to convert list of digits to a single number"""

  return long(''.join(map(str, list_of_digits))) if len(list_of_digits) != 0 else 0
