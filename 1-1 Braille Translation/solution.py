#!/usr/bin/python

"""
Provides solution() function that takes a string parameter and returns a string of 1's and 0's
representing the bumps and absence of bumps in the input string.
Encodes the 26 lowercase letters, handle capital letters by adding a Braille modifier before that character,
and use a blank character (000000) for spaces
"""

"""
Declaration of required variables, reference lists and definition of required functions

character_store
  saves computation time when same characters are repeated in input
  contains pre-filled data for corner cases such as braille w,x,y,z and space

reference_list
  braille codes for characters in first decade (a-j)

decade_offset
  offset value to be set for characters belonging to a specific decade

capitalization_mark
  braille modifier for captial letters (000001)

error_code
  decimal equivalent for braille ! character to replace any unidentified characters
"""

character_store = {
    ' ': 0,   #000000
    'w': 23,  #010111
    'x': 45,  #101101
    'y': 47,  #101111
    'z': 43   #101011
}

reference_list = [32, 48, 36, 38, 34, 52, 54, 50, 20, 22]
decade_offset = [0, 8, 9]

capitalization_mark = 1   #000001
error_code = 26           #011010

def _to_binary(decimal_value):
  """private helper function to convert decimal value to 6-digit binary"""

  return format(decimal_value, '06b')

def solution(input_text):
  """Returns the braille code of the input string as a sequence of 0s and 1s

  input_text:  the sequence of alphabets/space characters as a string

  Note: if any character is out of range, the braille character for exclamation is added instead
  """

  braille_output = ''
  for character in input_text:
    braille_code = error_code
    if character.isupper():
      key = character.lower()
      braille_output = braille_output + _to_binary(capitalization_mark)
    else:
      key = character

    cache_data = character_store.get(key)
    if cache_data is not None:
      braille_code = cache_data
    else:
      key_int = ord(key)
      if key_int >= 97 and key_int <= 118:
        idx = key_int - 97
        decade = idx / 10
        idx = idx - decade *10
        braille_code = reference_list[idx] + decade_offset[decade]
        character_store[key] = braille_code

    braille_output = braille_output +  _to_binary(braille_code)

  return braille_output
