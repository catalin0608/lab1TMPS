class papagal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Peekaboo"

    def __str__(self):
        return "papagal"


class corb:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "caw-caw"

    def __str__(self):
        return "corb"


def get_pet(pet="papagal"):
    """Metoda de fabrică"""

    pets = dict(papagal=papagal("Gummy"), corb=corb("Huginn"))
    return pets[pet]


# exemplificăm utilizarea metodei de fabrică pentru a obține un papagal
papagal_pet = get_pet("papagal")
print(f'Acesta este un {papagal_pet}, și sună ca {papagal_pet.speak()}')

# exemplificăm utilizarea metodei de fabrică pentru a obține un corb
corb_pet = get_pet("corb")
print(f'Acesta este un {corb_pet}, și sună ca {corb_pet.speak()}')
