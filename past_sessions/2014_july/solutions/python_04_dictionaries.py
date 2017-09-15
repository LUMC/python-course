# Exercise: Dictionaries
# ===
#
# We are going to store the output of a function ($f(x) = x^2$) together with
# its input in a dictionary.
#
# * Make a dictionary containing all squares smaller than 100.
# * Print the content of this dictionary in english, e.g., "4 is the square
#   of 2".

d = {}
for i in range(10):
    d[i] = i ** 2

for i in d:
    print "{0} is the square of {1}.".format(d[i], i)
