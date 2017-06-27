#!/usr/bin/env python3

string = input("Please enter text to meme: ")

meme = [letter.upper() if string.index(letter)%2 == 0 \
	 else letter.lower() for letter in string]
meme = ''.join(meme)

print(meme)
