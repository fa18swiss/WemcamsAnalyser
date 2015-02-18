import urllib
from datetime import datetime
import Config


todayStr = ("{:" + Config.dateFormat + "}").format(datetime.today())
for webcam in Config.webcams:
    urllib.urlretrieve(webcam.url(), "Webcam/Images/%s_%s.jpg" % (todayStr, webcam.name()))