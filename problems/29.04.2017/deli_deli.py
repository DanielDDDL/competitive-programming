# given a set of rules, define how the plural of a word should be written
# rules:
# 1. if the word is on the list of undefined words, replace it with the one given
# 2. if the word ends in a consonant fallowed by a "y", replace the "y" with "ies"
# 3. If the word end with "o", "s", "ch", "sh" ou "x", add "es" at the end
# 4. If none of the above rules can be applied, just add "s" at the end of it

# ------------------ FUNCTIONS --------------------
# returns the id of the word in the undefined words list
# if not found, returns -1
def und_word_id (word, und_words):
    for i in range (len(und_words)):
        if word == und_words[i][0]:
            return i

    return -1 # not found

# return true if the word end with the given string
# false otherwise
def check_end (word, ending):
    comp_end = word[len(word) - len(ending):] # just the end of the word
    if comp_end == ending:
        return True
    else:
        return False

# apply the specified rules
def make_plural (word, und_words):

    vowels = ["a","e","i","o","u"]
    exceptions = ["o", "s", "ch", "sh", "x"]

    u_id = und_word_id(word, und_words)
    # rule number 1
    if u_id != -1:
        return und_words[u_id][1]

    # rule number 2
    if word[len(word) - 1] == "y" and word[len(word) - 2] not in vowels:
        return word[0:len(word) - 1] + "ies"

    # rule number 3
    for i in range (len(exceptions)):
        if check_end(word, exceptions[i]):
            return word + "es"

    # rule number 4
    return word + "s"


# ------------- START OF THE PROGRAM --------------
# 0 - numbers of undefined words
# 1 - numbers of words that are going to be given
info = [int(x) for x in input().rstrip().split(" ")]
und_words = [] # 0 - singular, 1 - plural
for i in range(info[0]):
    u_word = input().rstrip().split(" ")
    und_words.append(u_word)

for i in range(info[1]):
    word = input().rstrip()
    print(make_plural(word, und_words))
