import shutil
import os

if __name__ == "__main__":
    for f in os.listdir('.'):
        if f.count("2014"):
            newName = f[f.find("2014"):]
            shutil.move(f, newName)
