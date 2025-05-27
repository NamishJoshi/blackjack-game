# modules
import random
from njoshi3_Card import Card

# global variables
suits = {"Hearts", "Diamonds", "Spades", "Clubs"} # set
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
         "Eight", "Nine", "Ten", "Jack", "Queen", "King") # tuple
values = { "Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, 
          "Queen": 10, "King": 10} # dictionary
playing = True

# deck class
class Deck():
  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        temp_card = Card(suit,rank)
        self.deck.append(temp_card)
  
  def __str__(self):
    deck_composition = ''
    for card in self.deck:
      deck_composition += '\n'+ card.__str__()
    return "The deck has: " + deck_composition

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    single_card = self.deck.pop()
    return single_card
