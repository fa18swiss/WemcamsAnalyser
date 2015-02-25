import urllib
from datetime import datetime
import Config

todayStr = ("{:" + Config.dateFormat + "}").format(datetime.today())
for webcam in Config.webcams:
    try:
        urllib.urlretrieve(webcam.url(), "%s/%s_%s.jpg" % (Config.pathImages, todayStr, webcam.name()))
    except:
        pass
import Move
