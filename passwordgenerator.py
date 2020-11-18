#Verifing the Buzz Fizz Gaming program
for total in range(1, 101):
  if total%3==0 and total%5==0:
    print("Buzz Fizz")
  elif total%3==0:
    print("Fizz")    
  elif total%5==0:
    print("Buzz")
  else:
    print(total)
