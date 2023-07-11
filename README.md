# Find-nearbys
This is a python project, I created using Open Street Map api and also with google maps api
(open Street Map api is in find your location.py file  and google api is in  g_maps_api.py)

{Remember if you are using g_maps_api  please paste your own api key to the program section [params section (Line 10)]

[AIM:- In here program expects an input of a place if that place exist in real world and it will
	give the output of
		 1. How many Schools, Names of them and which one is nearest to you
		 2. How many Malls, Names of them and which one is nearest to you
		 1. How many Rail Stations, Names of them and which one is nearest to you
   	and store all those schools, malls,stations name in a .csv file for later use 
   
   NOTE: it can calculate only in the radius of 5km of that place 
]

[only for who is using open street api(find your location.py]

[Problems: It can only find the nearest Schools if there are max 4 schools in the radius of 5 km otherwise
           it can't fetch data to find the nearest,
	same as  Max 3 malls to find nearby and 3 railway stations to find nearby
	
	   rememeber in my code if you rerun and retype the place name with a new one that previous data  was stored in .csv file will be deleted
	   (to fix that on line 405 change the value w to a it will not overwrite the data)
    
	   ( to change the name of .csv file change the file name "your_places" to your desired name in line 405)
]


[if you are using google maps api(g_maps_api.py
No problems found... except I didn't write code to store it to .csv you can write it by your won
but make sure put your input like placename,city name(if your place can't find by api)
]


I've tested it with  this areas:
Gurgaon:
palam vihar, Leisure Valley Park, Aravali Biodiversity Park, Damdama Lake, DLF phase 2

KOlkata:
DUm DUm, Naihati,Barrackpore
