import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def wrap_around(idx,rotation_factor):
    if idx >= 25:
        cipher_index = 0
        cipher_index = cipher_index + rotation_factor - (idx-25)
    else:
        cipher_index = idx + rotation_factor
    return cipher_index

def rotationalCipher(input, rotation_factor):
  # Write your code here
  string_anchors_lc ="abcdefghijklmnopqrstuvwxyz"
  string_anchors_uc ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  number_anchors ="0123456789"
      
  cipher_str = []
      
  for i in input:
    if i.isalpha():
      asc_val = ord(i)
      if asc_val >= 65 and asc_val <=91:
          idx = asc_val-65
          cipher_index = 0
          if idx >= 25:
             cipher_index = 0
             cipher_index = cipher_index + rotation_factor - (idx-25)
          else:
             cipher_index = idx + rotation_factor
          cipher_str.append(string_anchors_uc[cipher_index])
      else:
          idx = asc_val-97
          cipher_index = 0
          if idx >= 25:
             cipher_index = 0
             cipher_index = cipher_index + rotation_factor -1-(idx-25)
          else:
             cipher_index = idx + rotation_factor
          cipher_str.append(string_anchors_lc[cipher_index])
    elif i.isnumeric():
      if i == 9:
        cipher_index = rotation_factor-1
      else:
        cipher_index = rotation_factor+1
      cipher_str.append(number_anchors[cipher_index])
    else:
      cipher_str.append(i)
    
  return cipher_str


print(rotationalCipher("Zebra",3))