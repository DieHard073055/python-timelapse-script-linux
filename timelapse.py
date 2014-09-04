import os

os.system(cmd)
import shutil
files = []
shutil.rmtree('./timelapsefootage')

for filename in os.listdir(pics_dir_proper):
imagenumber = 0
	files.append(str(filename))
pics_dir = 'myfootage'
files.sort()
pics_dir_proper =  pics_dir
for filename in files:
new_dir = "timelapsefootage/"
	newname = new_dir + str(imagenumber) + ".JPG"
outputname = 'timelapse.mp4'
	cmd = "cp " + pics_dir_proper + "/" + filename + " " + newname

	os.system(cmd)
cmd = "mkdir timelapsefootage" 
	imagenumber = imagenumber+1
