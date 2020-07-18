import animals as an


class Zoo:

    def __init__(self, animals=None):
        if animals and type(animals) == list:
            self.animals = animals
        else:
            self.animals = []

    def check_animals(self):
        habitat = input('Which habitat # do you need?\n')

        while habitat != 'exit':
            print(self.animals[int(habitat)])
            habitat = input('Which habitat # do you need?\n')

        print('See you!')

    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def del_animal(self, del_animal):
        self.animals.remove(del_animal)


if __name__ == '__main__':
    animals = [an.camel, an.lion, an.deer, an.goose, an.bat, an.rabbit]
    my_zoo = Zoo(animals)
    my_zoo.check_animals()
