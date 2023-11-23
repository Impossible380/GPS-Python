import json
import copy


def extract_ways(object_list):
    road_list = []
    for object in object_list:
        if object["type"] == "way":
            road_list.append(object)

    return road_list


def create_graph(road_list):
    for actual_road in road_list:
        for crossing_road in road_list:
            if actual_road["nodes"]["lat"] == crossing_road["nodes"]["lat"] and \
                    actual_road["nodes"]["lon"] == crossing_road["nodes"]["lon"]:
                pass


def output_json(road_list):

    # json.load, charge un Fichier json depuis le disque dans un dico / liste

    # Objet standard associé à la carte (liste des routes)
    output_template = json.load(open("liste_routes.json"))

    # Objet standard associé à une route (liste de segments)
    feature_template = json.load(open("routes.json"))

    # On itere sur chacune des routes...
    for i, road in enumerate(road_list):

        # On utilise deepcopy pour copier intégralement et récursivement tout le contenu du dictionnaire
        route_output = copy.deepcopy(feature_template)

        # ...Et sur chacune des coordonnées
        for j, node in enumerate(road["nodes"]):
            lat = node["lat"]
            lon = node["lon"]
            coordinate = [lon,lat]
            route_output["geometry"]["coordinates"].append(coordinate)
        output_template["features"].append(route_output)

    # Bonne pratique : with open permet d'ouvrir un fichier sous un autre nom et le ferme automatiquement à la fin du
    # bloc with
    with open("out.json","w") as f:

        # json.dumps, va traduire notre dico / liste vers une chaine de caractères (que l'on écrit sur le disque pour
        # avoir un Fichier json :) )
        f.write(json.dumps(output_template))
