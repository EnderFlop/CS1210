def hawkID():
    return("agbarloon")

def createMarkerString(currentTweetIndex, tweetLatLonList, mapCenterLatLon):
  red_coords = "&markers=color:red|"
  yellow_coords = "&markers=color:yellow|size:small|"
  for index, tweet in enumerate(tweetLatLonList):

    #if the tweet has geo coords, use them
    if tweet is not None:
      if index == currentTweetIndex:
        red_coords += f"{tweet[0]},{tweet[1]}|"
      else:
        yellow_coords += f"{tweet[0]},{tweet[1]}|"

    #if not, use the defaults
    if tweet is None:
      if index == currentTweetIndex:
        red_coords += f"{mapCenterLatLon[0]},{mapCenterLatLon[1]}|"
      else:
        yellow_coords += f"{mapCenterLatLon[0]},{mapCenterLatLon[1]}|"
    
  #remove the last character (always a pipe)
  red_coords = red_coords[:-1]
  yellow_coords = yellow_coords[:-1]

  return red_coords + yellow_coords

#print(createMarkerString(1, [[40.7452888, -73.9864273], None, [40.76056, -73.9659]], [40.758895, -73.985131]))
#print("&markers=color:red|40.758895,-73.985131&markers=color:yellow|size:small|40.7452888,-73.9864273|40.76056,-73.9659")