#!/usr/bin/python2

def main():
    import Config
    import os, os.path
    import subprocess
    import datetime

    folders = Config.folderInFolder(Config.pathImages, True)

    workDir = os.path.join(os.path.join(Config.pathImages, ".."), "compress")
    if not os.path.exists(workDir):
        os.makedirs(workDir)

    todayStr = ("{:" + Config.dateOnlyFormat + "}").format(datetime.today())
    print("todayStr")
    for f in folders:
        path = os.path.join(Config.pathImages, f)
        tar = "%s.tar" % f
        print(path)
        print(f)
        subprocess.call(["tar", "-cvf", tar, path], cwd=workDir)
        subprocess.call(["xz", "-e", tar], cwd=workDir)

if __name__ == "__main__":
    main()
