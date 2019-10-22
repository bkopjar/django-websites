def find(ordered_list, element_to_find):
  for element in ordered_list:
    if element == element_to_find:
      return True
  return False
  
if __name__=="__main__":
  a= [2, 4, 5, 6, 8, 10]
  print(find(a, 5)) 
  print(find(a, 9)) 
  print(find(a, -1)) 
  print(find(a, 2)) 