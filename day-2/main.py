# while
# i = 1; 
# while i < 5:
#     print(i); # 1 2 3 4
#     i +=1; # 2 3 4 5
    

# print(f'Outside loop: {i}');

# for 

# name = "Rubel Islam"

# for letter in name:
#     print(letter)


# for x in range( 1 , 11, 1):
#     print(x); 


# print("=== Calculator ===")
# print("1. For input two numbers")
# print("Enter")
# value = int(input(''))


# if value == 1:
#     num1, num2 = map(int, input("Enter two number:").split())

#     print('Select Operation (eg. +, -, *, /)')
#     operator = input("Enter operator: ")
    
#     if operator == '+':
#         print(num1 + num2); 
    
#     elif operator == '-':
#         print(num1 - num2); 
    
#     elif operator == '*':
#         print(num1 * num2); 
    
#     elif operator == '/':
#         print(num1 / num2); 

#     else:
#         print('Invalid Operator'); 

# else:
#     print('Invalid')

# print("=== Calculator ===")
# print("1. For input two numbers")
# print("Enter")
# value = 0


# while value  !=  1:
#     value = int(input('Enter valid vlaue: '))


# if value == 1:
#     num1, num2 = map(int, input("Enter two number:").split())

#     print('Select Operation (eg. +, -, *, /)')
#     operator = input("Enter operator: ")
    
#     if operator == '+':
#         print(num1 + num2); 
    
#     elif operator == '-':
#         print(num1 - num2); 
    
#     elif operator == '*':
#         print(num1 * num2); 
    
#     elif operator == '/':
#         print(num1 / num2); 

#     else:
#         print('Invalid Operator'); 

# else:
#     print('Invalid')





# The FizzBuzz problem is a common introductory coding challenge where you
# write a program to print numbers from 1 to a given integer n. For multiples of 3, you print "Fizz"; 
# for multiples of 5, you print "Buzz";and for numbers divisible by both 3 and 5, you print "FizzBuzz". 
# Otherwise, you print the number itself. 

# 3 -> Fizz
# 5 -> Buzz
# 3 and 5 -> FizzBuzz

# Expected: 

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

n = int(input("Enter value"));

for x in range(1, n+1, 1):
    if x % 3 == 0 and x % 5 == 0: # x % 15 == 0
        print("FizzBuzz")
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x); 