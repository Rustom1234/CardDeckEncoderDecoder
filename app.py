from flask import Flask, render_template, request
import math
import base64

app = Flask(__name__)

class CardDeck:
    def __init__(self):
        self.deck = [rank + suit for suit in 'CDHS' for rank in 'A23456789TJQK']
    
    def get_deck(self):
        return self.deck.copy()

class CharacterEncoder:
    def __init__(self):
        self.char_to_num = {' ': 0}
        self.num_to_char = {0: ' '}
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i, char in enumerate(alpha):
            self.char_to_num[char] = i + 1
            self.num_to_char[i + 1] = char
    
    def encode_char(self, char):
        return self.char_to_num.get(char.upper(), 0)
    
    def decode_num(self, num):
        return self.num_to_char.get(num, ' ')
    
    def encode_message(self, message):
        return [self.encode_char(char) for char in message.upper()]
    
    def decode_numbers(self, numbers):
        return ''.join([self.decode_num(num) for num in numbers])

class MessageEncoder:
    def __init__(self, deck, char_encoder):
        self.deck = deck
        self.char_encoder = char_encoder
    
    def find_permutation_num(self, values):
        n = len(values)
        total_value = 0
        for i in range(n):
            # 27 is the base as we have 26 letters + space
            value = 27 ** (n - (i + 1)) * values[i]
            total_value += value
        return total_value
    
    def get_specific_perm(self, cards_deck, perm_number):
        n = len(cards_deck)
        permutation = []
        k = perm_number
        available_cards = cards_deck[:]
        
        # Precompute factorials up to n
        factorial = [math.factorial(i) for i in range(n + 1)]
        
        for i in range(n, 0, -1):
            fact = factorial[i - 1]
            index = k // fact
            if index >= len(available_cards):
                raise ValueError("Permutation number is too large for the deck size.")
            permutation.append(available_cards.pop(index))
            k %= fact
            
        return permutation
    
    def encode(self, message):
        values = self.char_encoder.encode_message(message)
        perm_number = self.find_permutation_num(values)
        encoded_deck = self.get_specific_perm(self.deck.get_deck(), perm_number)
        return encoded_deck

class MessageDecoder:
    def __init__(self, original_deck, char_encoder):
        self.original_deck = original_deck
        self.char_encoder = char_encoder
    
    def find_permutation_number(self, deck):
        n = len(deck)
        available_cards = self.original_deck.copy()
        perm_number = 0

        # Precompute factorial values
        factorial = [math.factorial(i) for i in range(n + 1)]

        for i in range(n):
            index = available_cards.index(deck[i])
            perm_number += index * factorial[n - i - 1]
            available_cards.pop(index)

        return perm_number
    
    def permutation_number_to_message(self, perm_number):
        if perm_number == 0:
            return ' '
        message = []
        while perm_number > 0:
            char_index = perm_number % 27  # Base 27 (26 letters + space)
            message.append(self.char_encoder.decode_num(char_index))
            perm_number //= 27

        return ''.join(message[::-1])
    
    def decode(self, encoded_deck):
        perm_number = self.find_permutation_number(encoded_deck)
        message = self.permutation_number_to_message(perm_number)
        return message

class Base64Handler:
    @staticmethod
    def further_encode(encoded_deck, delimiter=','):
        """
        Combines the list of encoded cards into a string and encodes it using Base64.
        """
        combined_str = delimiter.join(encoded_deck)
        bytes_str = combined_str.encode('utf-8')
        base64_bytes = base64.b64encode(bytes_str)
        base64_str = base64_bytes.decode('utf-8')
        return base64_str
    
    @staticmethod
    def further_decode(encoded_str, delimiter=','):
        """
        Decodes the Base64 string back to the list of card strings.
        """
        base64_bytes = encoded_str.encode('utf-8')
        bytes_str = base64.b64decode(base64_bytes)
        combined_str = bytes_str.decode('utf-8')
        card_list = combined_str.split(delimiter)
        return card_list

# Initialize components
deck = CardDeck()
char_encoder = CharacterEncoder()
message_encoder = MessageEncoder(deck, char_encoder)
message_decoder = MessageDecoder(deck.get_deck(), char_encoder)

@app.route('/', methods=['GET', 'POST'])
def index():
    encoded_result = None
    decoded_result = None
    if request.method == 'POST':
        if 'encode' in request.form:
            original_message = request.form.get('message', '')
            if original_message:
                try:
                    # Encode the message to a permutation of the deck
                    encoded_deck = message_encoder.encode(original_message)
                    # Further encode the deck into a Base64 string
                    encoded_string = Base64Handler.further_encode(encoded_deck)
                    encoded_result = encoded_string
                except Exception as e:
                    encoded_result = f"Error: {str(e)}"
        elif 'decode' in request.form:
            encoded_string = request.form.get('encoded_string', '')
            if encoded_string:
                try:
                    # Decode the Base64 string back to the deck
                    decoded_deck = Base64Handler.further_decode(encoded_string)
                    # Decode the deck back to the original message
                    decoded_message = message_decoder.decode(decoded_deck)
                    decoded_result = decoded_message
                except Exception as e:
                    decoded_result = f"Error: {str(e)}"
    
    return render_template('index.html', encoded=encoded_result, decoded=decoded_result)

if __name__ == "__main__":
    app.run(debug=True)
