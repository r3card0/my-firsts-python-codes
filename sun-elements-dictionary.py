def run():
    sun_elements = {
    'H':'Hydrogeno',
    'He' : 'Helio',
    'O': 'Oxígeno',
    'N':'Nitrogeno',
    'Si':'Silicio',
    'Mg':'Magnesio',
    'Na':'Sodio',
    'K':'Potasio',
    'Ca': 'Calcio',
    'P': 'Fósforo',
    'S':'Azufre',
    'Fe':'Fierro',
    'Al':'Aluminio',
    'Cu': 'Cobre'
    }
    for symbol, element in sun_elements.items():
        print(symbol,":", element)


if __name__ == '__main__':
    run()