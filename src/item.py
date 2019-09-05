

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def onTake(self):
        print(f'you have picked up: {self.name}')

    def onDrop(self):
        print(f'you have dropped: {self.name}')

    def look(self):
        print(f'You looked at the {self.name}:\n    {self.description}')
