class Game:
    def __init__(self):
        self.life=90
        player_name=input("enter player name :")
        self.name=player_name
        print("welcome to the game world..!!",player_name)

    def attack(self,enemy):
        enemy.life=enemy.life-1
        if self.life > 0:
            print("attack from {self.name}to {enemy.name}")
        else:
            print("Game Over..")
            print(enemy.name,"Dead")
    def show_life(self):
        if self.life <=0:
            print("game over")
        else:        
          print(f"{self.name} life is {self.life}")
player_name1=Game()
player_name2=Game()
player_name1.attack(player_name2)
player_name2.attack(player_name1)
player_name1.attack(player_name2)
player_name1.attack(player_name2)
# player_name1.attack()

player_name2.show_life()

