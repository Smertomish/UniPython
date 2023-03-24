import json


with open("animals.json") as read_file:
    data_animals = json.load(read_file)

print(type(data_animals))

count_diurnal = 0
animals_weight = dict()

for animal in data_animals["animals"]:

    # поиск всех птиц
    if animal["animal_type"] == "Bird":
        print(json.dumps(animal, indent=2))
        print()

    # подсчёт всех дневных животных
    if animal["active_time"] == "Diurnal":
        count_diurnal += 1

    # поиск наименьшего веса
    animals_weight[float(animal["weight_min"])] = animal["name"]
    animals_weight_min = [w for w in animals_weight.keys()]
    animals_weight_min.sort()
    animals_weight_min = animals_weight_min[0]


print("количество дневных животных: ", count_diurnal)
print(animals_weight)
print(f"Минимальный вес:  {animals_weight[animals_weight_min]}: {animals_weight_min}")