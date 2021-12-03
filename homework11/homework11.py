import tkinter
import math
import ssl
import json
import webbrowser
import os
from dotenv import load_dotenv
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
from twitteraccess import authTwitter, searchTwitter, printable, whoIsFollowedBy, getMyRecentTweets, get_url

def hawkID():
    return("agbarloon")

#
# In HW10 and 11, you will use two Google services, Google Static Maps API
# and Google Geocoding API.  Both require use of an API key.
# 
# When you have the API key, put it between the quotes in the string below
load_dotenv()
GOOGLEAPIKEY = os.getenv("HW10_API_KEY")


# To run the HW10 program, call the last function in this file: HW10().

# The Globals class demonstrates a better style of managing "global variables"
# than simply scattering the globals around the code and using "global x" within
# functions to identify a variable as global.
#
# We make all of the variables that we wish to access from various places in the
# program properties of this Globals class.  They get initial values here
# and then can be referenced and set anywhere in the program via code like
# e.g. Globals.zoomLevel = Globals.zoomLevel + 1
#
class Globals:
   
   rootWindow = None
   mapLabel = None

   defaultLocation = "Mt. Fuji, Japan"
   mapLocation = defaultLocation
   mapFileName = 'googlemap.gif'
   mapSize = 400
   zoomLevel = 9
   tweets = []
   currentTweetURL = None
   currentTweetEmbeddedURL = None
   
# Given a string representing a location, return 2-element tuple
# (latitude, longitude) for that location 
#
# See https://developers.google.com/maps/documentation/geocoding/
# for details about Google's geocoding API.
#
#
def geocodeAddress(addressString):
   urlbase = "https://maps.googleapis.com/maps/api/geocode/json?address="
   geoURL = urlbase + quote_plus(addressString)
   geoURL = geoURL + "&key=" + GOOGLEAPIKEY

   # required (non-secure) security stuff for use of urlopen
   ctx = ssl.create_default_context()
   ctx.check_hostname = False
   ctx.verify_mode = ssl.CERT_NONE
   
   stringResultFromGoogle = urlopen(geoURL, context=ctx).read().decode('utf8')
   jsonResult = json.loads(stringResultFromGoogle)
   if (jsonResult['status'] != "OK"):
      print("Status returned from Google geocoder *not* OK: {}".format(jsonResult['status']))
      result = (0.0, 0.0) # this prevents crash in retrieveMapFromGoogle - yields maps with lat/lon center at 0.0, 0.0
   else:
      loc = jsonResult['results'][0]['geometry']['location']
      result = (float(loc['lat']),float(loc['lng']))
   return result

# Contruct a Google Static Maps API URL that specifies a map that is:
# - is centered at provided latitude lat and longitude long
# - is "zoomed" to the Google Maps zoom level in Globals.zoomLevel
# - Globals.mapSize-by-Globals.mapsize in size (in pixels), 
# - will be provided as a gif image
#
# See https://developers.google.com/maps/documentation/static-maps/
#
# YOU WILL NEED TO MODIFY THIS TO BE ABLE TO
# 1) DISPLAY A PIN ON THE MAP
# 2) SPECIFY MAP TYPE - terrain vs road vs ...
#
def getMapUrl():
   lat, lng = geocodeAddress(Globals.mapLocation)
   urlbase = "http://maps.google.com/maps/api/staticmap?"
   args = f"center={lat},{lng}&zoom={Globals.zoomLevel}&size={Globals.mapSize}x{Globals.mapSize}&maptype={Globals.mapType.get()}&format=gif"
   for tweet in Globals.tweets:
      try:
         lat, lng = tweet["geo"]["coordinates"]
         if tweet["hw_11_selected"]:
            args += f"&markers=size:mid|color:green|{lat},{lng}"
         else:
            args += f"&markers=size:small|{lat},{lng}"
      except TypeError:
         continue
   #print(args)
   args = args + "&key=" + GOOGLEAPIKEY
   mapURL = urlbase + args
   return mapURL

# Retrieve a map image via Google Static Maps API, storing the 
# returned image in file name specified by Globals' mapFileName
#
def retrieveMapFromGoogle():
   url = getMapUrl()
   urlretrieve(url, Globals.mapFileName)

########## 
#  basic GUI code

