def equilateral(sides):
    if side(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
    return False
  
def isosceles(sides):
    if side(sides):
        for el in sides:
            if sides.count(el) >= 2:
                return True
    return False
  
def scalene(sides):
    if side(sides):
        if sides.count(sides[0]) == 1 and sides.count(sides[1]) == 1 and sides.count(sides[2]) == 1:
            return True
    return False
  
def side(self):
    if self[0] != 0 and self[1] !=0 and self[2] != 0:
        return self[0] + self[1] >= self[2] and self[1] + self[2] >= self[0] and self[0] + self[2] >= self[1]
    return False
