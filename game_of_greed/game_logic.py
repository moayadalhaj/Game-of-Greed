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
                return 1000
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
            score=400*Counter(tuple_input).most_common(1)[0][0]
            if Counter(tuple_input).most_common(1)[0][0] ==1:
                score=4000 

        if Counter(tuple_input).most_common(1)[0][1] == 6:
            score=800*Counter(tuple_input).most_common(1)[0][0]
            if Counter(tuple_input).most_common(1)[0][0] ==1:
                score=8000 

        for i in count:
            if i == 1 or i==5:
                if count[i] < 3:
                    if (i,count[i]) == (1,1):
                        return 100+score

                    if (i,count[i]) == (5,1):
                        return 50+score

                    if (i,count[i]) == (5,2):
                        return 100+score

                    if (i,count[i]) == (1,2):
                        return 200+score
        else:
            return score
    
    @staticmethod
    def roll_dice(int_input):
        output=[random.randint(1,6) for i in range(int_input)]
        return tuple(output)


if __name__== '__main__':
    c=GameLogic()
    print(c.roll_dice(6))
    print(c.calculate_score((1, 6, 3, 2, 5, 4)))
    print(c.calculate_score((1,1,1,5,5)))