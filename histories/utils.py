import datetime
import json
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def calculate_distance(route_line):
    distance = 0
    route_line = json.loads(route_line)
    for index in range(len(route_line) - 1):
        lon1 = route_line[index]["lon"]
        lat1 = route_line[index]["lat"]
        lon2 = route_line[index + 1]["lon"]
        lat2 = route_line[index + 1]["lat"]
        distance += haversine(lon1, lat1, lon2, lat2)
    return "%.1f" % distance


def calculate_duration(start, end):
    time_diff = end - start
    duration = datetime.timedelta(seconds=time_diff.total_seconds())
    return str(duration)
