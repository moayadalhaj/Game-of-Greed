from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game(Banker):
    def __init__ (self, round=1, dice=6, flag=True, score=0):
        self.round=round
        self.dice=dice
        self.score=score
        super().__init__()
        self.flag=flag

    def play(self):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")

        user_response = input("> ")
        if user_response=="n":
            print("ok, maybe another time")
        else:
            while self.flag and not self.dice == 0:
                self.rolling()

            

    def rolling(self):
        print(f"Starting round {self.round}")
        print(f"*** {GameLogic.roll_dice(self.dice)} ***")  

        user_choice = input("Enter dice to keep, or (q)uit:")

        if user_choice=='q':
            self.flag=False
            return 'Thank you for playing with us!'


        user_list = [] 
        for i in user_choice:
            user_list.append(int(i))
            
        user_tuple=tuple(user_list)
        unbanked_score=GameLogic.calculate_score(user_tuple)
        self.score+=unbanked_score
        self.shelf(unbanked_score)
        self.dice-=len(user_tuple)
        print(f"you have {self.score} unbanked score and {self.dice} dice remaining")
        user_input=input("(r)oll again, (b)ank your points or (q)uit:")

        if user_input == 'q':
            self.flag=False
            return f'Thanks for playing. You earned {self.bank()} points'
        elif user_input == 'r':
            unbanked_score=GameLogic.calculate_score(user_tuple)
            # self.score+=unbanked_score
            # self.shelf(unbanked_score)
            # print(f"you have {self.score} unbanked score and {self.dice} remaining dices")
            self.rolling()
        elif user_input == 'b':
            banked_score=self.bank()
            print(f"You banked {banked_score} in round {self.round}")
            print(f'Total score is {self.score} points')
            self.round+=1
            self.dice=6
            self.score=0
        
        

                
game = Game()
game.play()
