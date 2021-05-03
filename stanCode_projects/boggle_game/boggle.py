"""
File: boggle.py
Name: Chiachien Li 李佳謙
----------------------------------------
This is a boggle game program.
User can input 4*4 letters.
This program will find words in sequences of adjacent letters.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = []


def main():
	"""
	This is a boggle game program.
	User can input 4*4 letters.
	This program will find words in sequences of adjacent letters.
	"""
	read_dictionary()
	# list to save the letters input
	all_list = [0, 0, 0, 0]
	answers = []
	# answers have printed
	for i in range(4):
		character = input(str(i + 1) + ' row of letters: ')
		character = character.lower()
		if len(character) < 7 or character[1] != ' ' or character[3] != ' ' or character[5] != ' ' or\
			character[0].isalpha() is False or character[2].isalpha() is False or character[4].isalpha() is False or\
			character[6].isalpha() is False:
			print('Illegal input')
			break
		else:
			character += ' '
		all_list[i] = character.split()
	# letters may be able to spell a word
	s = ''
	for y in range(4):
		for x in range(4):
			# used coordinate
			used = []
			# add first word into string
			s += all_list[y][x]
			# add the position to used list
			used.append((x, y))
			# look for words in sequences of adjacent letters
			boggle(all_list, answers, s, used, x, y)
			# clear the letters to start a new round
			s = ''
	print('There are', len(answers), 'words in total.')


def boggle(all_list, answers, s, used, x, y):
	# find word and has not been printed yet
	if s in dictionary and len(s) >= 4 and s not in answers:
		answers.append(s)
		print('Found "'+s+'"')
		# look for longer words with the beginning of the previous word
		boggle(all_list, answers, s, used, x, y)
	else:
		# look for neighbors
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				if 0 <= y + i <= 3 and 0 <= x + j <= 3 and (x + j, y + i) not in used:
					used.append((x + j,  y + i))
					s += all_list[y + i][x + j]
					if has_prefix(s):
						boggle(all_list, answers, s, used, x + j, y + i)
					# no prefix and pop the last letter
					s = s[:len(s)-1]
					# no prefix and pop the coordinate
					used.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip('\n')
			dictionary.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
