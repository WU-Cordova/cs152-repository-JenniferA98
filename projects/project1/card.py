


class Card:
    """Represents a single card in a deck containing its face, suit and value"""

    face_values = {
        '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
        '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':[1,11]
    }

    suit_symbols = {
        'Hearts': '\u2665',
        'Spades': '\u2660',
        'Clubs': '\u2663',
        'Diamonds': '\u2666'
    }

    def __init__(self, face, suit) -> None:
        """Initializes card with a face and a suit"""
        self.face = face
        self.suit = suit
        self.value = self.get_value(face)


    def get_value(self,face):
        """Returns value of card based on its face"""
        return self.face_values.get(face)


    def __str__(self):
        """Returns a list representation of the cards face and suit"""
        suit_symbol = self.suit_symbols.get(self.suit)
        return f"[{self.face} {suit_symbol}]"


