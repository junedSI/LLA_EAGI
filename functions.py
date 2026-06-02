# functions in python 
# problem statement: write a function that takes in a list of numbers and returns the sum of those numbers
# syntax: 

# def function_name(parameters):
#     # function body
#    return result

# function call
# function_name(arguments)

# def function_name(parameter1: int|float = default_value, parameter2: int|str = default_value) -> type:

# recursion is a programming technique in which a function calls itself in order to solve a problem.
# syntax: 

# def recursive_function(parameters):
#     if base_case_condition:
#         return base_case_value
#     else:
#         return recursive_function(modified_parameters)

# base case is the condition under which the recursion will stop. 
# It is important to have a base case in a recursive function to prevent infinite recursion.

# recursive call is the call to the same function within the function body.
# def factorial(n: int) -> int:
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))  # Output: 120