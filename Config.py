dateFormat = "%Y-%m-%d_%H%M"
#default path
pathImages = r"Stamples\part_1"
# path for hostname
pathsImage = {
    "think-jules": r"Stamples\part_1",
    #"think-jules": r"E:\WebcamsImages\2015-03-10",
    "banana-black": r"/home/jules/Webcams/Images",
    "kamhy-alien": r"E:\GoogleDrive\HE-ARC\3eme\3252_Imagerie_Numerique\3252.2_TraitementDimage\WemcamsAnalyser\Stamples\part_2",
}
import platform
if platform.node() in pathsImage:
    pathImages = pathsImage[platform.node()]

from os import listdir
from os.path import isfile, join, isdir

#[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{4}_[A-Za-z_]{4,}.jpg

def filesInFolder(path, sort=False):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if sort:
        files.sort()
    return files

def folderInFolder(path, sort=False):
    files = [f for f in listdir(path) if isdir(join(path, f))]
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
    Webcam("LSGC_east" , "http://www.leseplaturesairport.ch/site/images/stories/webcam/LSGC1.jpg"    , 381, 366,  8),
    Webcam("LSGC_west" , "http://www.leseplaturesairport.ch/site/images/stories/webcam/LSGC3.jpg"    , 276, 287,  8),
    Webcam("LSGN_east" , "http://www.neuchatel-airport.ch/webcams/lsgn_east.jpg"                     , 146, 117,  0, 423), #modif
    Webcam("LSGN_west" , "http://www.neuchatel-airport.ch/webcams/lsgn_west.jpg"                     , 297, 265,  0, 421), #modif
    Webcam("LSGL_north", "http://www.lausanne-airport.ch/webcam0/last/webcam002.jpg"                 , 133, 125, 24), #modif
    Webcam("LSGL_south", "http://www.lausanne-airport.ch/webcam2/last/webcam000M.jpg"                ,  93,  93, 18), #modif
    Webcam("LSZQ_west" , "http://www.aerojura.ch/ressourcesannexes/aerojura/photos/capture/ouest.jpg", 407, 513, 27), #modif
    Webcam("LSZQ_east" , "http://www.aerojura.ch/ressourcesannexes/aerojura/photos/capture/est.jpg"  , 323, 296, 27), #modif
    Webcam("LSPL_east" , "http://aecs.lspl.ch/fileadmin/webcams/cam05_large.jpg"                     , 130, 215, 20),
    Webcam("LSPL_west" , "http://aecs.lspl.ch/fileadmin/webcams/cam23_large.jpg"                     , 217, 153, 20),
    Webcam("LSZB"      , "http://www.flughafenbern.ch/images/webcam/current.jpg"                     ,  58,  90,  8, 448),
    Webcam("LSZJ"      , "http://www.gamcy.ch/MOBOTIX/Courtelary-cam1.jpg"                           , 102,  80,  7), #modif
    Webcam("StImier"   , "http://www.chasseral-snow.ch/photo/camerapts0800-5.jpg"                    , 129, 115, 14), #modif
]