def run():
    # pesos = input('Exchange pesos to dollars, please submit your amount: ')
    # pesos = float(pesos)
    # dollar_price = 20.21
    # dollars = round(pesos / dollar_price, 2)
    # print('Your amount in dollars is: $'+ str(dollars))

    currency = input("""
    Currencies.
    1. Mexican pesos
    2. Colombian pesos
    3. Argentine pesos
    4. Brazil reales
    Choose an option please: """)

    if currency == '1':
        pesos = input('Exchange pesos to dollars, please submit your amount: ')
        pesos = float(pesos)
        dollar_price = 20.21
        dollars = round(pesos / dollar_price, 2)
        print('Your amount in dollars is: $'+ str(dollars))
    elif currency == '2':
        pesos = input('Exchange pesos to dollars, please submit your amount: ')
        pesos = float(pesos)
        dollar_price = 4046.68
        dollars = round(pesos / dollar_price, 2)
        print('Your amount in dollars is: $'+ str(dollars))
    elif currency == '3':
        pesos = input('Exchange pesos to dollars, please submit your amount: ')
        pesos = float(pesos)
        dollar_price = 102.58
        dollars = round(pesos / dollar_price, 2)
        print('Your amount in dollars is: $'+ str(dollars))
    elif currency == '4':
        pesos = input('Exchange reales to dollars, please submit your amount: ')
        pesos = float(pesos)
        dollar_price = 5.70
        dollars = round(pesos / dollar_price, 2)
        print('Your amount in dollars is: $'+ str(dollars))
    else:
        print('Incorrect! Please, choose a correct option!')



if __name__ == '__main__':
    run()