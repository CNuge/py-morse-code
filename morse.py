
for i,j in morse_dict.items():
    print(i,j)

import re
class morse:
    def __init__(self, morse = None, words = None):
        """ take in a message in morse code or plain words,
            store within the object """
        if morse is not None and words is not None:
            raise ValueError('can only pass in words or morse, not both!')
        if morse is not None:
            self.read_morse(morse)
        if words is not None:
            self.read_words(words)
        self. morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
              'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
              'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
              'p': '.--.', 'o': '--.-', 'r': '.-.', 's': '...', 't': '-',
              'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
              'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', ' ': '/', 
                } #has a -> z, 1 -> 9 , and / for spaces

    def read_morse(self, morse):
        """ read morse code into the class as a string.
            format should be spaces between letters,
            / between words:
            '... --- ... ' #sos
            '-.-. .- -- / -. ..- --. . ' #cam nuge """
        morse_words = morse.split('/')
        self.__morse = [x.split() for x in morse_words]
        # pass the list of words to the converter and store words

    def read_words(self, words):
        """ read words into the class as a string.
            message is converted to lower case.
            all punctuation is recorded as periods."""
        # remove the punctuation, convert to lower case
        words = re.sub(r'[^\w\s]','', words.lower())
        # split on whitespace
        word_list = words.split()
        # store words as a list (words) of lists (letters)
        self.__words = [list(word) for word in word_list]
        # pass list of words to the converter and store morse

    @property
    def morse(self):
        """ make the morse code callable via x.morse, show the formatted string """
        try:
            return '/'.join([' '.join(x) for x in self.__morse])
        except:
            raise ValueError('no message stored in the object')
    @property
    def words(self):
        """ make the words callable via x.words, show the formatted string """
        try:
            return ' '.join([''.join(x) for x in self.__words])
        except:
            raise ValueError('no message stored in the object')


    #make properties
    # so that someone can go class.morse, or class.words and it will give
    # out a pretty represented version of the data in the class

    # make a repr class that accounts for both the morse and the words
    # so that it will print the words and the morse side by side...
    # possibly include separate or with the repr:
    # make a 'say' and a 'telegraph' function to make python say the message or
    # do the beeps that correspond to the message

test = 'sos, other stuff!'


morse_test = morse()
morse.words #no words... returns <property at 0x10d7c48b8>
            #i would 
morse_test.read_words(test)
morse_test.words

test2 = '... --- ... / ----'

morse_test2 = morse()
morse_test2.read_morse(test2)
morse_test2.morse


#TODO
# change code to avoid the leak between instances... see the ghost bus chapter for how
# have the .read_morse() and .read_words() return valueError is no messages passed

