Health = 100
EnemyHealth = 100
Starting_Items = "Black robe, Breastplate, Warsword, Dagger"
Gold = 0
Dead = False
Enemy = ()
import random

Name = input("Man With Black Hood>>> Greetings, what is your name mysterious slayer? ")
print(f"Man With Black Hood>>> It is very good to meet you {Name}. I am guessing you are a slayer traveling here to destroy the demons and monsters around here, because of the gear you carry. I am thankful for your help. ")
print("Man With Black Hood>>> You should probobly get going. ")
user_input2 = print("Press 'w' to walk, and press 'p' to open your inventory and check your health. ")

while Dead == False:
    if input() == "p":
        print(f"{Name}, Your health is {Health}. Your items are, {Starting_Items}. You have collected {Gold} Gold ")
    elif input() == "w":
        if random.randint(1,4):
            if random <= 3:
                print("You walk in a foggy, grassy field")
            if random == 4:
                print(f"While you are walking, something leaps out of the fog, ready to attack. ")
                random.randint(1,3)
                if random == 1:
                    print("It is a Demon. Attack with 'a'. To run, 'r'")
                elif random == 2:
                    print("It is a Shade. Attack with 'a'. To run, 'r'")
                elif random == 3:
                    print("It is a puny Orc. Attack to end its pitiful life with 'a', To run, 'r'")
                def attack_enemy():
                    while True:
                        if Health > 0:
                            your_attack = random.randint(10,100)
                            print(f"You attacked the enemy for {your_attack} damage.")
                            EnemyHealth -= your_attack
                        
                        if EnemyHealth > 0:
                            enemy_attack = random.randint(10,100)
                            print(f"The enemy attacked you for {enemy_attack} damage.")
                            Health -= enemy_attack

                        if Health <= 0:
                            print("You have perished.")
                            break

                        elif EnemyHealth <= 0:
                            print("You slaughtered the Enemy.")
                            print("You have recieved 25 health and an item in your inventory.")
                            Health += 25
                            break

    else:
        print("thats not going to work...")

# i = random.randint(1,4)
# if i == 4:
#     print(f"While you are walking, something leaps out of the fog, ready to attack.")

# random.randint(1,3)
# random = Enemy
# if Enemy == 1:
#     print("It is a Demon. Attack with 'a'. To run, 'r' ")
# elif Enemy == 2:
#     print("It is a Shade. Attack with 'a'. To run, 'r' ")
# elif Enemy == 3:
#     print("It is a puny Orc. Attack with 'a'. To run, 'r' ")