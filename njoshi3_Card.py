# global variables
suits = {"Hearts", "Diamonds", "Spades", "Clubs"} # set
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
         "Eight", "Nine", "Ten", "Jack", "Queen", "King") # tuple
values = { "Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, 
          "Queen": 10, "King": 10} # dictionary

# card class
class Card():
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
  
  def __str__(self):
    return self.rank + " of " + self.suit

if __name__ == "__main__":
  new_card = Card("Hearts", "Ace")
  assert new_card.rank == "Ace"
  print(new_card.__str__())