# print from 1 to 1000, using loop while
def run():
    print('Print from 1 to 1000 using loop while')


    def one():
        LIMIT = 1002
        counter = 0
        accumulated = counter + 1
        while accumulated < LIMIT:
            print(counter)
            counter = counter + 1
            accumulated = 1 + counter         


    one()


if __name__ == '__main__':
    run()