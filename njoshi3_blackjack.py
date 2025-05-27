# modules
import random
from njoshi3_Card import Card
from njoshi3_Deck import Deck
from njoshi3_Hand import Hand
from njoshi3_Chips import Chips

# global variables
suits = {"Hearts", "Diamonds", "Spades", "Clubs"} # set
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
         "Eight", "Nine", "Ten", "Jack", "Queen", "King") # tuple
values = { "Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, 
          "Queen": 10, "King": 10} # dictionary
playing = True # bool

def take_bet(chips):
  """ Function of asking and keeping track of bets """
  while True:
    try:
      print(f"You have {chips.total} chips!")
      chips.bet = int(input("How many chips would you like to bet? "))
    except ValueError:
      print("Sorry, a bet must be a whole number!")
    else:
      if chips.bet < 0:
        print("Your bet must be either zero or above!")
      elif chips.bet > chips.total:
        print(f"Sorry, the maximum chips you can bet is {chips.total}!")
      else:
        break

def hit(deck, hand):
  """ Function of calling hits """
  hand.add_card(deck.deal())
  hand.check_aces()

def hit_or_stand(deck, hand):
  """ Function of deciding hit or stand by player """
  while True:
    inp = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
    if inp[0].lower() == 'h':
      hit(deck, hand)
    elif inp[0].lower() == 's':
      print("Player stands. Dealer is playing.")
      playing = False
    else:
      print("Please type either h or s, not hit or stand!")
      continue
    break

def show_cards(player, dealer):
  """ Function to show player cards but only one of dealer cards """
  print("\nDealers's Turn: ")
  print(f" {dealer.cards[1]}")
  # asterisk is used to print every item in a list
  # sep is used as seperator between item
  print("\nPlayer's Turn:", *player.cards, sep ='\n ')

def show_all(player,dealer):
  """ Function to show player and dealer cards """
  print("\nDealer's Turn:", *dealer.cards, sep ='\n ') 
  print("Dealer's Total =", dealer.value)
  print("\nPlayer's Turn:", *player.cards, sep ='\n ')
  print("Player's Total =", player.value)

def player_busted(player, chips):
  """ Function to bust player """
  print("Player busted!")
  chips.__sub__()

def player_wins(player, chips):
  """ Function to make player win """
  print("Player wins!")
  chips.__add__()

def dealer_busted(dealer, chips):
  """ Function to bust dealer """
  print("Dealer busted!")
  chips.__sub__()

def dealer_wins(dealer, chips):
  """ Function to make dealer win """
  print("Dealer wins!")
  chips.__add__()
  
# main class
while True:
  print("Hello! Welcome to Blackjack!")
  
  # shuffle and deal two cards to each player
  deck = Deck()
  deck.shuffle()

  player_hand = Hand()
  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())

  dealer_hand = Hand()
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

  player_chips = Chips()
  chip = int(player_chips._Chips__get_score())
  player_chips = Chips(chip)

  # ask player if they want their previous game imported
  import_game = input("Would you like to import your chips? y/n ")
  if import_game[0].lower() == 'y':
    chip = int(player_chips._Chips__get_score())
    player_chips = Chips(chip)

  take_bet(player_chips)
  show_cards(player_hand, dealer_hand)

  while playing:
    hit_or_stand(deck, player_hand)
    show_cards(player_hand, dealer_hand)

    # keep playing until dealer reaches 21
    if player_hand.value < 21:
      hit(deck, dealer_hand)

    # all game win and loss scenarios
    elif player_hand.value > 21:
      player_busted(player_hand, player_chips)
      break
    if dealer_hand.value > 21:
      dealer_busted(dealer_hand, player_chips)
      break
    elif player_hand.value == 21 and player_hand.value != dealer_hand.value:
      player_wins(player_hand, player_chips)
      break

    if player_hand.value == dealer_hand.value and player_hand.value == 21:
      print("Wow! This is a tie!")
      break

  # show player their total remaining chips
  print("--------------------------")
  show_all(player_hand, dealer_hand)
  print(f"\nPlayer total chips are at: {player_chips.total}")

  # ask to play again
  new_game = input("Want to play again? y/n: ")
  if new_game[0].lower() == 'y':
    player_chips.save_score()
    playing = True
    continue
  else:
    save = input("Would you like to save your chips? y/n: ")
    if save[0].lower() == 'y':
      player_chips.save_score()
    else:
      player_chips = Chips()
      player_chips.save_score()
    print("Thank you for playing BlackJack! See you again.")
    break