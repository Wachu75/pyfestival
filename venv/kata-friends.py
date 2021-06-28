import json

#names = ["Janek", "Inga", "Krzysztof", "Basia", "Ryan", "Kieran", "Mark", "Olga"]
friends = []
def friend(x):
    for name in x:
        if len(name) == 4:
            friends.append(name)
    return print(json.dumps(friends))

friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"])
