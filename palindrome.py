# recibe un dato del usuario
# evalua el dato del usuario
# responde si es un palindromo o no

def run():
    word = input('Please, write your word or phrase: ')
    word = word.lower()
    word = word.replace(' ','')
    if word == word[::-1]:
        print('Congrats! The word/phrase ' + word + ' is a palindrome')
    else:
        print('Sorry! The word/phrase ' + word + ' is not a palindrome') 


if __name__ == '__main__':
    run()