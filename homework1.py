import math
def hawkID():
    return("agbarloon")

def computeTripData(distanceK, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
  print("\n\n")
  #The length of the trip in hours
  vehicle_KPS = vehSpeedMPS / 1000 #meters per second to kilometers per second.
  total_hours = distanceK / vehicle_KPS
  print(f"total_hours = {total_hours}")

  driving_days = math.ceil(total_hours / 8) #can only drive 8 hours a day
  print(f"driving_days = {driving_days}")

  driving_end_perfectly = total_hours % 8 == 0 #If the trip end exactly on a day. True/False
  print(f"driving_end_perfectly = {driving_end_perfectly}")

  rest_days = math.floor(total_hours / 40) #every 40 hours needs an additional rest day
  print(f"rest_days = {rest_days}")

  rest_days_end_perfectly = total_hours % 40 == 0 #If the trip ends exactly on a rest day. True/False
  if rest_days_end_perfectly: #If it does, remove 1 rest day. Didn't actually take it
    rest_days -= 1
  print(f"rest_end_perfectly = {rest_days_end_perfectly}")

  total_driving_days = driving_days + rest_days
  print(f"total_driving_days = {total_driving_days}")

  #The gas cost of the trip in dollars
  total_gas_cost = (distanceK / vehKPL) * gasCostPerLiter #total liters needed multiplied by cost per liter
  print(f"total_gas_cost = {total_gas_cost}")

  #The number of breakfasts required
  num_breakfasts = total_driving_days - 1 #no brekkie on first day
  print(f"num_breakfasts = {num_breakfasts}")
  brekkie_cost = num_breakfasts * breakfastCostPerDay

  #The number of lunches required
  num_lunches = math.floor(total_hours/8) + rest_days
  final_day_length = total_hours % 8
  if final_day_length > 4.0:
    num_lunches += 1
  print(f"num_lunches = {num_lunches}")
  lunch_cost = num_lunches * lunchCostPerDay

  #The number of dinners required
  num_dinners = math.floor(total_hours/8) + rest_days #One a day if it gets that late
  if rest_days_end_perfectly: #If it ends on a rest night, dont do eat that night.
    num_dinners -= 1
  elif driving_end_perfectly: #If it ends at the very end of the day, don't eat that night either.
    num_dinners -= 1
  print(f"num_dinners = {num_dinners}")
  dinner_cost = num_dinners * dinnerCostPerDay

  #The number of hotel nights required
  num_hotel_nights = math.floor(total_hours/8) + rest_days #One hotel day a night
  if rest_days_end_perfectly: #If it ends on a rest night, dont do those night.
    num_hotel_nights -= 1
  elif driving_end_perfectly: #If it ends at the very end of the day, don't take a hotel that night either.
    num_hotel_nights -= 1
  print(f"num_hotel_nights = {num_hotel_nights}")
  hotel_cost = num_hotel_nights * hotelCostPerNight

  #The total cost of the trip in dollars
  total_cost = brekkie_cost + lunch_cost + dinner_cost + total_gas_cost + hotel_cost
  print(f"total_cost = {total_cost}")

  return total_hours, total_gas_cost, total_cost, num_breakfasts, num_lunches, num_dinners, num_hotel_nights

#computeTripData(, 1000, 10, 4, 5, 6, 7, 80)