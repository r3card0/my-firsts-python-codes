def run():
    user_value = input('Enter a value: ')
    count = 0
    while count < int(user_value):
        print('Your value is lower than: ',str(count))
        count = count + 1
    print('Good bye')



if __name__ == '__main__':
    run()