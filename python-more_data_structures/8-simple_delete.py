#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Əgər açar lüğətdə mövcuddursa
    if key in a_dictionary:
        # Açarı lüğətdən silirik
        del a_dictionary[key]
    # Dəyişdirilmiş lüğəti qaytarırıq
    return a_dictionary
