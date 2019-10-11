import os
import re

from glob import glob


def clean_directory_name(directory):
  regex = re.compile('[^a-zA-Z_]')
  directory = regex.sub('', directory)
  return directory

base_dir = "/home/jupyter/projects/planet_classifier/data/train"
directories = glob(base_dir + "/*/")
for directory in directories:
    i = 0
    for filename in os.listdir(directory):
        destination_name = "_" + str(i) + ".jpg"
        source_name = directory + filename
        renamed_directory = directory.rsplit('/', 2)[-2]
        destination = base_dir + "/" + renamed_directory + "_new/" + f"{renamed_directory}" + destination_name
        try:        
          os.rename(source_name, destination)
          print(destination)
          i += 1
        except Exception as e:
          print(e)
          pass
      

