# bootdev seems to be freaking out so i'll come back to this later.

def get_most_common_enemy(enemies_dict):

    max_so_far = float("-inf")
    enemy_name_max_count = None

    for enemies in enemies_dict:
        if max_so_far > enemies_dict[enemies]:
            enemy_name_max_count = enemies
            print(f"enemy max count is {enemy_name_max_count} and enemies is {enemies}")
    
    
