# Flow Control

1. Use the `input` builtin function to read two variables and print the
   maximum between them.
2. Considering a list `integers = [-2, 3, 20, -4]`.
   - Print only the positive values from the `integers` list.
   - Extend the `integers` list with another `10` values.
   - Print the number of positive values from the updated `integers` list.


1. 
var1=input("Enter the first variable: ")
var2=input("Enter the second variable: ")
if int(var1)>int(var2):
    print(var1)
else:
    print(var2)

2A
integers=[-2,3,20,-4]
for i in integers:
    if i>0:
        print(i)

2B
for i in range(0,11):
    integers.append(i)
print(integers)

2C
for i in integers:
    if i>0:
        print(i)
