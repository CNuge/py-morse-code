
#mac prerequsites
#brew install portaudio 
#pip install pyaudio

#windows prerequsites
#python -m pip install pyaudio

#Linux
# sudo apt-get install python-pyaudio python3-pyaudio


import pyaudio
import numpy as np
import re

class Morse:
    def __init__(self, morse = None, words = None):
        self.__letter_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
              'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
              'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
              'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
              'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
              'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', ' ': '/' } #has a -> z, 1 -> 9 , and / for spaces
        #dict comprehension to reverse the key, value hash
        self.__morse_to_letter = {v : k for k, v in self.__letter_to_morse.items()}        

        """ take in a message in morse code or plain words,
            store within the object """
        if morse is not None and words is not None:
            raise ValueError('can only pass in words or morse, not both!')
        if morse is not None:
            self.read_morse(morse)
        if words is not None:
            self.read_words(words)


    def read_morse(self, morse):
        """ read morse code into the class as a string.
            format should be spaces between letters,
            / between words:
            '... --- ... ' #sos
            '-.-. .- -- / -. ..- --. . ' #cam nuge """
        morse_words = morse.split('/')
        self.__morse = [x.split() for x in morse_words]
        # pass the list of words to the converter and store words
        words_from_morse = [[self.__morse_to_letter[letter] for letter in word] 
                                for word in self.__morse]
        self.__words = words_from_morse

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
        morse_from_words = [[self.__letter_to_morse[letter] for letter in word] 
                                for word in self.__words]
        self.__morse = morse_from_words

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


morse_test = Morse()
morse_test.words
morse_test.read_words(test)
morse_test.words
morse_test.morse 
print(morse_test)


test2 = '... --- ... / .----'

morse_test2 = Morse()
morse_test2.read_morse(test2)
morse_test2.morse
morse_test2.words

#iterate dict
for i,j in morse_to_letter.items():
    print(i,j)

#TODO
# change code to avoid the leak between instances... see the ghost bus chapter for how
# have the .read_morse() and .read_words() return valueError is no messages passed


letter_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
              'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
              'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
              'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
              'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
              'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', ' ': '/', 
                }


morse_to_letter = {v : k for k, v in letter_to_morse.items()}

inv_map = {v: k for k, v in my_map.items()}


class DotDash:
    def __init__(self):
        self.p = pyaudio.PyAudio()

        self.volume = 0.5     # range [0.0, 1.0]
        self.fs = 44000       # sampling rate, Hz, must be integer

        self.dash_duration = 1.5
        self.dot_duration = 0.75   # in seconds, may be float

        f = 440.0        # sine frequency, Hz, may be float


        # generate samples, note conversion to float32 array
        self.dot_samples = (np.sin(2*np.pi*np.arange(self.fs*self.dot_duration)*f/fs)).astype(np.float32)
        self.dash_samples = (np.sin(2*np.pi*np.arange(self.fs*self.dash_duration)*f/fs)).astype(np.float32)


        # for paFloat32 sample values must be in range [-1.0, 1.0]
        self.stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

    def dot(self):
        self.stream.write(self.volume*self.dot_samples)
    def dash(self):
        self.stream.write(self.volume*self.dash_samples)

    def close(self):

        # play. May repeat with different volume values (if done interactively) 
        self.stream.write(volume*samples)
        self.stream.stop_stream()
        self.stream.close()

        self.p.terminate()


