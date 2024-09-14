from constants import entity_unit_map
from units import more_unit_variations

# DO NOT REMOVE PLEASE
# used to generate collated_units variable in constants.py

yes = dict()

for key in entity_unit_map:
    yes[key] = set()
    for x in entity_unit_map[key]:
        yes[key] = yes[key].union(more_unit_variations[x])

print(yes)