# Creates a list of characters representing the word
def make_list(word):
    L = []
    for c in word:
        L.append(c)
    return L


# Swaps chars in the list and returns a new list without modifying the first one
def mySwap(wordRef, i, j):
    # Prevents changing wordRef.
    # wordRef is a reference of our list of chars and not a copy in that case
    word = wordRef[:]  # Copy of wordRef
    temp = word[i]
    word[i] = word[j]
    word[j] = temp
    return word


# Makes a string from the list of characters
def concat_list(word):
    str_result = ""
    for c in word:
        str_result += c;
    return str_result


def find_permutations(wordStr, index, L):
    word = make_list(wordStr)
    # Recursion Stop Case
    if index + 1 >= len(word):
        return L
    else:
        # Swapping every letter starting from the left
        for i in range(index, len(word)):
            newWord = mySwap(word, index, i)
            L.append(concat_list(newWord))
            # Recursion call, to swap letters from the current swapped letter
            L = find_permutations(newWord, index + 1, L)
        return list(dict.fromkeys(L))  # Prevents same values, could be optimized


def mainFunc():
    # Ask for word
    # Build a list of characters from that word

    # easy test
    # askedWord = "ab"

    # medium test
    # askedWord = "abcd"

    # hard test
    askedWord = "fariner"  # anagramme: refrain ou rafiner // faute ortho

    # RUN
    result = []
    result = find_permutations(askedWord, 0, result)
    # The result has unique elements
    # (converted do dictionnary to convert it into list again)
    # The number of elements should be exactly n!, such as n is len(word)
    print(len(result))
    print("Final results: ", "rafiner" in result)


if __name__ == "__main__":
    print("Hello:")
    mainFunc()
    print("Program Over.")
