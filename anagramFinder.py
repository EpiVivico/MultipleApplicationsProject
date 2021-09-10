from permutations import *


# This is an Anagram Finder (educational purpose).
# of course this method is way too slow to find anagrams...
class AnagramFinder:
    toPermute = ""  # Input word from user
    # Since dictionaries have a complexity of O(1) (constant), the operation
    # of searching the permutations in this dictionary is way way FASTER
    wordList = dict()  # A lexical reference from the loaded file
    allPermutations = []  # All possible permutations
    finalResults = []  # All anagrams found with the asked word

    # Constructor with a default file to open
    def __init__(self, filename="french.txt"):
        self.filename = filename
        self.openFile()

    # Opens a file of words and stores them into 'wordList'
    def openFile(self):
        file = open(self.filename, "r")
        if file is None:
            print("Error while opening file.")

        print("Opened file")
        lines = file.readlines()

        for i in range(len(lines)):
            self.wordList[lines[i].lower().rstrip()] = i  # add to dictionary

    # Asks for a word you want to search anagrams from
    # (you need to type the input)
    def askWord(self):
        self.toPermute = str(input("Hello there are " + \
                                   str(len(self.wordList)) + " elements in the lexical DataBase\n" \
                                   + "Enter a word: ")).lower()
        print(self.toPermute)

    # This is the function making everythig so slow
    # Doesn't need to find permutations
    # Just need to compare length and letters together)
    def searchAnagram(self):
        self.allPermutations = \
            find_permutations(self.toPermute, 0, self.allPermutations)

        for permutation in self.allPermutations:
            if permutation in self.wordList:
                self.finalResults.append(permutation)


# prevents from running scripts while importing stuff
if __name__ == "__main__":
    Afinder = AnagramFinder()
    Afinder.askWord()
    Afinder.searchAnagram()

    print(Afinder.finalResults)
