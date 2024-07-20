

class Pet:
   
    PET_TYPES = [
    "dog", 
    "cat", 
    "rodent", 
    "bird", 
    "reptile", 
    "exotic"
    ]
    all = []
    
    
    def __init__(self, name, pet_type="dog", owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
    def get_type(self):
        return self._pet_type
    
    def set_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception

    pet_type = property(get_type, set_type)

class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        owner_pets = []
        for pet in Pet.all:
            owner_pets.append(pet)
        return owner_pets

    def add_pet(self, pet):
        if pet.owner is None:
            pet.owner = self
    
    def sort_pets_by_name(self):
        owner_pets = self.pets()
        sorted_pets = sorted(owner_pets, key=lambda pet: pet.name)
        return sorted_pets
    
    def get_sorted_pets(self):
        return self.sort_pets_by_name()