# Exercise: Iterate over a list
# ===
#
# First we are going to make a list and fill it with a simple sequence. Then
#  we are going to use this list to print something.
#
# * Make a list containing the number 0, 1, ... 9.
# * Print the last 10 lines of the song ''99 bottles of beer'' using this
#   list.

my_list = range(10)
for i in my_list[::-1]:
    print "{0} bottles of beer on the wall, {0} bottles etc.".format(i)
