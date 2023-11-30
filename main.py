import json
from utils import *


if __name__ == "__main__":
    # input_file = input("Dans quelle fichier se trouvent les données demandées ? ")
    actual_file = open("ste-foy.json")
    object_list = json.load(actual_file)

    road_list = extract_ways(object_list)
    graph = create_graph(road_list)
    print(len(graph))