import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
player_score = 0
dealer_score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank
    
    def get_value(self):
        return VALUES[self.get_rank()]     

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        
# define hand class
class Hand:
    
    #__init__ 
    def __init__(self):
        self.hand = []
    
    #__str__
    def __str__(self):
        hand_string = '' 
        for x in self.hand:
            hand_string += str(x) + ' ' 
        hand_string += str(self.get_value())
        
        return hand_string 
    
    #adds cards to empty hand
    def add_card(self, card):
        self.hand.append(card)
    
    #gets value of the hand 
    def get_value(self):
        val = 0
        num_aces = 0
        for x in self.hand:
            val += x.get_value()
            if num_aces > 0 and (val + 10) <= 21:
                val += 10
            if x.get_rank() == 'A':
                num_aces += 1
        return val
                   
   
    def draw(self, canvas, pos, draw_back):
        
        for x in self.hand:
            location = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(x.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(x.suit))
            if draw_back == True:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [CARD_CENTER[0] +pos[0] + 73 * self.hand.index(x), CARD_CENTER[1] + pos[1]], CARD_BACK_SIZE)
                draw_back = False
            else:                
               canvas.draw_image(card_images, location, CARD_SIZE,[CARD_CENTER[0] +pos[0] + 73 * self.hand.index(x), CARD_CENTER[1] + pos[1]], CARD_SIZE)            
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for x in RANKS:
            for y in SUITS:
                self.deck.append(Card((y),(x)))


    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.card = self.deck[0]
        self.deck.remove(self.card)
        return self.card
    
    def __str__(self):
        deck_string = ''
        for x in self.deck:
            deck_string += str(x) + ' '	# return a string representing the deck
        return deck_string

#define event handlers for buttons
def deal():
    global outcome, score, in_play, player_hand, dealer_hand, my_deck, in_play
    my_deck = Deck()
    my_deck.shuffle()
    print my_deck

    player_hand = Hand()
    dealer_hand = Hand()
    outcome = "Would You Like To Hit Or Stand?"
    in_play = True

    
    player_hand.add_card(my_deck.deal_card())    
    dealer_hand.add_card(my_deck.deal_card())
    player_hand.add_card(my_deck.deal_card())    
    dealer_hand.add_card(my_deck.deal_card())
    
    print player_hand 
    print dealer_hand 


    

def hit():
    global my_deck, player_hand, dealer_score, hit_or_stand, outcome	# replace with your code below
    player_hand.add_card(my_deck.deal_card())
    
    if player_hand.get_value() > 21:
        outcome = "You Busted! The Dealer Wins! Deal?"
        dealer_score += 1
        
    print player_hand


    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global my_deck, player_hand, dealer_hand, player_score, dealer_score, outcome, in_play
    # replace with your code below
     
    in_play = False 
   
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(my_deck.deal_card())

    if dealer_hand.get_value() >  21:
         outcome = "The Dealer Busts! Player Wins! Deal?"
         player_score += 1
            
    elif dealer_hand.get_value() >= player_hand.get_value():
         outcome = "The Dealer Wins! Deal?"
         dealer_score += 1
    else:
         outcome = 'The Player Wins! Deal?'
         player_score += 1
            


                    
        
        
    print str(player_hand) + ' ' + '- Players Hand'    
    print str(dealer_hand) + ' ' + '- Dealers Hand' 

   
       
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

def reset():
    global score, outcome, player_score, dealer_score
    player_score = 0
    dealer_score = 0
    outcome = 0
    in_play = False
    deal()
    
# draw handler    
def draw(canvas):  
    
    global in_play    
    dealer_hand.draw(canvas, [0, 100], in_play)    
    player_hand.draw(canvas, [0, 350], False)
    
    
    canvas.draw_text(outcome, [1, 250], 20, "Black")
    canvas.draw_text("Your Score Is: "+ str(player_score), [1, 50], 20, "Black")
    canvas.draw_text("Dealer's Hand", [1, 85], 20, "Black")
    canvas.draw_text("Your Hand", [1, 320], 20, "Black")
    canvas.draw_text("The Dealer's Score is: " + str(dealer_score), [400, 50], 20, "Black")
    canvas.draw_text("Black Jack",[220, 50], 35, "Black")

   

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw)


deal()
frame.start()

