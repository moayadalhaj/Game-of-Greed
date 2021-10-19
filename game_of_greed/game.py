from collections import Counter
import random

class GameLogic():
    """
    GameLogic class that containes two static method
    
    first one is calculate_score:
    --------
    input: a tuple of integers as that represent a dice roll
    output: is an integer representing the roll’s score according to rules of game.
    
    second is roll_dice
    --------
    input: is an integer between 1 and 6
    output: is a tuple with random values between 1 and 6. 
    """
    @staticmethod
    def calculate_score(tuple_input):
        if not len(tuple_input):
            return 0

        count=Counter(tuple_input)

        new_list=list(tuple_input)
        new_list.sort()

        if new_list == [1,2,3,4,5,6]:
            return 1500
        
        if len(tuple_input)==6:
            if Counter(tuple_input).most_common()[0][1] == 2 and Counter(tuple_input).most_common()[1][1] == 2 and Counter(tuple_input).most_common()[2][1] == 2:
                return 1500
        score=0

        if Counter(tuple_input).most_common(1)[0][1] == 3:
            score=100*Counter(tuple_input).most_common(1)[0][0]
            if Counter(tuple_input).most_common(1)[0][0] ==1:
                score=1000
            if len(Counter(tuple_input).most_common()) > 1:
                if Counter(tuple_input).most_common()[1][1] == 3:
                    score+=100*Counter(tuple_input).most_common()[1][0]

        if Counter(tuple_input).most_common(1)[0][1] == 4:
            score=200*Counter(tuple_input).most_common(1)[0][0]
            if Counter(tuple_input).most_common(1)[0][0] ==1:
                score=2000 
        
        if Counter(tuple_input).most_common(1)[0][1] == 5:
            score=300*Counter(tuple_input).most_common(1)[0][0]
            if Counter(tuple_input).most_common(1)[0][0] ==1:
                score=3000 

        if Counter(tuple_input).most_common(1)[0][1] == 6:
            score=400*Counter(tuple_input).most_common(1)[0][0]
            if Counter(tuple_input).most_common(1)[0][0] ==1:
                score=4000 

        for i in count:
            if i == 1 or i==5:
                if count[i] < 3:
                    if (i,count[i]) == (1,1):
                        score = 100+score

                    if (i,count[i]) == (5,1):
                        score = 50+score

                    if (i,count[i]) == (5,2):
                        score = 100+score

                    if (i,count[i]) == (1,2):
                        score = 200+score
        else:
            return score
    
    @staticmethod
    def roll_dice(int_input):
        output=[random.randint(1,6) for i in range(int_input)]
        return tuple(output)


class Banker:
    """
    this class contains two instance methods which relate to the scored points of the game:
    Banker.shelf(): has an integer input and returns all the unbanked score in the shelf
    Banker.bank(): returns all the points that stored in the bank
    Banker.clear_shelf(): clear all the points in the shelf
    """
    def __init__ (self):
        self.balance=0
        self.shelved=0

    def shelf(self,score):
        self.shelved+=score
        return self.shelved

    def bank(self):
        amount=self.shelved
        self.balance+=self.shelved
        self.shelved=0
        return self.balance

    def clear_shelf(self):
        self.shelved=0

class Game(Banker):
    def __init__ (self, round=1, dice=6, flag=True, score=0):
        self.roller=GameLogic.roll_dice
        self.round=round
        self.dice=dice
        self.score=score
        super().__init__()
        self.flag=flag

    def play(self,roller):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")

        user_response = input("> ")
        if user_response=="n":
            print("OK. Maybe another time")
        else:
            while self.flag and not self.dice == 0:
                dices=roller(self.dice)
                self.rolling(dices)
           
    def rolling(self,dices):

        print(f"Starting round {self.round}")
        print(f"Rolling {self.dice} dice...")
        
        print(f"*** {' '.join([str(i) for i in dices])} ***")  

        print("Enter dice to keep, or (q)uit:")
        user_choice = input("> ")

        if user_choice=='q':
            self.flag=False
            print(f'Thanks for playing. You earned {self.bank()} points')
            return


        user_list = [] 
        for i in user_choice:
            user_list.append(int(i))
            
        user_tuple=tuple(user_list)
        unbanked_score=GameLogic.calculate_score(user_tuple)
        self.score+=unbanked_score
        self.shelf(unbanked_score)
        self.dice-=len(user_tuple)
        print(f"You have {self.shelved} unbanked points and {self.dice} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_input=input("> ")

        
        if user_input == 'r':
            unbanked_score=GameLogic.calculate_score(user_tuple)
            self.rolling(self.roller(self.dice))

        elif user_input == 'b':
            print(f"You banked {self.shelved} points in round {self.round}")
            print(f'Total score is {self.bank()} points')
            self.round+=1
            self.dice=6
            self.bank()

        elif user_input == 'q':
            self.flag=False
            print(f'Thanks for playing. You earned {self.balance} points')
            return
        
        

if __name__=='__main__':
    game = Game()
    game.play(GameLogic.roll_dice)
