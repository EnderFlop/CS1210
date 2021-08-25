import math
def hawkID():
    return("agbarloon")

def computeTripData(distanceK, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
  #The length of the trip in hours
  vehicle_KPS = vehSpeedMPS / 1000 #meters per second to kilometers per second.
  total_hours = distanceK / vehicle_KPS
  print(f"total_hours = {total_hours}")
  driving_days = math.ceil(total_hours / 8) #can only drive 8 hours a day
  print(f"driving_days = {driving_days}")
  driving_end_perfectly = total_hours % 8 == 0 #If the trip end exactly on a day. True/False
  print(f"driving_end_perfectly = {driving_end_perfectly}")
  rest_days = math.floor(total_hours / 40 #every 40 hours needs an additional rest day
  print(f"rest_days = {rest_days}")
  rest_days_end_perfectly = total_hours % 40 == 0 #If the trip ends exactly on a rest day. True/False
  total_driving_days = driving_days + rest_days

  #The gas cost of the trip in dollars
  total_gas_cost = (distanceK / vehKPL) * gasCostPerLiter #total liters needed multiplied by cost per liter

  #The number of breakfasts required
  num_breakfasts = total_driving_days - 1 #no brekkie on first day
  

  #The number of lunches required
  num_lunches = total_driving_days

  #The number of dinners required

  #The number of hotel nights required
  num_hotel_nights = total_driving_days #One hotel day a night
  if rest_days_end_perfectly: #If the trip ends when a rest day would start
    num_hotel_nights -= 1 #subtract that rest day
  elif driving_end_perfectly:
    num_hotel_nights -= 1

  #The total cost of the trip in dollars

