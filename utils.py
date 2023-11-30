import json
import copy


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