import math

def wrap_around_numbers(idx,rotation_factor):
    return ((idx + rotation_factor) % 10)

def wrap_around_chars(idx,rotation_factor):
  if idx + rotation_factor >= 25:
    return ((idx + rotation_factor) % 25)-1
  else:
    return ((idx + rotation_factor) % 25)

def rotationalCipher(input, rotation_factor):
  # Write your code here
  string_anchors_lc ="abcdefghijklmnopqrstuvwxyz"
  string_anchors_uc ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  number_anchors ="0123456789"
      
  cipher_str = []
      
  for i in input: # O(n)
    if i.isalpha():
      asc_val = ord(i)
      cipher_index = 0
      if asc_val >= 65 and asc_val <=91:
          idx = asc_val-65
          cipher_index = wrap_around_chars(idx,rotation_factor)
          cipher_str.append(string_anchors_uc[cipher_index])
      else:
          idx = asc_val-97
          cipher_index = wrap_around_chars(idx,rotation_factor)
          cipher_str.append(string_anchors_lc[cipher_index])
    elif i.isnumeric():
         idx = int(i)
         cipher_index = wrap_around_numbers(idx,rotation_factor)
         cipher_str.append(number_anchors[cipher_index])
    else:
      cipher_str.append(i)
    
  return "".join(cipher_str)



print(rotationalCipher("All-convoYs-9-be:Alert1.",4))
print(rotationalCipher("abcdZXYzxy-999.@",200))
print(rotationalCipher("v",4))