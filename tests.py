from morse import Morse, DotDash
import unittest



class MorseCodeTests(unittest.TestCase):
	""" """
	@classmethod
	def setUpClass(self):
		""" this sets up a class through each of the initiation methods, making
			sure they all work """
		self.morse_test1 = Morse(morse = '... --- ... / .----')
		self.morse_test2 = Morse(words = 'cam was here')
		self.morse_test3 = Morse()
		self.morse_test3.read_words('You... never did! - The Kenosha Kid')
		self.morse_test3 = Morse()
		self.morse_test4.read_morse('-.-. .- -- / -. ..- --. . -. -')
		self.morse_test5 = Morse()
		self.morse_test5 = read(morse = '... --- ...')

	
	def test_encoding(self):
		self.assertEqual(self.morse_test1.words, self._primary_test)
	
	def test_secondary_output(self):
		self.assertEqual(self._secondary_example, self._secondary_test)


	self.assertRaises(ValueError, match_snp, 'F')
# turn the working examples below into tests, also use them in the readme file for examples

test = 'sos, we are going down!'

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


test3 = 'matt brachmann'
morse_test3 = Morse(words = test3)
morse_test3.read(words='cam')
morse_test3.read_words('matt')
morse_test3.words
morse_test3.morse
print(morse_test3)
morse_test3.transmit()


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


if __name__ == '__main__':

	unittest.main()
