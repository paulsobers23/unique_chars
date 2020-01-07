def unique_chars(string):
  if len(string) == 0:
    return None
  
  if string == " ":
    return None
    
  charaDic = {}
  for char in string:
    if char in charaDic: