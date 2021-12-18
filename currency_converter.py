def run():
    pesos = input('Exchange pesos to dollars, please submit your amount: ')
    pesos = float(pesos)
    dollar_price = 20.21
    dollars = round(pesos / dollar_price, 2)
    print('Your amount in dollars is: $'+ str(dollars))



if __name__ == '__main__':
    run()