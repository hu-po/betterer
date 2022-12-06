import cProfile
import uuid
import random

# CoPilot
# PROMPT: "a function to sort a dictionary by value"
def copilot_sort_by_value(d):
    items=d.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    return [ backitems[i][1] for i in range(0,len(backitems))]

# ChatGPT
# PROMPT: "write a python function to sort a dictionary by value"
# PROMPT: "can you write that function so that it returns a list of the sorted keys"
# PROMPT: "Modify the function so that it sorts by ascending order"
def chatgpt_sort_dictionary_by_value(d):
  # Create a list of tuples where the first element is the key and the second element is the value
  items = [(key, value) for key, value in d.items()]

  # Sort the list of tuples by the second element (the value) in ascending order
  sorted_items = sorted(items, key=lambda item: item[1])

  # Create a new list of the sorted keys
  sorted_keys = [key for key, value in sorted_items]

  return sorted_keys


if __name__ == "__main__":

    # Make a large random dictionary with uuids as keys and ints as values
    d = {str(uuid.uuid4()): _ for _ in range(10000)}

    # Shuffle the dictionary
    d = {k: d[k] for k in random.sample(d.keys(), len(d))}

    # test dictionary
    # d = {'a': 2, 'b': 4, 'c': 3, 'd': 1, 'e': 5}
    # print("Original dictionary:", d)

    # assert that the two functions return the same result
    print("CoPilot:", copilot_sort_by_value(d))
    print("ChatGPT:", chatgpt_sort_dictionary_by_value(d))
    assert copilot_sort_by_value(d) == chatgpt_sort_dictionary_by_value(d)

    # profile the two functions
    cProfile.run('copilot_sort_by_value(d)')
    cProfile.run('chatgpt_sort_dictionary_by_value(d)')

    # Winner is ChatGPT!