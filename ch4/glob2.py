import glob
files = glob.glob("glob2.py") + glob.glob("os*.py") + glob.glob("*.txt")
for file in files: 
    print(file)
