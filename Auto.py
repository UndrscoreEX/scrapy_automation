import os
from posixpath import dirname
import shutil
import subprocess



# How to begin:
# Run this in the directory after the 'scrapy startproject ___ ' and the "genspider _____" command. 
# So run it in the directory containing the "startproject" directory 

# -- Or change the file name here manually:
# e.g 
# spider = "AWSspider"

# -- choose output directory or it will just output to the current directory:
# output = "/mnt/c/Users/ethan/Desktop/Scraping Excel sheets/test/"

result = subprocess.run(["echo", "this is working "], stdout=subprocess.PIPE)
subprocess.run(["echo", "-----"+result.stdout.decode('utf-8')+"------"])


# for dirpath, dirnames, files in os.walk(os.path.abspath(os.curdir+"/UdemyTest/spiders")):

# -- Checks the spiders files and looks for the spider file: 


try:
    print( "using the manually selected: ", spider )
except: 
    print("No spider selected. Searching for spider...")
    dir = os.path.basename(os.path.abspath(os.curdir))
    spideroptions = []
    for dirpath, dirnames,files in os.walk(os.path.abspath(os.curdir+"/"+dir+"/spiders")):
        for x in files:
            if x != "__init__.py":
                if ".pyc" not in x :
                    spideropt = x.replace(".py","")
                    print(spideropt)
                    spideroptions.append(spideropt)
    if len(spideroptions) == 1:
        spider = spideroptions[0]
    else:
        for ind,x in enumerate(spideroptions):
            print(f"Press: {ind} To run: {x}")
        result = input("Which spider do you want to run?")
        spider = spideroptions[int(result)]

# -- the name of the file to be output.
filename = dir+".csv"




# -- running scrapy
subprocess.call(["scrapy", "crawl", spider, "-o", filename])

# -- Move the scraped file:
try:
    print( output )
    shutil.copy(filename, output +filename)
    subprocess.call(["echo", "----------------------------------done---------------------------"])
except:
    print('No output directory selected. Check startproject folder for the csv file. ')
