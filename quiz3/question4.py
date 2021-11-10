class Box:                                                                                                            
    def __init__(self, width, height, depth, maxWeight):                                                              
        self.width = width                                                                                            
        self.height = height                                                                                          
        self.depth = depth                                                                                            
        self.maxWeight = maxWeight
        # objectsInside should contain a list of (name, weight) tuples
        self.objectsInside = []                                                                               
        self.currentWeightInside = 0                                                                                     
        self.currentNumberOfObjectsInside = 0                                                                                                                                                                                              
                                                                                                                      
    def volume(self):                                                                                                 
        return self.width * self.height * self.depth                                                                  
                                                                                                                      
    def numberOfObjectsInside(self):                                                                                  
        return self.currentNumberOfObjectsInside                                                                      
                                                                                                                      
    def remainingWeightCapacity(self):                                                                                
        return self.maxWeight - self.currentWeightInside                                                              
                                                                                                                      
    # If the box's weight capacity will not be exceeded, add given object to the box,                                                          
    #    updating self. objectsInside, self.currentWeightInside and 
    #    and self.currentNumberOfObjectsInside      
    # Otherwise, print an appropriate message.                                                                        
    #                                                                                                                 
    def addObject(self, objectName, objectWeight):
        if self.remainingWeightCapacity() < objectWeight:
            print("Can't fit that inside the box, it's too heavy!")
        else:
            self.objectsInside.append((objectName, objectWeight))
            self.currentNumberOfObjectsInside += 1
            self.currentWeightInside += objectWeight
        return
                                                                                                                      
    # Return True if the size (by volume) of self is larger than that of the other box, 
    # Otherwise return False             
    #                                                                                                                 
    def isLargerThan(self, otherBox):                                                                                 
        if self.volume() > otherBox.volume():
            return True
        return False

    # Return True if self contains a larger number of objects than otherBox 
    # Otherwise return False             
    #                                                                                                                 
    def containsMoreObjectsThan(self, otherBox):    
        if self.currentNumberOfObjectsInside > otherBox.currentNumberOfObjectsInside:
           return True
        return False                                                                           

    # empty the given box so that there are no objects afterwards.
    #    Make sure you update all relevant properties.
    def makeEmpty(self):
        self.currentNumberOfObjectsInside = 0
        self.currentWeightInside = 0
        self.objectsInside = []


def testBox():
    box1 = Box(3, 2, 4, 100)
    box2 = Box(2, 3, 5, 20)
    print(box1.isLargerThan(box2))
    box1.addObject("o1", 90)
    box1.addObject("o2", 9)
    print(box1.remainingWeightCapacity(), box1.numberOfObjectsInside())
    box1.addObject("o3", 5)
    box2.addObject("o4", 10)
    print(box1.containsMoreObjectsThan(box2))
    print(box2.containsMoreObjectsThan(box1))
    box1.makeEmpty()
    print(box1.containsMoreObjectsThan(box2))
    print(box2.containsMoreObjectsThan(box1))
    return (box1, box2)

#print(testBox())