def hawkID():
    return("agbarloon")

# CS 1210, Falls 2021
# Discussion section 7, Oct. 18-20.  Due 8pm, Oct. 20

# DISCUSSION SECTION WORK:
#

# Download this file, ds7.py and also stack.py and circle.py
#
# 1. After studying the Stack class and testStack function in stack.py
#    complete the Queue class (and test it with the included testQueue function)
#
# 2. Afer studying and testing the Circle class in circle.py,
#    complete the Rectangle class below (and test it with the included
#    testRectangle function)
#
# 3. SUBMIT THIS ONE FILE, with your updates, TO ICON.
#
#
# NOTE: you may certainly add more tests to the test functions if you want.
#       BUT DO NOT add any top level code that automatically calls your
#       functions or creates class instances
#
#####

# 1. Complete the Queue class (following the style of the Stack class)
#
# A queue is similar to a stack but a bit different.
#
# A queue is a collection of items supporting three operations:
#   - enqueue (item): add item to the â€œfrontâ€ of the queue
#   - dequeue(): removes the â€œlastâ€ item from the queue
#                 (the one thatâ€™s been in the queue the longest) and returns it
#   - size(): returns the number of items currently in the queue
#
# Note: stacks are â€œLIFOâ€ (last-in-first-out)
#       while queues are â€œFIFOâ€ (first-in-first-out)

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if len(self.items) > 0:
            first = self.items[0]
            self.items = self.items[1:]
            return first
        else:
            print("Can't dequeue when there's nothing in the list!")
    
    def size(self):
        return len(self.items)

# 2. Complete the Rectangle class (following the style of the Circle class) 

import math

class Rectangle:
    def __init__(self, centerX = 0.0, centerY = 0.0, width = 0.0, height = 0.0):
        self.centerX = centerX
        self.centerY = centerY
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f"< rectangle of width {self.width} and height {self.height} ({self.width*self.height} units) centered at ({self.centerX},{self.centerY}) >"
       
    def setCenter(self, x, y):
        self.centerX = x
        self.centerY = y
    
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return (2*self.width) + (2*self.height)

    #
    # return True if the area of self is less than the area of otherRectangle
    # Otherwise return False
    def isSmallerThan(self, otherRectangle):
        other_area = otherRectangle.area()
        if self.area() < other_area:
            return True
        return False
   
    #
    # the intersects method should return True if the two rectangles
    # touch/intersect at all (even they just touch exactly at their edges or
    # corners). Note: think carefully about how to do this test. Sketching
    # some pictures can help you analyze the possibilities.
    #
    def intersects(self, otherRectangle):
        A_half_w = self.width / 2
        A_half_h = self.height / 2
        A_top_left_x = self.centerX - A_half_w
        A_top_left_y = self.centerY + A_half_h
        A_bottom_right_x = self.centerX + A_half_w
        A_bottom_right_y = self.centerY - A_half_h

        B_half_w = otherRectangle.width / 2
        B_half_h = otherRectangle.height / 2
        B_top_left_x = otherRectangle.centerX - B_half_w
        B_top_left_y = otherRectangle.centerY + B_half_h
        B_bottom_right_x = otherRectangle.centerX + B_half_w
        B_bottom_right_y = otherRectangle.centerY - B_half_h

        if A_top_left_x <= B_bottom_right_x and A_bottom_right_x >= B_top_left_x and A_top_left_y >= B_bottom_right_y and A_bottom_right_y <= B_top_left_y:
            return True
        return False


##### Test functions
    
def testQueue():
    try: 
        print("*** Start of Queue tests ***")
        q = Queue()
        if q.size() != 0:
            print("Error: queue size not correct right after creation")
        else:
            print("First test okay")
        q.enqueue(3)
        q.enqueue("hi")
        q.enqueue(99)
        q.enqueue(True)
        if q.size() != 4:
            print("Error: queue size not correct after 4 enqueues")
        else:
            print("Second test okay")
        v = q.dequeue()
        if v != 3:
            print("Error: dequeued item value check incorrect")
        else:
            print("Third test okay")
        if q.size() != 3:
            print("Error: queue size not correct after 1 dequeue")
        else:
            print("Fourth test okay")
        q.dequeue()
        q.dequeue()
        q.enqueue([1,2])
        if q.size() != 2:
            print("Error: queue size not correct after 2 more dequeues and an enqueue")   
        else:
            print("Fifth test okay")
        v = q.dequeue()
        if v != True:
            print("Error: second dequeued item value check incorrect")
        else:
            print("Sixth test okay") 
        q.dequeue()
        if q.size() != 0:
            print("Error: queue size not 0 after final 2 dequeues")
        else:
            print("Seventh test okay")
        print("*** Now will test dequeue of empty queue. It is okay if it crashes with")
        print("    an appropriate error.  Also okay if it just prints something appropriate.")
        q.dequeue()
        print("*** End of Queue tests ***")
    except Exception as err:
        print("An error occurred: ", err)
    return
        
    
def testRectangle():
    try:
        print("*** Start of Rectangle tests ***")
        rect1 = Rectangle(10.0, 5.0, 2.0, 1.0)
        area1 = rect1.area()
        perimeter1 = rect1.perimeter()
        if area1 != 2.0:
            print("Area test failed.")
        else:
            print("Area test passed.")
        if perimeter1 != 6.0:
            print("Perimeter test failed.")
        else:
            print("Perimeter test passed.")
        rect2 = Rectangle(0, 0, 3.5, 2.5)
        if rect1.isSmallerThan(rect2):
            print("isSmallerThan test1 passed")
        else:
            print("isSmallerThan test1 failed")
        if rect1.isSmallerThan(rect1):
            print("isSmallerThan test2 failed")
        else:
            print("isSmallerThan test2 passed")
        i12 = rect1.intersects(rect2)
        i21 = rect2.intersects(rect1)
        if (i12 or i21):
            print("First intersection tests failed.")
        else:
            print("First intersection tests passed.")
        rect1.setCenter(-2.75, 0.0)
        i12 = rect1.intersects(rect2)
        i21 = rect2.intersects(rect1)
        if (i12 and i21):
            print("Second intersection tests passed.")
        else:
            print("Second intersection tests failed.")
        rect1.setCenter(-2.76, 0.0)
        i12 = rect1.intersects(rect2)
        i21 = rect2.intersects(rect1)
        if (i12 or i21):
            print("Third intersection tests failed.")
        else:
            print("Third intersection tests passed.")
        rect1.setCenter(-2.75, 1.75)
        i12 = rect1.intersects(rect2)
        i21 = rect2.intersects(rect1)
        if (i12 and i21):
            print("Fourth intersection tests passed.")
        else:
            print("Fourth intersection tests failed.")      
        rect1.setWidth(1.0)  
        rect1.setHeight(1.0)
        i12 = rect1.intersects(rect2)
        i21 = rect2.intersects(rect1)
        if (i12 or i21):
            print("Fifth intersection tests failed.")
        else:
            print("Fifth intersection tests passed.")
        rect1.setCenter(0.5, 0.5)
        i12 = rect1.intersects(rect2)
        i21 = rect2.intersects(rect1)
        if (i12 and i21):
            print("Sixth intersection tests passed.")
        else:
            print("Sixth intersection tests failed.")
        print("*** End of Rectangle tests ***")
    except Exception as err:
          print("An error occurred: ", err)
    return      
    
#testQueue()
#testRectangle()
  
   
