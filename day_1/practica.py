DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Ciancoders',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'internship',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    # Comprehensions solutions

    # 1. obtener todos los desarrolladores de python
    python_developers = [dev for dev in DATA if dev['language'] == 'python']
    # printDevs(python_developers, 'Desarrolladores de python')

    # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
    python_developers_20 = [
        dev for dev in DATA if dev['language'] == 'python' and dev['age'] > 20]
    """ printDevs(python_developers_20,
              'Desarrolladores de python que tienen una edad mayor a 20') """
              
    # 3. obtener todos los trabajadores de ciancoders
    dev_cian = [dev for dev in DATA if dev['organization'] == 'Ciancoders']
    # printDevs(dev_cian, 'Trabajadores de ciancoders')

    # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
    dev_cian_30 = [dev for dev in DATA if dev['organization']
                   == 'Ciancoders' and dev['age'] > 30]
    """ printDevs(
        dev_cian_30, 'Trabajadores de ciancoders que tienen una edad mayor a 30') """

    # 5. obtener todos los trabajadores de mayores de 18 años
    dev_18 = [dev for dev in DATA if dev['age'] > 18]
    # printDevs(dev_18, 'Trabajadores de mayores de 18 años')

    # 6. obtener todos los trabajadores de mayores a 70 años
    dev_70 = [dev for dev in DATA if dev['age'] > 70]
    printDevs(dev_70, 'Trabajadores de mayores de 70 años')


def printDevs(dev_array, title):
    print(f'### {title} ###')
    for dev in dev_array:
        print(dev)
    print('-' * 100)


if __name__ == '__main__':
    run()
