import requests
import json
import csv


def search_nearby_places(place_name):
  # Encode the place name to include in the URL
  encoded_place_name = place_name

  # Make a request to the OpenStreetMap API to get the coordinates of user's location
  geocode_url = f'https://nominatim.openstreetmap.org/search?q={encoded_place_name}&format=json'
  response = requests.get(geocode_url)
  data = json.loads(response.text)

  if len(data) == 0:
    print('Place not found.')
    return

  # Extract the latitude and longitude of the place
  lat = float(data[0]['lat'])
  lon = float(data[0]['lon'])

  # Make a request to the OpenStreetMap API to find nearby area in range of 5km
  nearby_url = f'https://overpass-api.de/api/interpreter?data=[out:json];(node["amenity"="school"](around:5000,{lat},{lon});node["shop"](around:5000,{lat},{lon});node["public_transport"="station"](around:5000,{lat},{lon});node["highway"="road"](around:5000,{lat},{lon}););out;'
  response = requests.get(nearby_url)
  data = response.json()

  
  schools = [] #to put all nearby schols name in a list
  malls = [] # to put all nearby malls in a list
  stations = [] # to put all nearby rail/metro stations in a list
  roads=[] #to put all nearby highway in the list



#sort the particular data from the whole fetched data from api
  
  for element in data['elements']:

    if 'tags' in element and 'amenity' in element['tags'] and element['tags'][
        'amenity'] == 'school':

      schools.append(element['tags'])
      names = [item.get('name', 'Unnamed School') for item in schools[0:]]

    if 'tags' in element and 'shop' in element['tags'] and element['tags'][
        'shop'] == 'mall':
      malls.append(element['tags']['name'])

    if 'tags' in element and 'public_transport' in element['tags'] and element['tags']['public_transport'] == 'station':
        stations.append(element['tags']['name'])

    if 'tags' in element and 'addr:railway' in element['tags'] and element['tags']['railway'] == "subway"  :
        roads.append(element['tags']['name'])






  
  
#schools Calculations(find how many, name and nearest of them)
  print(f'Schools nearby: {len(names)}\n')

  qq = []
  if len(schools) == 1:
    if names[0] == "Unnamed School":
      # continue
      print("Sorry No info found about this school")
    else:
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[0]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
  
      w = lat - latix
      qq.append(w)


  if len(names) == 2:
    if names[0] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    if names[1] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    else:
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[0]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[1]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
  
      x = lat - latix
      qq.append(x)

  
  if len(names) == 3:
    if names[0] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    if names[1] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    if names[2] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    else:
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[0]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[1]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[2]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
  
      x = lat - latix
      qq.append(x)
  
  
  if len(names) == 4:
    if names[0] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    if names[1] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    if names[2] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    if names[3] == "Unnamed School":
      print("Sorry No Lat Long found\n")
    else:
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[0]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[1]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[2]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
      geo0 = f'https://nominatim.openstreetmap.org/search?q={names[3]}&format=json'
      response = requests.get(geo0)
      d = json.loads(response.text)
      latix = float(d[0]['lat'])
  
      x = lat - latix
      qq.append(x)
 
#print all the school names
  for school_name in names:
    print(school_name)

#calculate nearest of them ( if there are less than 5 school in 5km radius)
  if len(schools)<5 and len(schools)>0:
    min_number = min(float(num) for num in qq)
  
    
    if min_number == qq[0]:
      print("\nThe nearest School of all of them is", names[0])
      dist1 = qq[0] * 111.32
      distance1 = f"{dist1:.2f}"
      print("Distance in Km:", distance1)
    elif min_number == qq[1]:
      print("\nThe nearest School of all of them is", names[1])
      dist1 = qq[1] * 111.32
      distance1 = f"{dist1:.2f}"
    elif min_number == qq[2]:
      print("\nThe nearest School of all of them is", names[2])
      dist1 = qq[2] * 111.32
      distance1 = f"{dist1:.2f}"
    elif min_number == qq[3]:
      print("\nThe nearest School of all of them is", names[3])
      dist1 = qq[3] * 111.32
      distance1 = f"{dist1:.2f}"
  else:
      print("\nSorry!Too many Schools Present Can't fetch data to find nearby school")
  






  
#shopping Malls Calculations  
    
  mm=[]   #append (user lat -mall's lat) 

#calcualtion to find how many,name, nearby Malls)
  print("\nThere are",len(malls)," Malls in this area")
  if len(malls) == 0:
    print("\n Sorry! No Malls Found\n")
    
  elif len(malls) == 1:
      print(f'\nMall name: {malls[0]}\n')
   
      mall0 = f'https://nominatim.openstreetmap.org/search?q={malls[0]}&format=json'
      response = requests.get(mall0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat'])
      mall_lat1 = lat- lati1
      
      mm.append(mall_lat1)
  elif len(malls)==2:
      for mall in malls:
        print(f'Mall name: {malls[:-1]}\n')
   
      mall0 = f'https://nominatim.openstreetmap.org/search?q={malls[0]}&format=json'
      response = requests.get(mall0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat'])
      mall_lat2 = lat- lati1
      mm.append(mall_lat2)
      
      mall0 = f'https://nominatim.openstreetmap.org/search?q={malls[1]}&format=json'
      response = requests.get(mall0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat']) 
      mall_lat2 = lat- lati1
      
      mm.append(mall_lat2)
  
  elif len(malls) == 3:
      for mall in malls:
        print(f'\nMall name: {mall}\n')
   
      mall0 = f'https://nominatim.openstreetmap.org/search?q={malls[0]}&format=json'
      response = requests.get(mall0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat'])
      mall_lat3 = lat- lati1
     
      mm.append(mall_lat3)
      
      mall0 = f'https://nominatim.openstreetmap.org/search?q={malls[1]}&format=json'
      response = requests.get(mall0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat']) 
      mall_lat3 = lat- lati1
      
      mm.append(mall_lat3)
    
      mall0 = f'https://nominatim.openstreetmap.org/search?q={malls[2]}&format=json'
      response = requests.get(mall0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat']) 
      mall_lat3 = lat- lati1
     
      mm.append(mall_lat3)
  
  mn=[]
  for i,item in enumerate(mm):
      if i == 0:
          a=abs(float(item))
          mn.append(a)


  if len(malls)<=3 and len(malls) >0:
    min_number = min(float(num) for num in mn)
  
    if min_number == mn[0]:
      print("The nearest Mall of all of them is", malls[0])
      dist1 = mn[0] * 111.32
      distance1 = f"{dist1:.2f}"
      print("Distance in Km:", distance1)
      breakpoint
    elif min_number == mn[1]:
      print("The nearest Mall of all of them is", malls[1])
      dist1 = mn[1] * 111.32
      distance1 = f"{dist1:.2f}"
    elif min_number == mn[3]:
      print("The nearest Mall of all of them is", malls[2])
      dist1 = mn[2] * 111.32
      distance1 = f"{dist1:.2f}"
  else:
    print("\n Sorry No Can't fetch data to find the closest Mall")
  
  


  

#Railway Calculations

  ril=[]
  ril2=[]
  if len(stations) == 0:
    print("\nSorry! No Nearby Railway station Found\n")
  elif len(stations) == 1:
    print(f'\nRailway Stations nearby: {len(stations)}\n')
    for station in stations:
      print(f'\nRailway Station names: {station}\n')
   
      rail0 = f'https://nominatim.openstreetmap.org/search?q={stations[0]}&format=json'
      response = requests.get(rail0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat'])
      ri_1 = lat- lati1
      print("Distance in Km",ri_1)
  
  elif len(stations) == 2:
    print(f'\nRailway Stations nearby: {len(stations)}\n')
    for station in stations:
      print(f'\nRailway Station names: {station}\n')
   
      rail0 = f'https://nominatim.openstreetmap.org/search?q={stations[0]}&format=json'
      response = requests.get(rail0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat'])
      ri = lat- lati1
      
      rail0 = f'https://nominatim.openstreetmap.org/search?q={stations[0]}&format=json'
      response = requests.get(rail0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat'])
      ri = lat- lati1
      ril.append(ri)
  elif len(stations) == 3:
    print(f'\nRailway Stations nearby: {len(stations)}\n')
    for station in stations:
      print(f'\nRailway Station names: {station}\n')
   
      rail0 = f'https://nominatim.openstreetmap.org/search?q={stations[0]}&format=json'
      response = requests.get(rail0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat'])
      ri = lat- lati1
      
      rail0 = f'https://nominatim.openstreetmap.org/search?q={stations[0]}&format=json'
      response = requests.get(rail0)
      ddx = json.loads(response.text)
      # print(ddx)
      lati1 = float(ddx[0]['lat'])
      ri = lat- lati1
      ril.append(ri)
   
  elif len(stations) > 3:
    print(f'\nRailway Stations nearby: {len(stations)}\n')
    for station in stations:
      print(f'\nRailway Station names: {station}\n')

  


  for i,item in enumerate(ril):
        if i == 0:
            a=abs(float(item))
            ril2.append(a)

  
  if len(stations)<=3 and len(stations)>0:
    min_number = min(float(num) for num in ril2)
  
    if min_number == ril2[0]:
      print("The nearest Station of all of them is", stations[0])
      dist1 = ril[0] * 111.32
      distance1 = f"{dist1:.2f}"
      print("Distance in Km:", distance1)
      breakpoint
    elif min_number == ril2[1]:
      print("The nearest Station of all of them is", stations[1])
      dist1 = ril[1] * 111.32
      distance1 = f"{dist1:.2f}"
    elif min_number == ril2[3]:
      print("The nearest Station of all of them is", stations[2])
      dist1 = ril[2] * 111.32
      distance1 = f"{dist1:.2f}"
  elif len(stations)>3:
    print("Sorry! Too many Stations found can't fetch the data to find nearest of them")
  

  if len(roads) == 0:
    print( "\nSorry! No Nearby roads Found\n")
  else:
    print(f'\nRoads nearby: {len(roads)}')
    print(f'\nRoad names: {roads}\n')

  # if len(metro) == 0:
  #   print("Metro: Sorry! No Metro station Found\n")
  # else:
  #   print(f'Metro nearby: {len(metro)}')
  #   print(f'Metro Station names: {metro}')



  
# Create a CSV file and  append
  create_csv_file = open('your_places.csv', 'w', newline='')
  csv_append = csv.writer(create_csv_file)

  
  # Write the data to the CSV file
  if len(schools)==0:
    csv_append.writerow(['School Name:-'])
    csv_append.writerow(["Sorry No nearby School Found"])
  else:
    csv_append.writerow(['School Names:-'])
    csv_append.writerow(names)

  if len(malls)==0:
    csv_append.writerow(['Mall:-'])
    csv_append.writerow(["Sorry No nearby Malls Found"])
  else:
    csv_append.writerow(['Mall Name:-'])
    csv_append.writerow(malls)
    
  if len(stations)==0:
    csv_append.writerow(['Rail Stations:-'])
    csv_append.writerow(["Sorry No Rail Stations Found"])
  else:
    csv_append.writerow(['Railway Stations:-'])
    csv_append.writerow(stations)
  if len(roads)==0:
    csv_append.writerow(['Highways:-'])
    csv_append.writerow(["Sorry No Highways Found"])
    
  else:
    csv_append.writerow(['Highways:-'])
    csv_append.writerow(roads)



  # Close the CSV file
  create_csv_file.close()
# place = "Sikandarpur

place=input("Enter the place: ")

search_nearby_places(place)
