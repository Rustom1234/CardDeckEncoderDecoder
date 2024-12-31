# Deck Of Cards Encoder/Decoder

<img src="images/Screenshot 2024-12-31 at 1.02.29 AM.png" alt="Initial App Look" width="400"/>

## Introduction

A Python-based web application that encodes messages into specific permutations of a deck of cards and decodes them back. The application uses Flask for the web interface and Base64 for additional encoding.

## Installation

1. **Clone the Repository:**
```
git clone https://github.com/yourusername/card-deck-encoder.git
cd card-deck-encoder
```
2. **Create a Virtual Environment:**
```
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
3. **Install Required Packages:**
```
pip install Flask
```
This application only requires Flask as an external dependency.

## Running the Application

1. **Navigate to the Project Directory:**
- Ensure you're in the directory containing app.py.
2. **Run the Flask App:**
```
python app.py
```
3. **Access the Web Interface:**
- Open your web browser and navigate to http://127.0.0.1:5000/.

## Usage
1. **Encode a Message**
- Navigate to the "Encode Message" Section:
- Enter Your Message:
- Click "Encode":
The application will process your message and display a Base64 encoded string representing a specific permutation of the deck.

<img src="images/Screenshot 2024-12-31 at 1.09.38 AM.png" alt="Writing Encoded Message" width="300"/> <img src="images/Screenshot 2024-12-31 at 1.09.58 AM.png" alt="Encoding Message..." width="300"/>

2. **Decode a Message**
- Navigate to the "Decode Message" Section:
- Paste the string you wish to decode in the provided textarea.
- Click "Decode":
The application will decode the string and display the original message.

<img src="images/Screenshot 2024-12-31 at 1.15.35 AM.png" alt="Writing Decoded Message" width="300"/><img src="images/Screenshot 2024-12-31 at 1.15.51 AM.png" alt="Decoding Message" width="300"/>

## Credit

The inspiration and initial prompt for the card deck encoding was used from my solution to CodeWars' "Hide a message in a deck of playing cards" practice question. 
The link to the specific question is: 
https://www.codewars.com/kata/59b9a92a6236547247000110.
