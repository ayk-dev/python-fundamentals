class Zoo:
    __animals = 0

    def __init__(self, name):
        self.zoo_name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        zoo_name = self.zoo_name

        result = ''
        if species == 'mammal':
            result += f'Mammals in {self.zoo_name}: {", ".join(self.mammals)}'
        elif species == 'fish':
            result += f'Fishes in {self.zoo_name}: {", ".join(self.fishes)}'
        elif species == 'bird':
            result += f'Birds in {self.zoo_name}: {", ".join(self.birds)}'

        return result

    def get_count(self):
        return f'Total animals: {self.__animals}'


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for _ in range(n):
    species, name = input().split()
    zoo.add_animals(species, name)

species = input()

print(zoo.get_info(species))
print(zoo.get_count())



