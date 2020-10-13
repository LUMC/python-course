# User Defined Functions

1. Write a Python function that returns the maximum of two numbers.
2. Write a Python function that returns the maximum of three numbers.
   Try to reuse the first maximum of two numbers function.
3. Write a Python function that accepts a list as a parameter. Next, it
   determines and prints the number of positive and negative numbers.

def max_of_two(x,y):
    """Returns the maximum of two variables x and y."""
    if x>y:
        return x
    else:
        return y
        
def max_of_three(x,y,z):
    """Returns the maximum of two variables x and y."""
    if x>y and x>z:
        return x
    elif z>x and z>y:
        return z
    else:
        return y
        
def pos_or_neg(aList):
    """Returns the positive and negative values of a list."""
    positive=[]
    negative=[]
    for i in aList:
        if i>=0:
            positive.append(i)
        else:
            negative.append(i)
    return print("The positive values in the list are: ",positive,". The negative values in the list are: ",negative,".")
