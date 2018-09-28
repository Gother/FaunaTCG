

class Deck:
    def __init__(self, size, id, cards):
        self.size = size
        self.id = id
        self.cards = cards

    def get_size(self):
        return self.size

    def get_id(self):
        return self.id

    def get_cards(self):
        return self.cards
