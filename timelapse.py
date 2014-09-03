import os

os.system(cmd)
import shutil
files = []
shutil.rmtree('./timelapsefootage')

for filename in os.listdir(pics_dir_proper):
