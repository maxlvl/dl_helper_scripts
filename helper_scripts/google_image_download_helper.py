from datetime import date

from google_images_download import google_images_download 

response = google_images_download.googleimagesdownload()

planet_arguments = ["mercury planet", "venus planet", "earth planet", "mars planet", "saturn planet", "jupiter planet", "neptune planet", "uranus planet"]
date_ranges = {
	"09/01/2019": "09/30/2019",
	"08/01/2019": "08/30/2019",
	"07/01/2019": "07/30/2019"
	}

for planet in planet_arguments:
	for key, value in date_ranges.items():
		time_range = {}
		time_range["time_min"] = key
		time_range["time_max"] = value

		arguments = {
			"keywords": planet,
			"limit": 500,
			"print_urls": True, 
			"size": "medium",
			"time_range": f"{time_range}",
			"output_directory": "./data/",
			"image_directory": f"train/{planet}",
			"chromedriver": "/usr/bin/chromedriver" #this should be the default location of where chromedriver is installed on a linux VM box.
			}


		paths = response.download(arguments)
		print(paths)
