"""
NAME:           Evan Whitmer
DATE:           10/9/2023
DESCRIPTION:    Write a function called keep which takes a list, and a Boolean-valued function 
                and returns the list consisting of all elements for which that function is true. 
"""

#defining odd and even functions
def is_even(n) : return n%2 == 0
def is_odd(m) : return m%2 != 0
    
#defining lists of different sizes for testing
test  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#defining keep in a way that it can fit in a single line to show better comprehension
def keep(my_list, fun): return[my_list[i] for i in range(len(my_list)) if fun(my_list[i])]

#print the results
print(keep(test, is_even))      #test for even
print(keep(test2, is_odd))      #test for odd