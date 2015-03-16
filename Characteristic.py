try:
    from enum import Enum
except:
    print("Module eunm not found, please download and install from https://pypi.python.org/pypi/enum34")
    import sys
    sys.exit(-1)


class ImagePart(Enum):
    ALL = 0
    SKY = 1
    GROUND = 2

class Channel(Enum):
    RGB_R = 1
    RGB_G = 2
    RGB_B = 3
    HSV_H = 4
    HSV_S = 5
    HSV_V = 6

#todo jules ajout equart type
class Characteristic:
    def __init__(self, name, channel, imagePart, proportion, leftX, leftY):
        self.__name = name
        self.__channel = channel
        self.__imagePart = imagePart
        self.__proportion = proportion
        self.__leftX = leftX
        self.__leftY = leftY
        if not isinstance(channel, Channel):
            raise TypeError("channel")
        if not isinstance(imagePart, ImagePart):
            raise TypeError("imagePart")
        if not isinstance(proportion, (float, int)):
            raise TypeError("proportion")
        if not isinstance(leftX, int):
            raise TypeError("leftX")
        if not isinstance(leftY, int):
            raise TypeError("leftY")
    def name(self):
        return self.__name
    def channel(self):
        return self.__channel
    def imagePart(self):
        return self.__imagePart
    def proportion(self):
        return self.__proportion
    def leftX(self):
        return self.__leftX
    def leftY(self):
        return self.__leftY

characteristics = (
    Characteristic("Blue", Channel.HSV_H, ImagePart.SKY, 90, 200, 210)
)
