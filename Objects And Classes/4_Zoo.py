class Zoo:
    __animals = 0

    def __init__(self, zooName):
        self.Zooname = zooName
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
            Zoo.__animals += 1
        elif species == 'fish':
            self.fishes.append(name)
            Zoo.__animals += 1
        elif species == 'bird':
            self.birds.append(name)
            Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.Zooname}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.Zooname}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result += f"Birds in {self.Zooname}: {', '.join(self.birds)}\n"
        result += f'Total animals: {Zoo.__animals}'
        return result


zoo = Zoo(input())
number_of_animals = int(input())
for i in range(number_of_animals):
    zoo_split = input().split(' ')
    species = zoo_split[0]
    animalName = zoo_split[1]
    zoo.add_animal(species, animalName)

print(zoo.get_info(input()))