
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
import time

class DotDash:
	""" this class initiates a pyaudio session and can be used to produce the
		morse code output sounds. example:
		sound = DotDash()
		sound.dot()
		sound.dash()"""
	def __init__(self):
		self.p = pyaudio.PyAudio()

		self.volume = 0.4	 # range [0.0, 1.0]
		self.fs = 44000	   # sampling rate, Hz, must be integer

		self.dash_duration = 1.5
		self.dot_duration = 0.75   # in seconds, may be float

		self.f = 400.0		# sine frequency, Hz, may be float


		# generate samples, note conversion to float32 array
		self.dot_samples = (np.sin(2*np.pi*np.arange(self.fs*self.dot_duration)*self.f/self.fs)).astype(np.float32)
		self.dash_samples = (np.sin(2*np.pi*np.arange(self.fs*self.dash_duration)*self.f/self.fs)).astype(np.float32)


		# for paFloat32 sample values must be in range [-1.0, 1.0]
		self.stream = self.p.open(format=pyaudio.paFloat32,
						channels=1,
						rate=self.fs,
						output=True)

	def dot(self):
		self.stream.write(self.volume*self.dot_samples)
	def dash(self):
		self.stream.write(self.volume*self.dash_samples)

	def close(self):
		# play. May repeat with different volume values (if done interactively) 
		self.stream.stop_stream()
		self.stream.close()
		self.p.terminate()


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

		self.read(morse, words)

	def read(self, morse = None, words = None):
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
			return ' / '.join([' '.join(x) for x in self.__morse])
		except:
			raise ValueError('no message stored in the object')
	@property
	def words(self):
		""" make the words callable via x.words, show the formatted string """
		try:
			return ' '.join([''.join(x) for x in self.__words])
		except:
			raise ValueError('no message stored in the object')

	def transmit(self):
		""" when called, this function makes the sound for the morse code message"""
		sound = DotDash()

		for i in self.morse:
			if i == '.':
				sound.dot()
			elif i == '-':
				sound.dash()
			elif i == ' ' or i == '/':
				""" make total of .4 second pause for letter breaks
					and .6 seconds for word breaks """
				time.sleep(.2)

			time.sleep(.2) #wait a fifth of a second between each command

	def speak(self):
		""" for mac os only, this function speaks the morse code message """
		from os import system
		system(f'say {self.words}')

	def __repr__(self):
		""" when print is called, show the morse code underneath the words """
		return f'message: {self.words}\n{self.morse}'


test = 'sos, other stuff!'


morse_test = Morse()
morse_test.words
morse_test.read_words(test)
morse_test.words #show the words
morse_test.morse #show the morse code
print(morse_test) #show the pretty print version of the message
morse_test.transmit() #play message in morse code
morse_test.speak() #say the message


test2 = '... --- ... / .----'
morse_test2 = Morse()
morse_test2.read_morse(test2)
morse_test2.morse
morse_test2.words
morse_test2.transmit()
print(morse_test2)


test3 = 'cam nugent'
morse_test3 = Morse(words = test3)
morse_test3.words
print(morse_test3)


test4 = '-.-. .- -- / -. ..- --. . -. -'
morse_test4 = Morse()
morse_test4.read(morse=test4)
print(morse_test4)





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


#iterate dict
for i,j in morse_to_letter.items():
	print(i,j)

sound = DotDash()
sound.dot()
sound.dash()


