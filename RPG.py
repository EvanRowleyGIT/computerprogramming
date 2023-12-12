Health = 100
EnemyHealth = 100
Starting_Items = "Black robe, Breastplate, Warsword, Dagger"
Inventory = []
Gold = 0
Dead = False
Enemy = ()
fight_option = 'f'
def enemy():
    while True:
        fight_option = input("Do you wish to fight this creature? ")
        if fight_option == 'y':
            print("You pull out your warsword, deciding to fight")
            player_attack = random.randint(1,10)
            enemy_attack = random.randint(1,10)
            print(f"You swing your sword, attacking the enemy for {player_attack} damage, but the enemy attacks you back for {enemy_attack} damage")
            Health = Health - enemy_attack
            EnemyHealth = EnemyHealth - player_attack
            if Health <= 0:
                print("You were slain.")
                break
            elif EnemyHealth <=0:
                print("You have slaughtered the enemy")
                break
        elif fight_option == 'n':
            run = random.randint(0,1)
            if run == 1:
                print("You run away succesfully")
                break
            if run == 0:
                print("You tried to run away, but the enemy skill managed to attack as you ran.")
                Health = Health - 50
    
import random
random1 = random.randint(1,4)
random2 = random.randint(1,3)


Name = input("Man With Black Hood>>> Greetings, what is your name mysterious slayer? ")
print(f"Man With Black Hood>>> It is very good to meet you {Name}. I am guessing you are a slayer traveling here to destroy the demons and monsters around here, because of the gear you carry. I am thankful for your help. ")
print("Man With Black Hood>>> You should probobly get going. ")    
user_input2 = print("Press 'w' to walk, and press 'p' to open your inventory and check your health. ")
while Dead == False:
    if input() == "p":
        print(f"{Name}, Your health is {Health}. Your items are, {Starting_Items}. You have collected {Gold} Gold ")
    elif input() == "w":
        if random1 == random.randint(1,4):
            if random1 <= 3:
                random2 = random.randint(1,3)
            if random2 == 1:
                print("While you are walking, out of the fog a shade appears, press 'y' to attack, and 'n' to run away. ")
                Enemy = ("Shade")
                enemy()
            elif random2 == 2:
                print("While you are walking, out of the fog a demon of darkness appears, press 'y' to attack and 'n' to run away. ")
                Enemy = ("Demon of Darkness")
                enemy()
            elif random2 == 3:
                print("While you are walking, out of the fog a mere orc appears. Kill it quickly with 'y'. If you must run, press 'n' ")
                Enemy = ("Orc")
                enemy()
            elif random1 >= 2:
                print("As you walk, you see nothing notable press 'w' to keep going. Press, 'p' to check your inventory, and check your health ")
                enemy()