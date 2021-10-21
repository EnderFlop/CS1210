import random

def hawkID():
    return("agbarloon")

class Box:
  def __init__(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width = 1.0, height = 1.0, depth = 1.0):
    self.centerX = centerX
    self.centerY = centerY
    self.centerZ = centerZ
    self.width = width
    self.height = height
    self.depth = depth
  
  def __repr__(self):
    return f"< {self.width}-by-{self.height}-by-{self.depth} 3D box with center at ({self.centerX}, {self.centerY}, {self.centerZ}) >"
  
  def setCenter(self, x, y, z):
    self.centerX = x
    self.centerY = y
    self.centerZ = z
  
  def setWidth(self, w):
    self.width = w
  
  def setHeight(self, h):
    self.height = h
  
  def setDepth(self, d):
    self.depth = d
  
  def volume(self):
    return self.width * self.height * self.depth
  
  def surfaceArea(self):
    return 2*(self.width*self.height + self.height*self.depth + self.depth*self.width)
  
  def touches(self, otherBox):
    # box1.touches(box2) should return True if the two 3D boxes touch/intersect at all, even they just touch exactly at their edges or corners. 
    # (Think of boxes as filled/solid objects so that if a box fully contains another, they are also considered to be touching.)
    # SOLUTION: If a's leftmost point is to the right of b's rightmost point, a is totally to the right of b. Expand this.
    A_right_x = self.centerX + self.width / 2
    A_left_x = self.centerX - self.width / 2
    A_top_y = self.centerY + self.height / 2
    A_bottom_y = self.centerY - self.height / 2
    A_front_z = self.centerZ + self.depth / 2
    A_back_z = self.centerZ - self.depth / 2

    B_right_x = otherBox.centerX + otherBox.width / 2
    B_left_x = otherBox.centerX - otherBox.width / 2
    B_top_y = otherBox.centerY + otherBox.height / 2
    B_bottom_y = otherBox.centerY - otherBox.height / 2
    B_front_z = otherBox.centerZ + otherBox.depth / 2
    B_back_z = otherBox.centerZ - otherBox.depth / 2

    #If any of these checks succeed, there can be no overlap.
    x_check_1 = A_right_x < B_left_x
    x_check_2 = B_right_x < A_left_x
    y_check_1 = A_top_y < B_bottom_y
    y_check_2 = B_top_y < A_bottom_y
    z_check_1 = A_front_z < B_back_z
    z_check_2 = B_front_z < A_back_z
    if x_check_1 or x_check_2 or y_check_1 or y_check_2 or z_check_1 or z_check_2:
      return False
    return True
  
  def contains(self, otherBox):
    # box1.contains(box2) should return True if no point of box 2 is outside or even on the boundary of box2
    # very similar to previous problem, just change checks to ensure:
    # a's right face is less than the b's right face AND the a's left face is greater than b's left face.
    A_right_x = self.centerX + self.width / 2
    A_left_x = self.centerX - self.width / 2
    A_top_y = self.centerY + self.height / 2
    A_bottom_y = self.centerY - self.height / 2
    A_front_z = self.centerZ + self.depth / 2
    A_back_z = self.centerZ - self.depth / 2

    B_right_x = otherBox.centerX + otherBox.width / 2
    B_left_x = otherBox.centerX - otherBox.width / 2
    B_top_y = otherBox.centerY + otherBox.height / 2
    B_bottom_y = otherBox.centerY - otherBox.height / 2
    B_front_z = otherBox.centerZ + otherBox.depth / 2
    B_back_z = otherBox.centerZ - otherBox.depth / 2

    #If all these checks succeed, the box is inside the other box.
    x_check_1 = B_right_x < A_right_x
    x_check_2 = B_left_x > A_left_x
    y_check_1 = B_top_y < A_top_y
    y_check_2 = B_bottom_y > A_bottom_y
    z_check_1 = B_front_z < A_front_z
    z_check_2 = B_back_z > A_back_z

    if x_check_1 and x_check_2 and y_check_1 and y_check_2 and z_check_1 and z_check_2:
      return True
    return False

