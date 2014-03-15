__author__ = 'octopuscabbage'
from random import randint
from re import match
import string

class Ghoster:
    def __init__(self):
        self.known_words = set()
        self.load_dict("/usr/share/dict/words")
        self.syllables = set()
        self.__load_syllables()
        self.last_input = ""

    def __load_syllables(self):
        syllables = open("syllables.txt").readlines()
        final_syllables = set()
        for line in syllables:
            final_syllables.add(line.strip(" ").strip("\n").strip(string.punctuation).lower())
        self.syllables = self.syllables.union(final_syllables)

    def load_dict(self,path_to_dict):
        words = open(path_to_dict).readlines()
        final_words = set()
        for line in words:
            final_words.add(line.strip(" ").strip("\n").strip(string.punctuation))
        self.known_words = self.known_words.union((final_words))

    def do_round(self,input_chars):
        if input_chars == "-1":
            #get challenged
            print("How dare you challenge me!")
            input_string = input("What string am I being challenged on >> ")
            words = self.__words_that_begin_with__(input_string)
            words = self.__eliminate_invalid_words__(input_string,words)
            try:
                return words.pop()
            except KeyError:
                return "...oops"
        if input_chars == "":
            #Start the round
            common_letters = ['e','t','a','o','i','n','s','h','r','d']
            return common_letters[randint(0,len(common_letters-1))]
        else:
            words = self.__words_that_begin_with__(input_chars)
            words =self.__eliminate_invalid_words__(input_chars,words)

            if len(words) == 0:
                #Time for some bluffin'!
                return "Challenge!"
            guess_word = self.string_difference(input_chars,words.pop())
            #todo: time permitting, check this word to make sure it's valid on websters
            return guess_word[len(input_chars)]

    def __words_that_begin_with__(self,input_word):
        acceptable_words = set()
        for word in self.known_words:
            if word.startswith(input_word):
                acceptable_words.add(word)
        return acceptable_words

    def __eliminate_invalid_words__(self,input_word,words):
        acceptable_words = set()
        length = len(input_word)
        for word in words:
            if len(word) > length + 1:
                acceptable_words.add(word)
        return acceptable_words

    def guess_valid_next_letter(self,input):
        for syllable in self.syllables:
            if input[-1] in syllable and len(syllable) > 1:
                return syllable[syllable.index(input[-1])]

    def string_difference(self,shorterstring,longerstring):
        return longerstring[len(shorterstring)-1:]
