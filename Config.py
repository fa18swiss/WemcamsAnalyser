dateFormat = "%Y-%m-%d_%H%M"
pathImages = r"E:\\WebcamsImages\\"

from os import listdir
from os.path import isfile, join



def filesInFolder(path, sort=False):

    files = [f for f in listdir(path) if isfile(join(path, f))]
    if sort:
        files.sort()
    return files

class Webcam:
    def __init__(self, name, url, skyLeft, skyRight, ignoreTop = 0, ignoreBottom = 0):
        self.__name = name
        self.__url = url
        self.__skyLeft = skyLeft
        self.__skyRight = skyRight
        self.__ignoreTop = ignoreTop
        self.__ignoreBottom = ignoreBottom
    def name(self):
        return self.__name
    def url(self):
        return self.__url
    def ignoreTop(self):
        return self.__ignoreTop
    def ignoreBottom(self):
        return self.__ignoreBottom
    def skyLeft(self):
        return self.__skyLeft
    def skyRight(self):
        return self.__skyRight
    def __repr__(self):
        return "Webcam '%s'" % self.__name

webcams = [
    Webcam("LSGC_east" , "http://www.leseplaturesairport.ch/site/images/stories/webcam/LSGC1.jpg"    , 381, 366, 8),
    Webcam("LSGC_west" , "http://www.leseplaturesairport.ch/site/images/stories/webcam/LSGC3.jpg"    , 30, 30),
    Webcam("LSGN_east" , "http://www.neuchatel-airport.ch/webcams/lsgn_east.jpg"                     , 30, 30),
    Webcam("LSGN_west" , "http://www.neuchatel-airport.ch/webcams/lsgn_west.jpg"                     , 30, 30),
    Webcam("LSGL_north", "http://www.lausanne-airport.ch/webcam0/last/webcam002.jpg"                 , 30, 30),
    Webcam("LSGL_south", "http://www.lausanne-airport.ch/webcam2/last/webcam000M.jpg"                , 30, 30),
    Webcam("LSZQ_west" , "http://www.aerojura.ch/ressourcesannexes/aerojura/photos/capture/ouest.jpg", 30, 30),
    Webcam("LSZQ_east" , "http://www.aerojura.ch/ressourcesannexes/aerojura/photos/capture/est.jpg"  , 30, 30),
    Webcam("LSPL_east" , "http://aecs.lspl.ch/fileadmin/webcams/cam05_large.jpg"                     , 130, 215, 20),
    Webcam("LSPL_west" , "http://aecs.lspl.ch/fileadmin/webcams/cam23_large.jpg"                     , 30, 30),
    Webcam("LSZB"      , "http://www.flughafenbern.ch/images/webcam/current.jpg"                     , 30, 30, 8, 448),
    Webcam("LSZJ"      , "http://www.gamcy.ch/MOBOTIX/Courtelary-cam1.jpg"                           , 30, 30),
]