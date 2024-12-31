import math
import itertools

original_deck = [rank + suit for suit in 'CDHS' for rank in 'A23456789TJQK']

# Create a dictionary to map letters and space to numbers
char_to_num = {' ': 0}
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i, char in enumerate(alpha):
    char_to_num[char] = i + 1

def decode(encoded_deck, original_deck, char_to_num):
    
    # Step 1: Determine the permutation number from the deck
    def find_permutation_number(deck):
        n = len(deck)
        available_cards = original_deck[:]
        perm_number = 0

        # Precompute factorial values
        factorial = [math.factorial(i) for i in range(n + 1)]

        for i in range(n):
            index = available_cards.index(deck[i])
            perm_number += index * factorial[n - i - 1]
            available_cards.pop(index)

        return perm_number

    # Step 2: Convert permutation number back to message
    def permutation_number_to_message(perm_number):
        message = []
        while perm_number > 0:
            char_index = perm_number % 27  # Base 27 (26 letters + space)
            for key, value in char_to_num.items():
                if value == char_index:
                    message.append(key)
                    break
            perm_number //= 27

        return ''.join(message[::-1])

    # Calculate the permutation number from the given deck
    perm_number = find_permutation_number(encoded_deck)
    return permutation_number_to_message(perm_number)

# Example usage
encoded_deck = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AD', '7D', 'TD', '8S', 'KH', '7H', 'KD', 'TH', '2H', '5H', '2D', 'AS', '3D', '9S', 'KS', '9D', '5D', '6D', 'QD', '3H', '5S', '9H', '4D', '7S', '2S', '4H', 'QS', '3S', '8D', '4S', 'JS', '6H', 'JD', 'QH', '8H', 'JH', 'AH', 'TS', '6S']

decoded_message = decode(encoded_deck, original_deck, char_to_num)
print("Decoded message:", decoded_message)
