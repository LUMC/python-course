# Exercise: Analyse a repeat structure
# ===
#
# We are going to make a repeating DNA sequence and extract some subsequences
# from it.
#
# * Make a short tandem repeat that consists of three "ACGT" units and five
#   "TTATT" units.
# * Print all suffixes of the repeat structure.
#
# **Note:** A suffix is an ending. For example, the word "spam" has five
# suffixes: "spam", "pam", "am", "m" and "".
#

dna_string = "ACGT" * 3 + "TTATT" * 5
for i in range(0, len(dna_string) + 1):
    print dna_string[i:]

# * Print all substrings of length 3.

k = 3
for i in range(0, len(dna_string) - k + 1):
    print dna_string[i:i + k],

print

# * Print all unique substrings of length 3.
#
# **Hint:** All elements in a set are unique.

unique_words = set()
for i in range(0, len(dna_string) - k + 1):
    unique_words.add(dna_string[i:i + k])

print unique_words
