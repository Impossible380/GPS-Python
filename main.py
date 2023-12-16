import json
from utils import *


if __name__ == "__main__":
    # input_file = input("Dans quelle fichier se trouvent les données demandées ? ")
    actual_file = open("ste-foy.json")
    object_list = json.load(actual_file)

    road_list = extract_ways(object_list)
    graph = create_graph(road_list)
    start_node = ('4.7981541', '45.7327439')
    end_node = ('4.7976545', '45.7329538') # ('4.8078291', '45.7247847')
    # print(graph)

    path = dijkstra(start_node, end_node, graph)
    output_path_json(path)