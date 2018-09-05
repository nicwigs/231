
import cards

# Create the deck of cards
def start():    
    the_deck = cards.Deck()
    the_deck.shuffle()
    
    print( "===== shuffled deck =====" )
    the_deck.display()
    return the_deck


def deal(p1_lst,p2_lst,the_deck):
    print( "Dealt 26 cards to each player (alternating)" )
    print()

    for i in range( 5 ):
        p1_lst.append( the_deck.deal() )
        p2_lst.append( the_deck.deal() )
    print("player 1 hand: {}".format(p1_lst))
    print("player 2 hand: {}".format(p2_lst))

def turn(p_lst,player):
    p_card = p_lst.pop(0) #grab first card
    print("player {} card: {}".format(player,p_card))   
    return p_card.rank() if p_card.rank() != 1 else 14,p_card #if ace make it rank 14
    
def compare(rank1, rank2,p_card1,p_card2,p1_lst,p2_lst):
    if rank1 == rank2:
        print()
        print( "---Tie battle---" )
        p1_lst.append(p_card1)
        p2_lst.append(p_card2)
        print("player 1 hand: {}".format(p1_lst))
        print("player 2 hand: {}".format(p2_lst))
    elif rank1 > rank2:
        print()
        print( "---Player #1 wins battle---" )
        p1_lst.append(p_card1)
        p1_lst.append(p_card2)
        print("player 1 hand: {}".format(p1_lst))
        print("player 2 hand: {}".format(p2_lst))
    else:
        print()
        print( "---Player #2 wins battle---" )
        p2_lst.append(p_card1)
        p2_lst.append(p_card2)
        print("player 1 hand: {}".format(p1_lst))
        print("player 2 hand: {}".format(p2_lst))
        
    if not p1_lst:
        print()
        print("---Winner is player 2---")
        print("player 1 hand: {}".format(p1_lst))
        print("player 2 hand: {}".format(p2_lst))
        return 0
    elif not p2_lst:
        print()
        print("---Winner is player 1---")
        print("player 1 hand: {}".format(p1_lst))
        print("player 2 hand: {}".format(p2_lst))
        return 0

def main():        
    p1_lst=[]
    p2_lst=[]
    
    the_deck = start()    
    deal(p1_lst,p2_lst,the_deck)
    while True:
          p1_tup = turn(p1_lst,1)  
          p2_tup = turn(p2_lst,2)
          result = compare(p1_tup[0],p2_tup[0],p1_tup[1],p2_tup[1],p1_lst,p2_lst)
          if result == 0: #if player runs out of cards
              break
          ask = input("Do you wish to contine playing: 'quit' if not: ")
          if ask == "quit":
              if len(p1_lst) > len(p2_lst):
                  print()
                  print("----Player one wins game----")
                  print("player 1 hand: {}".format(p1_lst))
                  print("player 2 hand: {}".format(p2_lst))
              elif len(p1_lst) < len(p2_lst):
                  print()
                  print("----Player two wins game----")
                  print("player 1 hand: {}".format(p1_lst))
                  print("player 2 hand: {}".format(p2_lst))
              else:
                  print()
                  print("----Tie game----")
                  print("player 1 hand: {}".format(p1_lst))
                  print("player 2 hand: {}".format(p2_lst))
              break
main()