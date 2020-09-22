# runs lwarpmk, moves some files and copies others
# end result: 
#   complete website ends up in ./out_html/, whilst keeping original tex working dir moderately clean

from glob import glob
import os
import shutil

if os.path.exists("./out_html"):
	shutil.rmtree("./out_html/")
os.makedirs("out_html")
	
os.system("lwarpmk html1")

# for multiple linked files use e.g.
#os.system("lwarpmk html1 -p notes_1")
#os.system("lwarpmk html1 -p notes_2")

move_extensions = ["html"]
copy_extensions = ["png", "jpg", "svg", "txt", "css"]

for ext in move_extensions:
	files = glob("./*." + ext)
	for file in files:
		shutil.move(file, os.path.join("./out_html", file))
		
for ext in copy_extensions:
	files = glob("./*." + ext)
	for file in files:
		shutil.copy(file, os.path.join("./out_html", file))
		
