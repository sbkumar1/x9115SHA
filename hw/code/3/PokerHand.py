"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from Card import *

class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def make_pair(self):
	self.pair={}
	for card in self.cards:
	        if card.rank in self.pair.keys():
			self.pair[card.rank]+=1
		else:
			self.pair.update({card.rank:1})
  
    def check_pair(self,no_comp):
	self.make_pair()
	for key,value in self.pair.items():
                if (value>=no_comp):
                        return True
	return False

    def has_pair(self):	
	if (self.check_pair(2)==True):
		return True
	else:
		return False
    
    def has_two_pair(self):
	list1=[]
	self.make_pair()
	for key,value in self.pair.items():
		if (value>=4):
			return True
		elif (value>=2):
			list1.append(key)
	if (len(list1)>=2):
		return True
	else:
		return False

    def three_of_a_kind(self):
	if (self.check_pair(3)==True):
                return True
        else:
                return False

    def four_of_a_kind(self):
	if (self.check_pair(4)==True):
                return True
        else:
                return False

    def check_straight(self):
	rank_list=[]
	for card in self.cards:
		rank_list.append(card.rank)
	rank_list.sort()
	counter=0
	for i in range(len(rank_list)-1):
		#print rank_list[i],rank_list[i+1]
		if ((rank_list[i]+1)==rank_list[i+1]):
			counter+=1
		else:
			counter=0
	if (counter>=4):
		#print "counter",counter		
		return True
 
    def check_full_house(self):
	list1=[]
	self.make_pair() 
	for key,value in self.pair.items():
		list1.append(value)
	return set([3,2]).issubset(list1 )	

    def check_straight_flush(self):
	if ((self.has_flush()==True) and (self.check_straight()==True)):
		return True
	else:
		return False

    def classify(self):
	classify=''
	if (self.check_straight_flush()==True):
		classify='Straight Flush'
	elif (self.four_of_a_kind()==True):
		classify='Four of a kind'
	elif (self.check_full_house()==True):
		classify='Full House'
	elif (self.has_flush()==True):
		classify='Flush'
	elif (self.check_straight()==True):
		classify='Straight'
	elif (self.three_of_a_kind()==True):
		classify='Three of a Kind'
	elif (self.has_two_pair()==True):
		classify='Two Pair'
	elif (self.has_pair()==True):
		classify='One Pair'
	else:
		classify='No Pair'
	return classify

    def probab(self):
	counter_straight_flush=0
	counter_four_of_a_kind=0
	counter_full_house=0
	counter_flush=0
	counter_Straight=0
	counter_three_of_a_kind=0
	counter_two_pair=0
	counter_one_pair=0
	counter_no_pair=0
	for i in range(2):
		hand = PokerHand()
        	deck.move_cards(hand, 7)
        	hand.sort()
		x=hand.classify()
		print "Indside Probab",x
		if (x=='Straight Flush'):
			counter_straight_flush=counter_straight_flush+1
		elif (x=='Four of a kind'):
			counter_four_of_a_kind=counter_four_of_a_kind+1
		elif (x=='Full House'):
			counter_full_house=counter_full_house+1
		elif (x=='Flush'):
			counter_flush=counter_flush+1
		elif (x=='Straight'):
			counter_straight=counter_straight+1
		elif (x=='Three of a Kind'):
			counter_three_of_a_kind=counter_three_of_a_kind+1
		elif (x=='Two Pair'):
			counter_two_pair=counter_two_pair+1
		elif (x=='One Pair'):
			counter_one_pair=counter_one_pair+1
		else:
			counter_no_pair=counter_no_pair+1
		print "no pair",counter_no_pair
		print "one pair", counter_one_pair
		print "two pair", counter_two_pair
		print "three of a kind", counter_three_of_a_kind
		print "Straight", counter_three_of_a_kind
		print "Flush", counter_flush
		print "Full House", counter_full_house
		print "Four of a kind",counter_four_of_a_kind
		print "Straight Flush",counter_straight_flush


if __name__ == '__main__':
    # make a deck
    print "Evaluating...."
    counter_straight_flush=0
    counter_four_of_a_kind=0
    counter_full_house=0
    counter_flush=0
    counter_straight=0
    counter_three_of_a_kind=0
    counter_two_pair=0
    counter_one_pair=0
    counter_no_pair=0    
    for i in range(10000):
    	deck = Deck()
    	deck.shuffle()
 	for i in range(7):
                hand = PokerHand()
                deck.move_cards(hand, 7) #Change the no of cards to 5 or 7 here
                hand.sort()
                x=hand.classify()
                #print "Inside Probab",x
                if (x=='Straight Flush'):
                        counter_straight_flush=counter_straight_flush+1
                elif (x=='Four of a kind'):
                        counter_four_of_a_kind=counter_four_of_a_kind+1
                elif (x=='Full House'):
                        counter_full_house=counter_full_house+1
                elif (x=='Flush'):
                        counter_flush=counter_flush+1
                elif (x=='Straight'):
                        counter_straight=counter_straight+1
                elif (x=='Three of a Kind'):
                        counter_three_of_a_kind=counter_three_of_a_kind+1
                elif (x=='Two Pair'):
                        counter_two_pair=counter_two_pair+1
                elif (x=='One Pair'):
                        counter_one_pair=counter_one_pair+1
                else:
                        counter_no_pair=counter_no_pair+1
    print "*************************************************************"
    print "RESULTS FROM 70000 ITERATIONS FOR 7 PLAYERS WITH 7 CARDS EACH"
    print "(All Results are in %)" 
    print "no pair",counter_no_pair/700.000
    print "one pair", counter_one_pair/700.000
    print "two pair", counter_two_pair/700.000
    print "three of a kind", counter_three_of_a_kind/700.000
    print ("Straight %.5f" % (counter_straight/700.0))
    print "Flush", counter_flush/700.000
    print "Full House", counter_full_house/700.000
    print "Four of a kind",counter_four_of_a_kind/700.000
    print ("Straight Flush %.5f" % (counter_straight_flush/700.000))
    print "*********************************************************"
