# global variables
suits = {"Hearts", "Diamonds", "Spades", "Clubs"} # set
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
         "Eight", "Nine", "Ten", "Jack", "Queen", "King") # tuple
values = { "Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, 
          "Queen": 10, "King": 10} # dictionary

# chips class: keeps track of bets and points total
class Chips():
  
  def __init__(self, total=1000):
    self.total = total # allow user to choose bet out of 1000
    self.bet = 0

  def __add__(self):
    self.total += self.bet

  def __sub__(self):
    self.total -= self.bet

  def __str__(self):
    return "Money left: " + str(self.total)

  def __get_score(self):
    __file = open("njoshi3_Chips.txt", "r")
    r_file = __file.readlines()
    __file.close()
    return r_file[1]

  def save_score(self):
    with open("njoshi3_Chips.txt", 'r') as __file:
      data = __file.readlines()
    data[1] = str(self.total)  
    with open("njoshi3_Chips.txt", 'w') as __file:
      __file.writelines(data)
  
if __name__ == "__main__":
  bet = Chips(200)
  assert bet.total == 200
  bet.__sub__()
  bet.__get_score()
  bet.save_score()