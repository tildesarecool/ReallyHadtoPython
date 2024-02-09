def find_missing_ids(first_ids, second_ids):

    final_set = set()

    first_id_set = set(first_ids)
    #print(first_id_set)
    sec_id_set = set(second_ids)
    #print(sec_id_set)

    final_set = first_id_set.difference(sec_id_set)
    #print(final_set)

    
    return list(final_set)
