'''
20.2
Write a method to shuffle a deck of cards. It must be a perfect shuffle - in other words, each 52! permutations of the deck has to be equally likely. Assume that you are given a random number generator which is perfect.
'''
# what is the random number generator like?
import random
def shuffle(cards):
    output = []
    while cards:
        cur = random.choice(cards)
        output += [cur]
        cards.remove(cur)
    return output
    

if __name__ == '__main__': 
    cards = [i for i in range(1,53)]
    print shuffle(cards)