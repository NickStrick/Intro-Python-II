# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[], is_light=False):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light

    def setItem(self, item):
        if self.items == []:
            self.items = [item]
        else:
            self.items = [*self.items, item]

    def removeItem(self, item):
        for i in self.items:
            if item == i:
                self.items.remove(i)

            # else:
            #     print('item isnt in list!!!')
