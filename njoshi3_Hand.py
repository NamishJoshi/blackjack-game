# global variables
suits = {"Hearts", "Diamonds", "Spades", "Clubs"} # set
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
         "Eight", "Nine", "Ten", "Jack", "Queen", "King") # tuple
values = { "Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, 
          "Queen": 10, "King": 10} # dictionary

# hand class: adds a card to a hand and checks for points total
class Hand():
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def add_card(self, card):
    self.cards.append(card)
    self.value += values[card.rank]
    if card.rank == "Ace":
      self.aces += 1

  def check_aces(self):
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1