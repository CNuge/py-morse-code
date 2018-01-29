TO DO:

- write the unit tests for the class
- make the travis.yml file with dependencies, call tests.py
- write the readme with examples of loading in the data via the different methods
- write the dependencies into the readme file
- give some examples in the readme
- make repository public
- explain it in a blog post, highlight the special class methods



The Morse class does the following:

	- reads in string of words or morse code and allow for translation between the two
	- provides a transmit function to play the morse code version of the message out loud
	- lets you easily print the words and corresponding morse side by side
	- mac/linux only: uses the internal say command to read the message out loud

limitations:
	- if the message is input as a word, all punctuation will be removed
	- the 'stop' to indicate the end of a sentence is not yet coded in
		this could be a useful addition if made to be optional
	- the speak command is performed using the mac/linux 'say' command so not usable on windows



# Setup and dependencies

mac prerequsites
brew install portaudio 
pip install pyaudio

windows prerequsites
python -m pip install pyaudio

Linux
	sudo apt-get install python-pyaudio python3-pyaudio
optional - to make the .speak() function work:
	sudo apt-get install gnustep-gui-runtime