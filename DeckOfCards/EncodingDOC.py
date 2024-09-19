import itertools
import math

# Initialize deck of cards
deck = [rank + suit for suit in 'CDHS' for rank in 'A23456789TJQK']

# Create a dictionary for encoding characters
char_to_num = {' ': 0}
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i, char in enumerate(alpha):
    char_to_num[char] = i + 1

def encode(message, deck, char_to_num):
    # Convert message to uppercase to match the dictionary
    message = message.upper()
    
    def find_permutation_num(text):
        # Convert each character to its corresponding value from the dictionary
        values = [char_to_num[char] for char in text]
        n = len(values)
        total_value = 0
        for i in range(n):
            # 27 is the base as we have 26 letters + space
            value = 27 ** (n - (i + 1)) * values[i]
            total_value += value
        return total_value
    
    # Calculate the permutation number from the message
    perm_number = find_permutation_num(message)

    def get_specific_perm(cards_deck, perm_number):
        n = len(cards_deck)
        permutation = []
        k = perm_number
        available_cards = cards_deck[:]
        
        # Precompute factorials up to n
        factorial = [math.factorial(i) for i in range(n)]
        
        for i in range(n, 0, -1):
            fact = factorial[i - 1]
            index = k // fact
            permutation.append(available_cards.pop(index))
            k %= fact
            
        return permutation
    
    # Return the specific permutation of the deck
    return get_specific_perm(deck, perm_number)

# Example usage
result = encode("Tarini is a rat bastard", deck, char_to_num)
print(result)

        
        
    