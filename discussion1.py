# CS1210, Fall 2021, Discussion section 1.

# Three parts:
# Part 1: make sure to modify the hawkID() function to return your HawekID. This
# is required for EVERY discussion and homework assignment
# Part 2: read, execute, and review the functions.  No changes needed.
# Part 3: complete the three functions as specified.
#
# Submit the whole modified file to ICON.

#####
#
# Part 1. Replace 'yourhawkid' with your Hawk ID
#         E.g. Prof. Cremer would change "yourhawkid" to "cremer"
#
def hawkID():
    return("agbarloon")

#####
#
# PART 2. Just read, execute, and understand. No changes necessary.
#
# 2a and 2b. Understand that fuctions averageOf and avarageOfV2 are equivalent.
#    averageOfV2 simply uses some temporary local variables along the way
#    to producing the same result.  It's probably not necessary in these simple
#    functions BUT I STRONGLY ENCOURAGE you to write simple lines of code and
#    use temporary variables with MEANINGFUL names.  For complex functions, it
#    can be SUPER USEFUL for readability and debugging.
# 2c and 2d. Make sure you understand the difference between print and return

# First, a function that *returns* the average of three numbers. Two versions:
#
# 2a. without using additional variables
#
def averageOf(num1, num2, num3):
    return( (num1 + num2 + num3) / 3 )

# 2b. using additional variables for intermediate results - a good habit
#
def averageOfV2(num1, num2, num3):
    sumOfInputs = num1 + num2 + num3
    average = sumOfInputs / 3
    return average

# Next two functions that are similar except that one *prints* and one *returns* values.
#
# 2c. printMinAndMax *prints* values rather than *returning* results
#
def printMinAndMax(num1, num2, num3):
    minOfInputs = min(num1, num2, num3)
    maxOfInputs = max(num1, num2, num3)
    print((minOfInputs, maxOfInputs))

# 2d. *Similar* to 0C above but importantly different.  Does not print anything.
# Returns value for caller to use as desired.
#
def returnMinAndMax(num1, num2, num3):
    minOfInputs = min(num1, num2, num3)
    maxOfInputs = max(num1, num2, num3)
    return (minOfInputs, maxOfInputs)

# Try in Python shell:
# >>> printMinAndMax(2, 9, 3)
# >>> returnMinAndMax(2, 9, 3)
# Results in the Python shell might look the same but different things are happening.
# Continue with
# >>> minAndMax = printMinAndMax(2, 9, 3)
# (2, 9)
# >>> minAndMax
# >>>
# and compare with
# >>> minAndMax = returnMinAndMax(2, 9, 3)
# >>> minAndMax
# (2, 9)
# >>>
# Understand the difference!!

#####

# Part 3.

# 3a. Complete simple function kilometersFromMiles(miles)
# that takes a floating point value, miles, representing a distance in miles and returns
# a floating value equal to the same distance expressed in kilometers. Use a good conversion
# factor; try to use official "SI" factors!
#   
def kilometersFromMiles(miles):
    # complete this function!
    computed_kilometers = miles * 1.60934
    return computed_kilometers

# 3b. Complete simple function litersFromGallons(gallons)
# that takes a floating point value, gallons, representing a volume in gallons and returns
# a floating value equal to the same volume expressed in liters. Use a good conversion
# factor; try to use official "SI" factors!
#   
def litersFromGallons(gallons):
    computed_liters = gallons * 3.78541
    return computed_liters

# 3c. Complete function costOfTrip(distanceInKM, speedInKPH, kmPerLiter, gasCostPerLiter)
# that computes the time and cost of a trip based on speed and fuel
# efficiency of a vehicle, and RETURNS both the time and cost, in that order
#
# The inputs are all floats:
#  - distanceInKilometers: the trip distance in kilometers
#  - speedInKPH: the speed of the trip in kilometers per hour
#  - kmPerLiter: the number of kilometers traveled on one liter of gas
#  - gasCostPerLiter: the cost of one liter of gas in dollars
#
# The function must return two things:
#  - time required for trip (in hours, a floating point value)
#  - gas cost for trip (in dollars, a floating point value)
#
# Note: The calculations in this function are closely related to some
# of the calculations needed in HW1!
#
# Pseudocode/outline:
#
# costOfTrip(distanceInKilometers, speedInKPH, kmPerLiter, gasCostPerLiter):
#
#       # 1. calculate time required in hours (from distance and speed),
#                   associating result with a variable
#       # 2. calculate liters of gas needed (from distance and kpl),
#                   associating result with a different variable
#       # 3. calculate total cost of gas (from gas cost per liter and liters needed),
#                   again saving result in a variable.
#
#       # 4. return the two values, using values saved in the above calculations.
#
# Example usage:
#
# >>> costOfTrip(100.0, 20.0, 16.0, 2.25)
# (5.0, 14.0625)
#
def costOfTrip(distanceInKilometers, speedInKPH, kmPerLiter, gasCostPerLiter):
    hours_required = distanceInKilometers / speedInKPH
    liters_needed = distanceInKilometers / kmPerLiter
    total_gas_cost = liters_needed * gasCostPerLiter
    return hours_required, total_gas_cost



 