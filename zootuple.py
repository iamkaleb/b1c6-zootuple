zoo = ('Monkey', 'Bear', 'Cheetah', 'Snake', 'Ostrich', 'Elephant', 'Python', 'Flamingo', 'Otter', 'Lion')

print(zoo.index('Ostrich'))

if 'Flamingo' in zoo:
    print('Flamingo')

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo

print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eighth_animal)
print(ninth_animal)
print(tenth_animal)

zoo_list = list(zoo)

zoo_list.extend(['Jaguar', 'Giraffe', 'Bat'])

print(zoo_list)

zoo = tuple(zoo_list)

print(zoo)