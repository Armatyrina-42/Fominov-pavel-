def find_second_largest():
 """
 Returns:
   int: Второй по величине элемент в последовательности.
 """
 max_value = 0 
 second_max_value = 0 
 number = int(input()) 
 while number != 0: 
  if number > max_value: 
   second_max_value = max_value 
   max_value = number 
  elif number > second_max_value and number != max_value: 
   second_max_value = number 
  number = int(input()) 
 return second_max_value
result = find_second_largest()
print(f"Второй по величине элемент в последовательности: {result}")