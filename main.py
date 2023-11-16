import json


if __name__ == "__main__":
    input_file = input("Dans quelle fichier se trouvent les données demandées ? ")
    actual_file = open(input_file)
    print(type(json.load(actual_file)))