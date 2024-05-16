# well i just got the solution to this one
# since i couldn't figure it out
# I think i might need some practice with dictionaries
# because I don't think i was even close

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict