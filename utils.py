import json
import copy

from math import *


# Calcul de la distance entre deux coordonnées sur la terre.
# Les formules mathématiques constituant la fonction ne sont pas importantes pour le reste du code.
def haversine(lon1, lat1, lon2, lat2):
    R = 6372.8  # Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * asin(sqrt(a))

    return R * c


# distances = { (12.0, 4.2): 0, (10.0, 5.6): 5, (1.4,7.12): 3, (2.3,4): Inf }
# arguments de la fonction: distances et visited
# retour de la fonction: node qui n'est pas visitée et qui a la distance la plus petite


def closest_node(distances, visited):
    min_dist = float(inf)
    min_node = 0

    for node in distances:

        if node not in visited and distances[node] < min_dist:
            min_dist = distances[node]
            min_node = node

    print(min_node)
    return min_node


def dijkstra(start, nodes):
    distances = {}
    visited = []

    for k in nodes:
        distances[k] = float(inf)
    distances[start] = 0

    for i in range(len(nodes)):
        # print(distances)
        current_node = closest_node(distances, visited)
        visited.append(current_node)

        for voisin in nodes[current_node]:
            new_distance = distances[current_node] + haversine(float(current_node[0]), float(current_node[1]),
                                                               float(voisin[0]), float(voisin[1]))

            if new_distance < distances[current_node]:
                distances[current_node] = new_distance

    # print(distances[current_node])


def extract_ways(object_list):
    road_list = []
    for object in object_list:
        if object["type"] == "way":
            road_list.append(object)

    return road_list


def create_graph(road_list):
    graph = {}

    for actual_road in road_list:
        for j, actual_road_node in enumerate(actual_road["nodes"]):
            lon = actual_road_node["lon"]
            lat = actual_road_node["lat"]

            if not (lon, lat) in graph:
                graph[(lon, lat)] = []

            if j > 0:
                adj_lon = actual_road["nodes"][j - 1]["lon"]
                adj_lat = actual_road["nodes"][j - 1]["lat"]
                graph[(lon, lat)].append((adj_lon, adj_lat))

            if j < len(actual_road["nodes"]) - 1:
                adj_lon = actual_road["nodes"][j + 1]["lon"]
                adj_lat = actual_road["nodes"][j + 1]["lat"]
                graph[(lon, lat)].append((adj_lon, adj_lat))

    return graph


def output_json(road_list):

    # json.load, charge un Fichier json depuis le disque dans un dico / liste

    # Objet standard associé à la carte (liste des routes)
    output_road_list = json.load(open("road_list.json"))

    # Objet standard associé à une route (liste de segments)
    feature_road = json.load(open("road.json"))

    # On itere sur chacune des routes...
    for i, road in enumerate(road_list):

        # On utilise deepcopy pour copier intégralement et récursivement tout le contenu du dictionnaire
        output_road_item = copy.deepcopy(feature_road)

        # ...Et sur chacune des coordonnées
        for j, node in enumerate(road["nodes"]):
            lon = node["lon"]
            lat = node["lat"]
            coordinates = [lon, lat]
            output_road_item["geometry"]["coordinates"].append(coordinates)

        output_road_list["features"].append(output_road_item)

    # Bonne pratique : with open permet d'ouvrir un fichier sous un autre nom et le ferme automatiquement à la fin du
    # bloc with
    with open("out.json", "w") as out_file:

        # json.dumps, va traduire notre dico / liste vers une chaine de caractères (que l'on écrit sur le disque pour
        # avoir un Fichier json :) )
        out_file.write(json.dumps(output_road_list))