def testBox():
  box1 = Box(10.0, 5.0, 0.0, 2.0, 1.0, 1.0)
  #print(box1)
  print(box1.volume() == 2.0)
  box2 = Box(0, 0, 0, 3.5, 2.5, 1.0)
  print(box2.surfaceArea() == 29.5)
  print(box1.touches(box2) == False)
  box1.setCenter(2.75, 0.0, 0.0)
  print(box1.touches(box2) == True)
  box1.setCenter(2.76, 0.0, 0.0)
  print(box1.touches(box2) == False)
  box1.setCenter(2.75, 1.75, 1.0)
  print(box1.touches(box2) == True)
  box1.setCenter(0.0, 0.0, 0.0)
  print(box1.touches(box2) == True)
  box1.setWidth(50.0)
  print(box1.touches(box2) == True)
  box1.setDepth(50.0)
  print(box1.touches(box2) == True)
  box3 = Box(0, 0, 0)
  print(box3.contains(box3) == False)
  box4 = Box(0.5, 0.0, 0.0, 2.0, 3.0, 4.0)
  print(box4.contains(box3) == False)
  box4.setWidth(2.1)
  print(box4.contains(box3) == True)

#testBox()

class NimGame:
  def __init__(self, heaps):
    self.heaps = heaps
    print(f"Nim game initialized with {len(heaps)} heaps.")
  
  def __repr__(self):
    string = f"< Nim game with {len(self.heaps)} heaps."
    for i in range(len(self.heaps)):
      string += f"\n\tHeap {i}: {self.heaps[i]} balls."
    string += "\n>"
    return string

  def remove(self, heap, balls):
    if self.heaps[heap] < balls:
      print(f"You can't take that many balls from heap {heap}, try again.")
      return
    else:
      print(f"You took {balls} balls from heap {heap}.")
      self.heaps[heap] -= balls
    
    print(self)

    if sum(self.heaps) == 0:
      print("Player Wins!")
    else:
      valid_heaps = [i for i in range(len(self.heaps)) if self.heaps[i] != 0]
      heap_choice = random.choice(valid_heaps)
      ball_count = random.randint(1, self.heaps[heap_choice])
      print(f"Computer took {ball_count} balls from heap {heap_choice}.")
      self.heaps[heap_choice] -= ball_count
      if sum(self.heaps) == 0:
        print("Computer Wins!")

#game = NimGame([2,3,4])
#print(game)

class Animal ():
    
    numAnimals = 0

    def __init__ (self, name = 'NoName', numLegs = 0):
        self.name = name
        self.numLegs = numLegs
        Animal.numAnimals = Animal.numAnimals + 1
        self.id = Animal.numAnimals

    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getNumLegs(self):
        return self.numLegs
   
    def speak(self):
        print("...")

    def __repr__(self):
        return ('<{} the animal. ID:{}>'.format(self.name, self.id))

class Cat(Animal):
    def __init__(self, name = 'noname', furColor = 'unknown'):
        Animal.__init__(self, name, 4)
        self.color = furColor
    
    def speak(self):
        print('meow')

    def getFurColor(self):
        return self.color

    def __repr__(self):
        return ('<{} the {} cat. ID: {}>'.format(self.name, self.color, self.id))

class Dog(Animal):
    
    def __init__(self, name = 'rover'):
        Animal.__init__(self, name, 4)
    
    def speak(self):
        print('woof')
        
    def fetch(self):
        print("I'm fetching ...")

    def __repr__(self):
        return '<{} the dog. ID:{}>'.format(self.name, self.id)

class Turtle(Animal):
  def __init__(self, name="Tungus"):
    Animal.__init__(self, name, 4)

  def speak(self):
    print("'Blub' (they say they love you <3)")
  
  def swim(self):
    print("Swimming!")
  
  def __repr__(self):
    return f"<{self.name} the turtle. ID:{self.id}>"
  
        
def testAnimal():
    c1 = Cat("Milo")
    c2 = Cat(furColor = "black")
    d1 = Dog()
    d2 = Dog()
    t1 = Turtle()
    t2 = Turtle("Roger")
    for animal in [c1, c2, d1, d2, t1, t2]:
        print(animal)
        animal.speak()
    d1.fetch()
    print(c2.getFurColor())
    t2.swim()