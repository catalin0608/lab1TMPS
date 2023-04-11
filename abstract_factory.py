class cow:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Mooooooo"
    
    def food(self):
        return "iarba"

    def __str__(self):
        return "vaca"


class dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "HamHam"
    
    def food(self):
        return "carne"

    def __str__(self):
        return "caine"


def get_pet(pet="cow"):
    """the factory method"""

    pets = dict(cow=cow("Jessy"), dog=dog("Buddy"))
    return pets[pet]

class petfactory:
    def __init__(self, name):
        self.name = name

    def get_pet_obj(self):
        return get_pet(self.name)

    def get_food(self):
        return get_pet(self.name).food()


class petStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet_obj()
        food = self._pet_factory.get_food()

        print(f"Animalul este {pet} iar mancarea este {food}, si {pet} vorbeste {pet.speak()}")

cowClass = petfactory('cow')
petStore(cowClass).show_pet()

dogClass = petfactory('dog')
petStore(dogClass).show_pet()
