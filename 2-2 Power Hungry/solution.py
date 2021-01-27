#!/usr/bin/python

"""
Provides solution() function that takes a list of integers and returns the string representation of maximum product of
some non-empty subset of those numbers. The input list shall contain at least 1 and no more than 50 integers 
whose absolute value is no greater than 1000. Any two negative values shall be multiplied to produce a positive value.
"""

def solution(list_of_digits):
  """Returns the string representation of maximum product of some/all non-empty numbers in the input list

  list_of_digits:  the list of numbers from -1000 to 1000 with list length from 1 to 50
  """

  try:
    # maximum output value
    product = None

    # largest negative number in the list
    max_negative = None

    # whether or not all input elements are zeroes
    has_zero = False
  
    # Input validation
    if not isinstance(list_of_digits, list):
      raise TypeError("input is not a list")

    list_length = 0
    for digit in list_of_digits:
      if not isinstance(digit, int):
        raise TypeError( ' "{}" is not a recognized input value'.format(digit))

      if digit > 1000 or digit < -1000:
        raise ValueError(' "{}" is not a number between -1000 and 1000'.format(digit))

      list_length = list_length + 1

    if list_length < 1 or list_length > 50:
      raise ValueError(' input list length is not between 1-50')

    # Calculate product
    for digit in list_of_digits:
      if digit == 0:
        has_zero = True
        continue

      if digit < 0:
        # find max_negative, do not multiply it with product yet
        if max_negative is None:
          max_negative = digit
          continue

        if digit > max_negative:
          product = (product or 1) * max_negative
          max_negative = digit
          continue

      product = (product or 1) * digit
    
    if product is None:
      # input has no positive numbers
      product = 0 if has_zero else max_negative
    elif product < 0:
      # multiply by max_negative to make it positive
      product = product * max_negative

    return str(product)

  except:
    raise
