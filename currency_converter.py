def run(exchange_rate,dollar_price):
    local_currency = input('Exchange '+ exchange_rate + ' to dollars, please submit your amount: ')
    local_currency = float(local_currency)
    dollars = round(local_currency / dollar_price, 2)
    print('Your amount in dollars is: $'+ str(dollars))
    

currency_menu = input("""
    Currencies.
    1. Mexican pesos
    2. Colombian pesos
    3. Argentine pesos
    4. Brazilian reales
    5. Guatemala quetzales
    Choose an option please: """)

if currency_menu  == '1':
    run('mexican pesos', 20.21)       
elif currency_menu  == '2':
    run('colombian pesos', 4046.80)        
elif currency_menu  == '3':
    run('argentine pesos', 102.58)      
elif currency_menu  == '4':
    run('brazilian reales', 5.70)
elif currency_menu  == '5':
    run('guatemalan quetzales', 7.79)       
else:
    print('Incorrect! Please, choose a correct option!')