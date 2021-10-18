from game_logic import GameLogic

class Game:
    def __init__ (self, round=1, dice=6):
        self.round=round
        self.dice=dice

    def play(self):
        print("welcome to Game of Greed")
        print("enter y to play the game and n to quit")

        user_response = input("do you want to play > ")
        if user_response=="n":
            print("ok, maybe another time")
        else:
            self.start()

            

    def start(self):
        print(f"start playing round {self.round}")

        print(GameLogic.roll_dice(self.dice))  

        user_choice = input("Enter dice to keep (no spaces) or (q)uit : ")
        user_list = [] 
        for i in user_choice:
            user_list.append(int(i))
            
        
        user_tuple=tuple(user_list)
        print(user_tuple)
        print(f"you have {GameLogic.calculate_score(user_tuple)} unbanked score and {self.dice-len(user_tuple)} remaining dices")

        

                
game = Game()
game.start()
