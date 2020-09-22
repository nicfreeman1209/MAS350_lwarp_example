# CC-BY-SA

# runs lwarpmk, moves some files and copies others
# end result: 
#   the complete html version ends up in ./out_html/, whilst keeping original tex working dir moderately clean

from glob import glob
import os
import shutil

out_path = "out_html"
if os.path.exists("./"+out_path+"/"):
	shutil.rmtree("./"+out_path)
os.makedirs(out_path)
	
os.system("lwarpmk html1")
#os.system("lwarpmk html1 -p notes_1")
#os.system("lwarpmk html1 -p notes_2")

move_extensions = ["html"]
copy_extensions = ["png", "jpg", "txt", "css"]

for ext in move_extensions:
	files = glob("./*." + ext)
	for file in files:
		shutil.move(file, os.path.join("./"+out_path, file))
		
for ext in copy_extensions:
	files = glob("./*." + ext)
	for file in files:
		shutil.copy(file, os.path.join("./"+out_path, file))
		
