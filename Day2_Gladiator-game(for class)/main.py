import random
import time
class Gladiator:
    def __init__(self,name):
        self.name = name
        self.hp = 30
        self.power = 1
    def attack(self,enemy):
        self.power = random.randint(1, 8)
        enemy.hp -= self.power
        if enemy.hp < 0:
            enemy.hp = 0
    def situation(self):
        print(self.name)
        print(f"HP : {self.hp}")
class Arena:
    def __init__(self,fighter1 , fighter2):
        self.f1 = fighter1
        self.f2 = fighter2
    def printer(self):
        time.sleep(4)
        print("#" * 10)
        print("STATUS: ")
        print("Team 1 :")
        self.f1.situation()
        print("Team 2 :")
        self.f2.situation()
    def start_battle(self):
        print("\n" + "*" * 40)
        self.f1.situation()
        print("\n" + "*" * 20)
        print("VS")
        print("" + "*" * 20)
        self.f2.situation()
        print("*" * 40)
        input("\n Hold your breath... Press ENTER to start the battle! 🔥")
        starter = random.randint(1,2)
        if starter == 1:
            while self.f1.hp > 0 and self.f2.hp > 0:
                self.printer()
                self.f1.attack(self.f2)
                print("Team 1 is attacking !!!!")
                time.sleep(2.5)
                print(f"Damage : {self.f1.power}")
                if self.f2.hp <= 0:
                    self.printer()
                    print("*" * 40)
                    print("THE WINNER : ")
                    print(self.f1.name)
                    break
                self.f2.attack(self.f1)
                print("Team 2 is attacking !!!!")
                time.sleep(2.5)
                print(f"Damage : {self.f2.power}")
                if self.f1.hp <= 0:
                    self.printer()
                    print("*" * 40)
                    print("THE WINNER : ")
                    print(self.f2.name)
                    break
        else:
            while self.f1.hp > 0 and self.f2.hp > 0:
                self.printer()
                self.f2.attack(self.f1)
                print("Team 2 is attacking !!!!")
                time.sleep(2.5)
                print(f"Damage : {self.f2.power}")
                if self.f1.hp <= 0:
                    self.printer()
                    print("*" * 40)
                    print("THE WINNER : ")
                    print(self.f2.name)
                    break
                self.f1.attack(self.f2)
                print("Team 1 is attacking !!!!")
                time.sleep(2.5)
                print(f"Damage : {self.f1.power}")
                if self.f2.hp <= 0:
                    self.printer()
                    print("*" * 40)
                    print("THE WINNER : ")
                    print(self.f1.name)
                    break

spartacus = Gladiator("Spartacus")
crixus = Gladiator("Crixus")
coliseum = Arena(spartacus,crixus)
coliseum.start_battle()






