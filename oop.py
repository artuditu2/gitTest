#!//usr/bin/env python3

class Point:
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        # protected property
        self.__color = "Red"
    def MovePoint(self, newX, newY):
        self.x = newX
        self.y = newY
    def PrintPoint(self):
        print("x = ", str(self.x))
        print("y = ", str(self.y))
    def GetColor(self):
        return self.__color
    def SetColor(self, __color):
        self.__color = __color

class Samochod:
    def __init__(self, myPredkosc = 0, myX = 0, myY = 0):
        self.x = myX
        self.y = myY
        self.predkosc = myPredkosc
    def wolniej(self, oIle):
        print("Zwalniam o ", oIle)
        self.predkosc = self.predkosc - oIle
    def szybciej(self, oIle):
        print("Przyspieszam o ", oIle)
        self.predkosc = self.predkosc + oIle

# mojeAuto = Samochod(0,0,0)
# mojeAuto.szybciej(12)
# mojeAuto.wolniej(4)
# print(mojeAuto.predkosc)

origin = Point(1,1)
myPoint = Point(5,8)

myPoint.MovePoint(10, 6)
myPoint.PrintPoint()
origin.PrintPoint()
print(type(origin))
print(myPoint.GetColor())
print("zmieniam kolor")
myPoint.SetColor("Green")
print(myPoint.GetColor())
