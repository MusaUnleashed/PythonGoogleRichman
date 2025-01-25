from csv import DictReader

with open("cow.csv") as f:
    reader = DictReader(f)
    for d in reader:
        # print(d)
        print(d["name"], d["population"])

# <ul>
#     <li>Afghanistan: 2,838 km</li>
#     <li>Aland Islands: 3,374 km</li>
#     <li>Albania: 1,687 km</li>
#     ...
# </ul>

# originally from http://stackoverflow.com/a/15737218/57952 :
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km
