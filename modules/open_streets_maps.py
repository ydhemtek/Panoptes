#priority:0
from Panoptes import *
import requests
from geopy import distance

def find_nearest_place2(place1_coords, country_code, place2_params, place2_endpoint):
    place2_params["countrycodes"] = country_code
    response = requests.get(place2_endpoint, params=place2_params).json()

    nearest_place2 = None
    nearest_distance = None
    for location in response:
        coords = (float(location['lat']), float(location['lon']))
        distance_to_location = distance.distance(place1_coords, coords).km
        if not nearest_place2 or distance_to_location < nearest_distance:
            nearest_place2 = location['display_name']
            nearest_distance = distance_to_location
    return nearest_place2, nearest_distance

@modules.new("find a place closest to another place")
def close_places() :
    place1 = str(input("\nplace 1 : "))
    place2 = str(input("\nplace 2 : "))
    country_code = str(input("\n(exemple : FR) enter a country : "))
    km = int(input("\nenter a maximum km : "))
    limit1 = int(input(f"\nlimited number of {place1} : "))
    limit2 = int(input(f"\nlimited number of {place2} : "))

    place1_endpoint = "https://nominatim.openstreetmap.org/search"
    place1_params = {
        "q": f"{place1}",
        "format": "json",
        f"limit": {limit1},
        "addressdetails": 1
    }

    place2_endpoint = "https://nominatim.openstreetmap.org/search"
    place2_params = {
        "q": f"{place2}",
        "format": "json",
        f"limit": {limit2},
        "addressdetails": 1
    }
    for place1_location in requests.get(place1_endpoint, params=place1_params).json():
        place1_coords = (float(place1_location['lat']), float(place1_location['lon']))
        nearest_place2, nearest_distance = find_nearest_place2(place1_coords, country_code, place2_params, place2_endpoint)
        if nearest_distance <= km:
            print(f"\nThe nearest {place2} to {place1_location['display_name']} is {nearest_place2} ({nearest_distance:.2f} km away)")
            print(f"Full address: {nearest_place2}")
    if not nearest_place2:
        print("No information found.")
    find_nearest_place2(place1_coords, country_code, place2_params, place2_endpoint)