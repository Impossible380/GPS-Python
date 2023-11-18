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
    print(road_list)