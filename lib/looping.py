#!/usr/bin/env python3

def happy_new_year():
   i = 10
   while i > 0:
     print(i)
     i -= 1
   if (i == 0):
    print("Happy New Year!")



def square_integers(int_list):
    squared_list = [num ** 2 for num in int_list]
    return squared_list

result = square_integers([1, 2, 3, 4, 5])
print(result) 
    


def fizzbuzz():
    
    count = 1
    while count <= 100:
        if (count % 3 == 0 and count % 5 == 0):
            print("FizzBuzz")
            count += 1
        elif (count % 3 == 0):
            print("Fizz")
            count += 1
        elif (count % 5 == 0):
            print("Buzz")
            count += 1
        else:
            print(count)
            count += 1

