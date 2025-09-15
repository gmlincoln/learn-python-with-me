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


print("=== Calculator ===")
print("1. For input two numbers")
print("Enter")
value = int(input(''))


if value == 1:
    num1, num2 = map(int, input("Enter two number:").split())

    print('Select Operation (eg. +, -, *, /)')
    operator = input("Enter operator: ")
    
    if operator == '+':
        print(num1 + num2); 
    
    elif operator == '-':
        print(num1 - num2); 
    
    elif operator == '*':
        print(num1 * num2); 
    
    elif operator == '/':
        print(num1 / num2); 

    else:
        print('Invalid Operator'); 

else:
    print('Invalid')

