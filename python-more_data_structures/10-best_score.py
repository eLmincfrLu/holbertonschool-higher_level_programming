#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    maxi_v = a_dictionary[list(a_dictionary)[0]]
    maxi_k = list(a_dictionary)[0]
    for key, value in a_dictionary.items():
        if value > maxi_v:
            maxi_v = value
            maxi_k = key
    return maxi_k
