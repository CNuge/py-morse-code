morse_dict = {'a': '.-',
                'b': '-...',
                'c': '-.-.', 
                'd': '-..',
                'e': '.',
                'f': '..-.',
                'g': '--.',
                'h': '....',
                'i': '..',
                'j': '.---',
                'k': '-.-',
                'l': '.-..',
                'm': '--',
                'n': '-.',
                'o': '---',
                'p': '.--.',
                'o': '--.-',
                'r': '.-.',
                's': '...',
                't': '-',
                'u': '..-',
                'v': '...-',
                'w': '.--',
                'x': '-..-',
                'y': '-.--',
                'z': '--..',
                '0': '-----',
                '1': '.----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.',
                ' ': '/', #will be used to indicate word breaks
                }

for i,j in morse_dict.items():
    print(i,j)


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

    def read_morse(self, morse):
        """ read morse code into the class as a string.
            format should be spaces between letters,
            / between words:
            '... --- ... ' #sos
            '-.-. .- -- / -. ..- --. . ' #cam nuge """
        # trim
        # split the words on the /
        # split the morse on whitespace
        # store a list (message) of lists (words)
        self.morse = 
        # pass the list of words to the converter and store words

    def read_words(self, words):
        """ read words into the class as a string.
            message is converted to lower case.
            all punctuation is recorded as periods."""
        
        # split on whitespace, convert to lower case
        # store words as a list (words) of lists (letters)
        self.words = 
        # pass list of words to the converter and store morse


    # make a repr class that accounts for both the morse and the words
    # so that someone can go class.morse, or class.words and it will give
    # out a pretty represented version of the data in the class


    # make a 'say' and a 'telegraph' function to make python say the message or
    # do the beeps that correspond to the message


