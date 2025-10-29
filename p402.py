# Q2 Define a function rotate that receives three arguments and returns a tuple in which the first argument
# is at index 1, the second argument is at index 2 and the third argument is at index 0. Define variables
# a, b and c containing ’Doug’, 22 and 1984. Then call the function three times. For each call, unpack
# its result into a, b and c, then display their values

def rotate(a,b,c):
    return (c,a,b)

a = 'Doug'
b = 22
c = 1984

a,b,c = rotate(a,b,c)
print(f"After First Call: a = {a}, b = {b}, c = {c}")

a,b,c = rotate(a,b,c)
print(f"After Second Call: a = {a}, b = {b}, c = {c}")

a,b,c = rotate(a,b,c)
print(f"After Third Call: a = {a}, b = {b}, c = {c}")

'''
After First Call: a = 1984, b = Doug, c = 22
After Second Call: a = 22, b = 1984, c = Doug
After Third Call: a = Doug, b = 22, c = 1984
'''