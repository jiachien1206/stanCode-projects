"""
File: anagram.py
Name: Chiachien Li 李佳謙
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary = []


def main():
    """
    This program will find the anagrams of the word input
    """
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or', EXIT, 'to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(s)


def read_dictionary():
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip('\n')
            dictionary.append(word)


def find_anagrams(s):
    """
    :param s: the word to find anagrams
    """
    word_list = []
    current_list = []
    anagrams = []
    for ch in s:
        word_list.append(ch)
    length = len(word_list)
    helper(length, word_list, current_list, anagrams)
    print(len(anagrams), 'anagrams:', anagrams)


def helper(length, word_list, current_list, anagrams):
    if len(current_list) == length:
        ans = ''
        for i in current_list:
            ans += word_list[i]
        if ans in dictionary and ans not in anagrams:
            print('Found:', ans)
            anagrams.append(ans)
            print('Searching...')
    else:
        for i in range(length):
            if i in current_list:
                pass
            else:
                current_list.append(i)
                sub_s = ''
                for num in current_list:
                    sub_s += word_list[num]
                if has_prefix(sub_s):
                    helper(length, word_list, current_list, anagrams)
                current_list.pop()


def has_prefix(sub_s):
    """
    :param sub_s: the string that has been chosen
    :return: whether sub_s is the beginning of at least one word in the dictionary
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
