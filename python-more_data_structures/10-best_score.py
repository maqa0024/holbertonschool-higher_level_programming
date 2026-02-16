#!/usr/bin/python3
def best_score(a_dictionary):
    # Əgər lüğət None-dırsa və ya boşdursa
    if not a_dictionary:
        return None
    
    # Ən böyük dəyəri tapırıq
    best_key = None
    best_value = float('-inf')  # Ən kiçik başlanğıc dəyər
    
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    
    return best_key
