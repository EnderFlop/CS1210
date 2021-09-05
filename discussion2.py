def hawkID():
    return("agbarloon")

# CS1210 Fall 2021, Discussion section assignment 2
#
# Complete each of the four functions and submit this file to the
# DS2 assignment item in the lecture ICON.

# Q1. Given non-negative integer num, q1(num) should return:
# 0 if num is not a multiple of 2, 7, or 14,
# 2 if num is a multiple of 2 but not 14,
# 7 if num is a multiple of 7 but not 14,
# 14 if num is a multiple of 14
# E.g. q1(3) should return 0 while q1(21) should return 7
#
def q1 (num):
    if num == 0:
      return 0
    if num % 2 != 0 and num % 7 != 0 and num % 14 != 0:
      return 0
    elif num % 2 == 0 and num % 14 != 0:
      return 2
    elif num % 7 == 0 and num % 14 != 0:
      return 7
    elif num % 14 == 0:
      return 14
    return

# Q2. Given non-negative integer n, q2(n) should call q1 for each integer from 1 up
# to and including n, adding up the results and returning the final sum.
# If n is 0, it should not call q1 at all and should simply return 0.
# q2 MUST use a WHILE loop to do the counting.
# Example output:
# >>> q2(7)
# 13
# >>> q2(21)
# 46
#
def q2(n):
    i = 0
    final_sum = 0
    while i <= n:
      #print(f"running q1 on {i}. result = {q1(i)}")
      final_sum += q1(i)
      i += 1
    return final_sum

# Q3.Complete function sumDigitsOf(n) that returns the sums the digits of a
#    the given positive number n
#
# For example, sumDigitsOf(5137) should return 16
#
# SOLUTION METHOD:
#
# How can we extract and sum the digits of a non-negative integer
# ONLY using math? 
#
# Some people might know that in Python we first convert the number to a
# string of digits and then look at each character in the string. BUT, the goal
# here is to do it with just math - NO STRING OPERATIONS ARE ALLOWED!
#
# Use this approach:
#
#    1. get the last digit of an integer by using % 10 
#       digit = number % 10 (E.g. if number was 432, digit will be 2)
#       Add this value to a variable you use for the ultimate sum.
#
#    2. get a new number with all but the last digit via
#       newNumber = number // 10  (E.g. if number was 432, newNumber will be 43)
#    
#    3. repeat those steps until nothing's left (i.e. when newNumber becomes 0)
#
#    USE A WHILE LOOP TO ACCOMPLISH THE ABOVE STEPS
#
#  HINT: First, you should try examples of steps 1 and 2 at a Python prompt to
#  make sure you understand. E.g. enter 432 % 10 and 432 // 10
#
def sumDigitsOf(number):
    final_sum = 0
    while number:
      digit = number % 10
      final_sum += digit
      number = number // 10
    return final_sum
