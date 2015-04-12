#!/usr/bin/python2

def main():
    import Config
    import os, os.path

    files = Config.filesInFolder(Config.pathImages, True)

    for f in files:
        date = f[:10]
        filePath = os.path.join(Config.pathImages, f)
        if os.path.isfile(filePath):
            folder = os.path.join(Config.pathImages, date)
            if not os.path.exists(folder):
                os.mkdir(folder)
            os.rename(filePath, os.path.join(folder, f))

if __name__ == "__main__":
    main()
