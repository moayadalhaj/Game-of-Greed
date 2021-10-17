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
        return amount

    def clear_shelf(self):
        self.shelved=0