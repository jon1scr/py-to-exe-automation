import os
import shutil
from sys import argv

py_file = argv[1]
os.system(f'pyinstaller --onefile {py_file}')

distDir = os.getcwd() + '\dist\\'
exeFile = distDir + os.listdir(distDir)[0]

for f in os.listdir():
    if f.endswith('.spec'):
        os.remove(f)
    elif f == 'dist':
        shutil.move(exeFile, os.getcwd())
        shutil.rmtree(f)
    elif f == 'build' or f == '__pycache__':
        shutil.rmtree(f)