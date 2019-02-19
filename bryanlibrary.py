
import math

def fibon_sequence(n): # this is the definition of the funtion
    x = 1
    y = 1

    cont = 1
    while cont <= n: #n is the parameter of the function, that should be given when the function is called
        print('a new fibon number is : ', x + y)

        temp = x
        x = y
        y = y + temp
        cont = cont + 1


def swap(a, b):
    temp = a
    a = b
    b = a
    return print(a, b)

def distance3d(x1, y1, z1, x2, y2, z2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return d

def distance2d(x1, y1, x2, y2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d

def eliminate_repeats(oldlist):
   newlist = []
   for letter in oldlist:
       if letter not in newlist:
           newlist.append(letter)

   return newlist

def convert_list_2word(alist):
    n = len(alist)
    new_word = ''
    for i in range(n):
        new_word = new_word + alist[i]
    return new_word

def translate(text1, dict1):
    #use raw input and split the sentence into a list of words
    list_text = text.split()
    new_list = []

    #iterate the input words and append translation
    #(or word if no translation) to the output
    for word in list_text:
        translation = dict1.get(word)
        new_list_append(translation if translation else word)
    return ''.join(new_list)


word = ''
secrete_word = list(word)
new_word = ['*'for i in range(len(secrete_word))]
penalty = 0
letters_used = []
while '*' in new_word and penalty < 7:
    guess = input("Enter a letter \n")
    if guess not in secrete_word or guess in letters_used:
        penalty += 1
    else:
        for i in range(len(secrete_word)):
            if guess == secrete_word[i]:
                new_word[i] = secrete_word[i]
    letters_used.append(guess)
    print(letters_used)
    print('penalty', penalty)
    print(new_word)


history = {'Archy':(12,4), 'Betty':(10,6)}
print(history)
print(history['Archy'])
print(history['Archy'][0])
print(history['Betty'][1])
#print the rate of success for betty, (6 out of 10)

rate_b = history['Betty'][1]/ history['Betty'][0]
print(rate_b)

rate_a = history['Archy'][1]/ history['Archy'][0]
print(rate_a)

#how to add another player to the history dictionary

history['Claudia'] = (84,36)
print(history)