import json
from utils import *


if __name__ == "__main__":
    # input_file = input("Dans quelle fichier se trouvent les données demandées ? ")
    actual_file = open("ste-foy.json")
    object_list = json.load(actual_file)
    print(len(object_list))

    road_list = extract_ways(object_list)
    print(road_list, len(road_list))