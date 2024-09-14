import difflib
# from constants import entity_unit_map
# from units import unit_variations
from constants import collated_units

# Your custom word list
vocabulary = {"apple", "banana", "grape", "orange", "mango"}

def spell_check(word, unit_type):
    """
    word: the potentially erroneous string
    unit_type: "width"|"depth"|"height"|"item_weigth" etc.
    """
    # Get the closest match from the vocabulary
    try:
        # vocab = entity_unit_map[unit_type]
        # vocab = unit_variations[vocab]
        vocab = collated_units[unit_type]
    except KeyError:
        print(f"spell_check.py : unit_type {unit_type} is not a valid input...")
        exit(0)

    matches = difflib.get_close_matches(word, vocab, n=1, cutoff=0.8)
    if matches:
        return matches[0]
    else:
        return f"No suggestions for '{word}'"

# Test
word = "gsm"
suggestion = spell_check(word, "item_weight")
print(suggestion)
