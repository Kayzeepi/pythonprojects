# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#global scope

# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         player_health += potion_strength
#         print(player_health)

#     drink_potion()
    
# print(player_health)

# There is no block scope

# game_level = 3

# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level <5:
#         new_enemy = enemies[0]

#     print(new_enemy)

#modifying global scope

# enemies = "Skeleton"

# def increase_enemies():
#     global enemies #<<this is important
#     enemies = "Zombie"
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#global constants

# PI = 3.432
# URL = "https://www.google.com"