def displayMap():
   retrieveMapFromGoogle()    
   mapImage = tkinter.PhotoImage(file=Globals.mapFileName)
   Globals.mapLabel.configure(image=mapImage)
   # next line necessary to "prevent (image) from being garbage collected" - http://effbot.org/tkinterbook/label.htm
   Globals.mapLabel.mapImage = mapImage
   
def readEntryAndDisplayMap():
   #### you should change this function to read from the location from an Entry widget
   #### instead of using the default location
   Globals.mapLocation = Globals.entryField.get()
   tweetSearchTerm = Globals.twitterField.get()
   if tweetSearchTerm:
      lat, lng = geocodeAddress(Globals.mapLocation)
      Globals.tweets = searchTwitter(tweetSearchTerm, latlngcenter=(lat,lng))
      for tweet_index in range(len(Globals.tweets)):
         Globals.tweets[tweet_index]["hw_11_selected"] = False
      Globals.currentTweetIndex = 0
      if Globals.tweets:
         updateTweet(Globals.currentTweetIndex)
   displayMap()

def updateTweet(index):
   for tweet_index in range(len(Globals.tweets)):
      Globals.tweets[tweet_index]["hw_11_selected"] = False
   Globals.openURLButton.configure(state=tkinter.NORMAL)
   Globals.tweetCountLabel.configure(text=f"Tweet {index+1} of {len(Globals.tweets)}. Posted by {Globals.tweets[index]['user']['name']} (@{Globals.tweets[index]['user']['screen_name']})")
   Globals.tweetDisplayText.configure(state=tkinter.NORMAL)
   Globals.tweetDisplayText.delete("1.0", "end")
   Globals.tweets[index]["hw_11_selected"] = True
   Globals.tweetDisplayText.insert(tkinter.INSERT, Globals.tweets[index]["full_text"])
   Globals.tweetDisplayText.configure(state=tkinter.DISABLED)
   Globals.currentTweetURL = get_url(Globals.tweets[index]["user"]["screen_name"], Globals.tweets[index]["id_str"])
   try:
      Globals.currentTweetEmbeddedURL = Globals.tweets[index]["entities"]["urls"][0]["url"]
   except (KeyError, IndexError) as e:
      try:
         Globals.currentTweetEmbeddedURL = Globals.tweets[index]["user"]["entities"]["url"]["urls"][0]["url"]
      except (KeyError, IndexError) as e:
         Globals.openURLButton.configure(state=tkinter.DISABLED)
   displayMap()


def increaseZoom():
  Globals.zoomLevel += 1
  Globals.zoomLabel.configure(text=f"Zoom: {Globals.zoomLevel}")
  displayMap()

def decreaseZoom():
  if Globals.zoomLevel != 0:
    Globals.zoomLevel -= 1
    Globals.zoomLabel.configure(text=f"Zoom: {Globals.zoomLevel}")
    displayMap()

def nextTweet():
   if Globals.currentTweetIndex != len(Globals.tweets) - 1:
      Globals.currentTweetIndex += 1
      updateTweet(Globals.currentTweetIndex)

def lastTweet():
   if Globals.currentTweetIndex != 0:
      Globals.currentTweetIndex -= 1
      updateTweet(Globals.currentTweetIndex)

def openInBrowser():
   if Globals.currentTweetURL == None:
      return
   webbrowser.open(Globals.currentTweetURL)

def openURLInBrowser():
   if Globals.currentTweetEmbeddedURL == None:
      return
   webbrowser.open(Globals.currentTweetEmbeddedURL)
   

def initializeGUIetc():

   Globals.rootWindow = tkinter.Tk()
   Globals.rootWindow.title("HW11")

   mainFrame = tkinter.Frame(Globals.rootWindow) 
   mainFrame.pack()

   # until you add code, pressing this button won't change the map (except
   # once, to the Beijing location "hardcoded" into readEntryAndDisplayMap)
   # you need to add an Entry widget that allows you to type in an address
   # The click function should extract the location string from the Entry widget
   # and create the appropriate map.
   helpLabel = tkinter.Label(mainFrame, text="Map Location:")
   helpLabel.pack(side=tkinter.LEFT)
   Globals.entryField = tkinter.Entry(mainFrame)
   Globals.entryField.pack(side=tkinter.LEFT)
   searchtermLabel = tkinter.Label(mainFrame, text="Search Terms:")
   searchtermLabel.pack(side=tkinter.LEFT)
   Globals.twitterField = tkinter.Entry(mainFrame)
   Globals.twitterField.pack(side=tkinter.LEFT)
   readEntryAndDisplayMapButton = tkinter.Button(mainFrame, text="Show me the map!", command=readEntryAndDisplayMap)
   readEntryAndDisplayMapButton.pack(side=tkinter.LEFT)

   imageFrame = tkinter.Frame(Globals.rootWindow)
   imageFrame.pack()
   # we use a tkinter Label to display the map image
   Globals.mapLabel = tkinter.Label(imageFrame, width=Globals.mapSize, bd=2, relief=tkinter.FLAT)
   Globals.mapLabel.pack()

   Globals.mapType = tkinter.StringVar(value="roadmap")

   masterFrame = tkinter.Frame(Globals.rootWindow)
   masterFrame.pack()
   zoomFrame = tkinter.Frame(masterFrame)
   zoomFrame.pack(side=tkinter.LEFT)
   Globals.zoomLabel = tkinter.Label(zoomFrame, text=f"Zoom: {Globals.zoomLevel}")
   Globals.zoomLabel.pack(side=tkinter.LEFT)
   zoomInButton = tkinter.Button(zoomFrame, text="+", command=increaseZoom)
   zoomInButton.pack(side=tkinter.LEFT)
   zoomOutButton = tkinter.Button(zoomFrame, text="-", command=decreaseZoom)
   zoomOutButton.pack(side=tkinter.LEFT)

   maptypeFrame = tkinter.Frame(masterFrame)
   maptypeFrame.pack(side=tkinter.LEFT)
   maptypeLabel = tkinter.Label(maptypeFrame, text="Choose Map Type:")
   maptypeLabel.pack(side=tkinter.TOP)
   roadmapButton = tkinter.Radiobutton(maptypeFrame, text = "roadmap", variable = Globals.mapType, value = "roadmap", command=displayMap)
   roadmapButton.pack(side=tkinter.LEFT)
   satelliteButton = tkinter.Radiobutton(maptypeFrame, text = "satellite", variable = Globals.mapType, value = "satellite", command=displayMap)
   satelliteButton.pack(side=tkinter.LEFT)
   terrainButton = tkinter.Radiobutton(maptypeFrame, text = "terrain", variable = Globals.mapType, value = "terrain", command=displayMap)
   terrainButton.pack(side=tkinter.RIGHT)
   hybridButton = tkinter.Radiobutton(maptypeFrame, text = "hybrid", variable = Globals.mapType, value = "hybrid", command=displayMap)
   hybridButton.pack(side=tkinter.RIGHT)

   tweetDataFrame = tkinter.Frame(Globals.rootWindow)
   tweetDataFrame.pack(side=tkinter.BOTTOM)
   Globals.tweetCountLabel = tkinter.Label(tweetDataFrame, text="Look Something Up!")
   Globals.tweetCountLabel.pack(side=tkinter.TOP)
   Globals.tweetDisplayText = tkinter.Text(tweetDataFrame, state=tkinter.DISABLED, height=5, width=60)
   Globals.tweetDisplayText.pack(side=tkinter.TOP, padx=10, pady=10)
   backTweetButton = tkinter.Button(tweetDataFrame, text="Last Tweet", command=lastTweet)
   backTweetButton.pack(side=tkinter.LEFT, fill=tkinter.X, padx=10, pady=10, expand=True)
   nextTweetButton = tkinter.Button(tweetDataFrame, text="Next Tweet", command=nextTweet)
   nextTweetButton.pack(side=tkinter.LEFT, fill=tkinter.X, padx=10, pady=10, expand=True)
   openTweetButton = tkinter.Button(tweetDataFrame, text="Open Tweet In Browser", command=openInBrowser)
   openTweetButton.pack(side=tkinter.LEFT, fill=tkinter.X, padx=10, pady=10, expand=True)
   Globals.openURLButton = tkinter.Button(tweetDataFrame, text="Open URL In Browser", command=openURLInBrowser)
   Globals.openURLButton.pack(side=tkinter.LEFT, fill=tkinter.X, padx=10, pady=10, expand=True)


def HW11():
    initializeGUIetc()
    displayMap()
    Globals.rootWindow.mainloop()

#HW11()