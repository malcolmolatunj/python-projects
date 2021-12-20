from string import ascii_letters, digits, punctuation

SYMBOLS = ascii_letters + digits + punctuation
KEY = 20
SHIFTED_SYMBOLS = SYMBOLS[KEY:] + SYMBOLS[:KEY]
translate = dict(zip(SYMBOLS, SHIFTED_SYMBOLS))
recover = dict(zip(SHIFTED_SYMBOLS, SYMBOLS))


def encode(message, *, method='e'):
    message = message.replace(' ','')
    code = translate if method == 'e' else recover
    
    response = ''
    for char in message:
        response += code[char]
    print("Your new message is:", response)


if __name__ == '__main__':
    method = input("Would you like to (e)ncrypt or (d)ecrypt a message?\n> ")
    message = input("Ok, what's your message?\n> ")
    if method.startswith('e'):
        encode(message, method='e')
    elif method.startswith('d'):
        encode(message, method='d')
    else:
        print("I didn't understand the selected method.")
        print("Try running the program again.")

