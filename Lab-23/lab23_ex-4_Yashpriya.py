# Exercise-4.a -
def CreateRepeats(n):
    n1=n
    def repeat(string):
       return [n1*string]
    return repeat   # Outer function is returning the inner function
repeat_10=CreateRepeats(10)
print(repeat_10("Hello"))

# Exercise-4.b -
def CreateExponent(n):
    n1=n
    def exponent(m):
        return m**n
    return exponent
get_square=CreateExponent(2)
getCube=CreateExponent(3)
print(f"Square: {get_square(5)}")
print(f"Cube: {getCube(2)}")
