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
    def __init__ (self,roll=None,round=1, dice=6, flag=True, score=0,flag2=True,dice2=0):
        self.roll=roll
        self.round=round
        self.dice=dice
        self.score=score
        super().__init__()
        self.flag=flag
        self.flag2=flag2
        self.dice2=dice2

    def play(self,roller=None):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        self._roller=roller or GameLogic.roll_dice
        self.roll=self._roller
        user_response = input("> ")
        if user_response=="n":
            print("OK. Maybe another time")
        elif user_response=="y":
            while self.flag and not self.dice == 0:
                dices=self._roller(self.dice)
                self.rolling(dices)
                if self.round>20:
                    print(f'Thanks for playing. You earned {self.balance} points')
                    break
    def rolling(self,dices):

        if self.dice == 6:
            print(f"Starting round {self.round}")

        if self.dice2 ==6:
            self.dice=6
        
        print(f"Rolling {self.dice} dice...")
        print(f"*** {' '.join([str(i) for i in dices])} ***")  
        if not self.zilch(dices):
            print(f'You banked 0 points in round {self.round}')
            print(f'Total score is {self.balance} points')
            self.round+=1
            self.dice=6
            self.shelved=0
            self.rolling(self.roll(self.dice))

        if self.flag==True:
            print("Enter dice to keep, or (q)uit:")
        user_choice = input("> ")

        if user_choice=='q':
            self.flag=False
            print(f'Thanks for playing. You earned {self.balance} points')
            return

        else: 
            user_list = [] 
            for i in user_choice:
                user_list.append(int(i))
                
            while self.cheat(user_list,list(dices))==False:
                print("Cheater!!! Or possibly made a typo...")
                print(f"*** {' '.join([str(i) for i in dices])} ***")  
                print("Enter dice to keep, or (q)uit:")
                user_choice=input("> ")
                if user_choice=='q':
                    self.flag=False
                    print(f'Thanks for playing. You earned {self.bank()} points')
                    return
                user_list = []
                for i in user_choice:
                    user_list.append(int(i))
                self.cheat(user_list,list(dices))

                
            user_tuple=tuple(user_list)
            unbanked_score=GameLogic.calculate_score(user_tuple)
            self.shelf(unbanked_score)
            self.dice-=len(user_tuple)

            self.handle_hot_dice(user_list)

            print(f"You have {self.shelved} unbanked points and {self.dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            user_input=input("> ")

            if user_input == 'r':
                unbanked_score=GameLogic.calculate_score(user_tuple)
                self.rolling(self.roll(self.dice))

            elif user_input == 'b':
                print(f"You banked {self.shelved} points in round {self.round}")
                print(f'Total score is {self.bank()} points')
                self.round+=1
                self.dice=6
                self.bank()
                self.score+=self.balance

            elif user_input == 'q':
                self.flag=False
                print(f'Thanks for playing. You earned {self.balance} points')
                return 
        
    def cheat(self,user_choice,dices):
        if len(user_choice) > len(dices):
            
            return False

        for i in user_choice:
            if i in dices:
                dices.remove(i)
            else:
                return False
        return True
    
    def zilch(self,dices):
        dices_score= GameLogic.calculate_score(dices)
        if dices_score==0:
            print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
            return False
        else:
            return True
            
    def handle_hot_dice(self,user_list):
        user_list.sort()
        if len(user_list) >= 6:

            if user_list == [1,2,3,4,5,6]:
                self.flag2=False
                self.dice2=6
            if Counter(user_list).most_common()[0][1] == 2 and Counter(user_list).most_common()[1][1] == 2 and Counter(user_list).most_common()[2][1] == 2:
                self.flag2=False
                self.dice2=6
                

if __name__=='__main__':
    game = Game()
    game.play(GameLogic.roll_dice)
