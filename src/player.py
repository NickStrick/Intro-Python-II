# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currRoom):
        self.room = currRoom
        self.name = name
