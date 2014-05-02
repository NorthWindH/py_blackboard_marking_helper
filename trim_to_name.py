import os
import shutil

if __name__ == "__main__":
    for f in os.listdir('.'):
        if "2014" in f:
            new_name = f[f.find("2014") + 20:]
            shutil.move(f, new_name)
