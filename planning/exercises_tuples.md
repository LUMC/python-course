# Tuples

Make a `a_tuple = ("Paris", [1, 2, 3], (10, 20, 30, 40, 50))`.
- Access value `30` from `a_tuple`.
- What is the sum of all the items from the tuple element of `a_tuple`.
- Unpack `a_tuple` in `3` variables: `city`, `a_list`, `another_tuple`.
- Copy elements `30` and `40` from `another_tuple` into `third_tuple`.

a_tuple = ("Paris", [1, 2, 3], (10, 20, 30, 40, 50))
print(a_tuple[2][2])
print(sum(list(a_tuple[2])))
(city, a_list, another_tuple) = a_tuple
third_tuple=another_tuple[2:4]
