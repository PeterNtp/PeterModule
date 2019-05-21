def toMorse(text):
    dec = ''
    mordic = { 'A':'.-', 'B':'-...', 
               'C':'-.-.', 'D':'-..', 'E':'.', 
               'F':'..-.', 'G':'--.', 'H':'....', 
               'I':'..', 'J':'.---', 'K':'-.-', 
               'L':'.-..', 'M':'--', 'N':'-.', 
               'O':'---', 'P':'.--.', 'Q':'--.-', 
               'R':'.-.', 'S':'...', 'T':'-', 
               'U':'..-', 'V':'...-', 'W':'.--', 
               'X':'-..-', 'Y':'-.--', 'Z':'--..', 
               '1':'.----', '2':'..---', '3':'...--', 
               '4':'....-', '5':'.....', '6':'-....', 
               '7':'--...', '8':'---..', '9':'----.', 
               '0':'-----', ', ':'--..--', '.':'.-.-.-', 
               '?':'..--..', '/':'-..-.', '-':'-....-', 
               '(':'-.--.', ')':'-.--.-' }
    
    for letter in text.upper():
        if letter != ' ':
            dec += mordic[letter] + ' '
    return print(f'Morse Code: {dec[:-1:]}')

def is_prime(num):
    mult = 0
    for n in range(1, num+1):
        if(num%n == 0):
            mult += 1
            print(f"Divisível por: {n}")
    if(mult == 2):
        print(f"{num} é primo!")
    elif(mult > 2):
        print(f"{num} não é primo, pois tem {mult} divisores!")