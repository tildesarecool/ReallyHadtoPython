# ch. 10 exercise 8 - ITERATING OVER A DICTIONARY IN PYTHON

def get_most_common_enemy(enemies_dict):
    enemy_count = float("-inf")
    output_dict = {}

    for value in enemies_dict.values():
        if enemy_count < int(value):
            enemy_count = int(value)

    for enemies in enemies_dict:
        
        if enemies_dict[enemies] == enemy_count:
{enemy_count}|")
            if enemies != None:
                return enemies
            else:
                return None