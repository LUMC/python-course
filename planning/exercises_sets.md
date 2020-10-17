# Sets

Consider `cities_a = ['London', 'Paris', 'Amsterdam', 'Lisbon', 'Prague']` and
`cities_b = {'Madrid', 'Amsterdam', 'Berlin', 'Paris'}`.
- Create a new set that contains only the cities present both in `cities_a`
  and `cities_b`.
- Add `cities_a` elements  to `cities_b`.

cities_a=set(['London', 'Paris', 'Amsterdam', 'Lisbon', 'Prague'])
cities_b=set(['Madrid', 'Amsterdam', 'Berlin', 'Paris'])

cities_ab=cities_a.intersection(cities_b)
cities_b.update(cities_a)
