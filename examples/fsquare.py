d = {}
for i in range(10):
    d[i] = i ** 2

for i in d:
    print "{0} is the square of {1}.".format(d[i], i)
