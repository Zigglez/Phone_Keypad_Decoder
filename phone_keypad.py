import argparse

parser = argparse.ArgumentParser(description='Decode phone key pad number. e.g "python phone_keypad.py 7773323444664 84433 22244474433777"')

parser.add_argument('Numbers', metavar='N', type=str, nargs='+',
                   help='a string of numbers separated by spaces')
args = parser.parse_args()
args = ' '.join(args.Numbers)

string = args.replace(',','').replace('.','').replace(':','').replace('!','').split(' ')

#keypad dictionary
keypad = {
        '2':'ABC',
        '3':'DEF',
        '4':'GHI',
        '5':'JKL',
        '6':'MNO',
        '7':'PQRS',
        '8':'TUV',
        '9':'WXYZ',
        }

def RLE(word):
    word += '$'
    counted_word = ''
    prevChar = word[0]
    count = -1 
    for letter in word:
        if letter != prevChar:
            counted_word += keypad[prevChar][count]
            prevChar = letter
            count = 0
        else:
            count += 1
    return counted_word


text = ''

for word in string:
    text += RLE(word) + ' '

print(text)

