# here is some example code!
from morse import Morse, DotDash

test = 'sos, we are going down!'
morse_test = Morse()
morse_test.words #this throws a value error, no message yet
morse_test.read_words(test)
morse_test.words #show the words
morse_test.morse #show the morse code
print(morse_test) #show the pretty print version of the message
morse_test.transmit() #play message in morse code
morse_test.speak() #say the message


test2 = '... --- ... / .----'
morse_test2 = Morse(morse = test2) #read in to start
morse_test2.morse
morse_test2.words
morse_test2.transmit()
print(morse_test2)


test3 = 'not cam'
morse_test3 = Morse(words = test3, morse='... --- ...') #ValueError - can only do one at a time!
morse_test3 = Morse()
morse_test3.read(words='cam') #the other read method
morse_test3.words
morse_test3.read(words = 'dave') #change the message
morse_test3.words
morse_test3.morse
print(morse_test3)
morse_test3.transmit()


test4 = '-.-. .- -- / -. ..- --. . -. -'
morse_test4 = Morse()
morse_test4.read(morse=test4)
print(morse_test4)


#just make the dot and dash sounds
sound = DotDash()
sound.dot()
sound.dash()

