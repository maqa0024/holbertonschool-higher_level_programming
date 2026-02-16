#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Yeni bir lüğət yaradırıq
    new_dict = {}
    
    # Orijinal lüğətdəki hər açar-dəyər cütü üçün
    for key, value in a_dictionary.items():
        # Dəyəri 2-ə vurub yeni lüğətə əlavə edirik
        new_dict[key] = value * 2
    
    # Yeni lüğəti qaytarırıq
    return new_dict
