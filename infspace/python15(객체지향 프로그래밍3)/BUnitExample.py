# Unit, Tank, DropShip, Marine 클래스의 실행파일

from BTank import *
from BDropship import *
from BMarine import *

if __name__ == "__main__":
    print("-" * 50)
    tank = Tank()
    tank.move(100, 300)
    tank.siegeMode()
    tank.stop("탱크", 300, 400)
    print("-" * 50)
    marine = Marine()
    marine.move(200, 550)
    marine.stimPack()
    marine.stop("마린", 300, 400)
    print("-" * 50)
    dropship = DropShip()
    dropship.move(1000, 2000)
    dropship.load()
    dropship.unload()
    dropship.stop("드랍쉽", 0, 0)
    print("-" * 50)