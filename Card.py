

class Card:
    def __init__(self, card_type, name, rarity, display):
        self.card_type = card_type
        self.name = name
        self.rarity = rarity
        self.display = display

    def get_card_type(self):
        return self.card_type

    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity

    def get_display(self):
        return self.display


def loadAnimals():
    with open('animallist', 'r') as f:
        x = f.readlines()

    x = x[10:]
    x = [y.replace('\n', '') for y in x]

    ll = []
    n_elements = 12

    c = int(len(x)/n_elements)


    for i in range(c):
        y = x[i*n_elements:(i+1)*n_elements]
        ll.append(y)

    animal_instances = []

    for animalline in ll:
        aid = animalline[0][:-1]
        name = animalline[1].split(':', 1)[1][1:]
        rarity = animalline[2].split(':', 1)[1][1:]
        display = animalline[3].split(':', 1)[1][1:]
        hp = animalline[4].split(':', 1)[1][1:]
        speed = animalline[5].split(':', 1)[1][1:]
        attack = animalline[6].split(':', 1)[1][1:]
        element = animalline[7].split(':', 1)[1][1:]
        aclass = animalline[8].split(':', 1)[1][1:]
        family = animalline[9].split(':', 1)[1][1:]
        skill = animalline[10].split(':', 1)[1][1:]

        animal = Animal(aid, name, rarity, display, hp, speed, attack, element, aclass, family, skill)
        animal_instances.append(animal)
    return animal_instances


class Animal:
    def __init__(self):
        pass

    def __init__(self, id, name, rarity, display, hp, speed, attack, element, animal_class, family, skill):
        self.name = name
        self.rarity = rarity
        self.display = display
        self.hp = hp
        self.speed = speed
        self.attack = attack
        self.element = element
        self.animal_class = animal_class
        self.family = family
        self.skill = skill


    def get_card_type(self):
        return self.card_type

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity

    def get_display(self):
        return self.display

    def get_hp(self):
        return self.hp

    def get_speed(self):
        return self.speed

    def get_element(self):
        return self.element

    def get_animal_class(self):
        return self.animal_class

    def get_family(self):
        return self.family

    def get_skill(self):
        return self.skill

class Item:
    def __init__(self, id, card_type, name, rarity, display, effect, item_type):
        self.card_type = card_type
        self.name = name
        self.rarity = rarity
        self.display = display
        self.effect = effect
        self.item_type = item_type

    def get_card_type(self):
        return self.card_type

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity

    def get_display(self):
        return self.display

    def get_effect(self):
        return self.effect

    def get_item_type(self):
        return self.item_type
