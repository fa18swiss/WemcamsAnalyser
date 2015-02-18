__author__ = 'Jules'

import Config


files = Config.filesInFolder(Config.pathImages, True)
dates = {}
count = 0
for f in files:
    date = f[:15]
    count+= 1
    if date in dates:
        dates[date] += 1
    else:
        dates[date] = 1
errors = [(f, dates[f]) for f in dates if dates[f] != 12]
errors.sort()
print("errors :")
print(errors)

