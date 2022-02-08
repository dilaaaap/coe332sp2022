import json

def compute_average_mass(a_list_of_dicts, a_key_string):
    total_mass = 0.
    for i in range(len(a_list_of_dicts)):
        total_mass += float(a_list_of_dicts[i][a_key_string])
    return (total_mass / len(a_list_of_dicts))

with open('Meteorite_Landings.json', 'r') as f:
    ml_data = json.load(f)

print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'))
