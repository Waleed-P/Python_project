import random
Player_hp=100
Dragon_hp=100
def generate_random_story():
    players = ["Hero", "Adventurer", "Knight", "Warrior", "Explorer"]
    actions = ["encountered", "fought", "battled", "confronted", "challenged"]
    dragons = ["Dragon", "Wyvern", "Drake", "Serpent", "Firedrake"]
    outcomes = ["victorious", "triumphant", "defeated", "brave", "courageous"]
    locations = ["mountain", "cave", "forest", "valley", "castle"]
    player = random.choice(players)
    action = random.choice(actions)
    dragon = random.choice(dragons)
    outcome = random.choice(outcomes)
    location = random.choice(locations)
    print("Once upon a time..",player,action,'a mighty ',dragon,'in the',location,'and emerged ',outcome,'!')


for i in range(0,10):
    generate_random_story()
    dhp=random.randint(1,20)
    php=random.randint(1,20)
    
    if Dragon_hp<=0 or Player_hp<0:
        break
    
    Dragon_hp=Dragon_hp-dhp
    Player_hp=Player_hp-php
    print('player hp=',Player_hp,'dragon hp=',Dragon_hp)
    
if Dragon_hp<=0 and Player_hp>=0:
    print("player wins")
elif Player_hp<=0 and Dragon_hp>=0:
    print("Dragon wins")
elif Player_hp<=0 and Dragon_hp<0:
    if Player_hp>Dragon_hp:
        print("player wins")
    else:
        print("Dragon wins")
elif Player_hp==0 and Dragon_hp==0:
    print('Tie')
