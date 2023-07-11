import requests
import math

geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'

city = input("Enter your place: ")  # Prompt the user to enter the city name

params = {
    'address': city,
    'key': 'PLEASE WRITE YOUR OWN API KEY'
}

response = requests.get(geocode_url, params=params)
data = response.json()
# print(data)

# Process the response
if data['status'] == 'OK':
    location = data['results'][0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']
  
  
places_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'





# school
params = {
    'location': f"{latitude},{longitude}",
    'radius': 5000,
    'type': 'school',
    'key': 'AIzaSyABpAsoBgH3DBlPTZwlF739MnlMBMtgJow'
}

response = requests.get(places_url, params=params)
data = response.json()
# print(data)

# Process the response
if data['status'] == 'OK':
    results = data['results']
    print(f"No. of schools {len(results)}\n")
    for place in results:
        name = place['name']
        address = place['vicinity']
        print(f" School Name: {name}")
      

    # Calculate distance between your plce and school
    def calculate_distance(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    # Find the nearest school
    nearest_school = None
    distance = float('inf')  # Initialize with infinity

    for place in results:
        name = place['name']
        address = place['vicinity']
        school_latitude = place['geometry']['location']['lat']
        school_longitude = place['geometry']['location']['lng']
        
        distance = calculate_distance(latitude, longitude, school_latitude, school_longitude)
        
        if distance < distance:
            distance = distance
            nearest_school = {
                'name': name,
                'address': address,
                'distance': distance
            }
    
    if nearest_school:
        print(f"\nNearest School: {nearest_school['name']}")
        print(f"Address: {nearest_school['address']}")
        print(f"Distance: {nearest_school['distance']} km")
    else:
        print("Sorry ! unable to find nearest school.")
else:
    print(f"Error: {data['status']} No school Found")








# shopping mall

params = {
    'location': f"{latitude},{longitude}",
    'radius': 5000,
    'type': 'shopping_mall',
    'key': 'AIzaSyABpAsoBgH3DBlPTZwlF739MnlMBMtgJow'
}

response = requests.get(places_url, params=params)
data = response.json()
# print(data)

# # Process the response
if data['status'] == 'OK':
    results = data['results']
    print("\nNo of Malls present",len(results),"\n")
    for place in results:
      # print(place)
      name = place['name']
      print(f" Mall Name: {name}")
      

    # Calculate distance between two coordinates
    def calculate_distance(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    # Find the nearest mall
    nearest_mall = None
    nearest_distance = float('inf')  # Initialize with infinity

    for place in results:
        name = place['name']
        address = place['vicinity']
        mall_latitude = place['geometry']['location']['lat']
        mall_longitude = place['geometry']['location']['lng']
        
        distance = calculate_distance(latitude, longitude, mall_latitude, mall_longitude)
        
        if distance < nearest_distance:
            distance = distance
            nearest_mall = {
                'name': name,
                'address': address,
                'distance': distance
            }
    
    if nearest_mall:
        print(f"\nNearest Mall: {nearest_mall['name']}")
        print(f"Address: {nearest_mall['address']}")
        print(f"Distance: {nearest_mall['distance']} km")
    else:
        print("Sorry! Unable to find nearest Mall.")
else:
    print(f"\nError: {data['status']} No Malls found")






# railway
params = {
    'location': f"{latitude},{longitude}",
    'radius': 5000,
    'type': 'train_station',
    'key': 'AIzaSyABpAsoBgH3DBlPTZwlF739MnlMBMtgJow'
}

response = requests.get(places_url, params=params)
data = response.json()


# # Process the response
if data['status'] == 'OK':
    results = data['results']
    # print(results)
    print("\nNo of Rail Stations present",len(results),"\n")
    for place in results:
      # print(place)
      name = place['name']
      print(f"Rail Station Name: {name}")
      

#     # Calculate distance between two coordinates
    def calculate_distance(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    # Find the nearest rail
    nearest_rail = None
    nearest_distance = float('inf')  # Initialize with infinity

    for place in results:
        name = place['name']
        address = place['vicinity']
        rail_latitude = place['geometry']['location']['lat']
        rail_longitude = place['geometry']['location']['lng']
        
        distance = calculate_distance(latitude, longitude, rail_latitude, rail_longitude)
        
        if distance < nearest_distance:
            distance = distance
            nearest_station = {
                'name': name,
                'distance': distance
            }
    
    if nearest_station:
        print(f"\nNearest station: {nearest_station['name']}")
        print(f"Distance: {nearest_station['distance']} km")
    else:
        print("Sorry! Unable to find nearest Rail Station")
else:
    print(f"\nError: {data['status']} No Rail Stations found")







# subway_train
params = {
    'location': f"{latitude},{longitude}",
    'radius': 5000,
    'type': 'subway_station',
    'key': 'AIzaSyABpAsoBgH3DBlPTZwlF739MnlMBMtgJow'
}

response = requests.get(places_url, params=params)
data = response.json()
# print(data)

# # Process the response
if data['status'] == 'OK':
    results = data['results']
    # print(results)
    print("\nNo of Metro Stations present",len(results),"\n")
    for place in results:
      # print(place)
      name = place['name']
      print(f" Metro Station Name: {name}")
      

#     # Calculate distance between two coordinates
    def calculate_distance(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    # Find the nearest school
    nearest_subway = None
    distance = float('inf')  # Initialize with infinity

    for place in results:
        name = place['name']
        address = place['vicinity']
        subway_latitude = place['geometry']['location']['lat']
        subway_longitude = place['geometry']['location']['lng']
        
        distance = calculate_distance(latitude, longitude, subway_latitude, subway_longitude)
        
        if distance < distance:
            distance = distance
            nearest_station = {
                'name': name,
                'distance': distance
            }
    
    if nearest_station:
        print(f"\nNearest Metro station: {nearest_station['name']}")
        print(f"Distance: {nearest_station['distance']} km")
    else:
        print("SOrry ! Unable to find nearest Metro station")
else:
    print(f"\nError: {data['status']} No Metro  found")









# highway
params = {
    'location': f"{latitude},{longitude}",
    'radius': 5000,
    'type': 'route',
    'key': 'AIzaSyABpAsoBgH3DBlPTZwlF739MnlMBMtgJow'
}

response = requests.get(places_url, params=params)
data = response.json()

# # Process the response
if data['status'] == 'OK':
    results = data['results']
    # print(results)
    print("\nNo of Highway present",len(results),"\n")
    for place in results:
      # print(place)
      name = place['name']
      print(f"Highway Name: {name}")
      

#     # Calculate distance between two coordinates
    def calculate_distance(lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    # Find the nearest highway
    nearest_highway = None
    nearest_distance = float('inf')  # Initialize with infinity

    for place in results:
        name = place['name']
        address = place['vicinity']
        highway_latitude = place['geometry']['location']['lat']
        highway_longitude = place['geometry']['location']['lng']
        
        distance = calculate_distance(latitude, longitude, highway_latitude, highway_longitude)
        
        if distance < nearest_distance:
            distance = distance
            nearest_highway = {
                'name': name,
                'distance': distance
            }
    
    if nearest_highway:
        print(f"\nNearest Highway : {nearest_highway['name']}")
        print(f"Distance: {nearest_highway['distance']} km")
    else:
        print("Sorry! Unable to find nearest Highway")
else:
    print(f"\nError: {data['status']} No Highway  found")
