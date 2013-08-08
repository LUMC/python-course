class Person(object):
    default_weight = 80

    def __init__(self, hair_colour='unknown', weight=0, length=0):
        self.hair_colour = hair_colour
        self.weight = weight or self.default_weight
        self.length = length

    def __str__(self):
        return "Person with hair colour: {0}, weight: {1} and length: {2}".format(
            self.hair_colour, self.weight, self.length)

    def __len__(self):
        return self.length

    def eat(self, amount=3):
        self.weight += amount

    def bleach(self):
        self.hair_colour = 'white'

    def _convert_weight(self, multiplier):
        return self.weight * multiplier

    def weight_in_pounds(self):
        return self._convert_weight(2.20462)

    def weight_in_grams(self):
        return self._convert_weight(1000)
