
# Bitwise AND
a = 0b1010  # 10
b = 0b1100  # 12
c = a & b
print("and", bin(c))

# Bitwise OR
m = 0b1010  # 10
n = 0b1100  # 12
o = m | n
print("or", bin(o))

# Bitwise XOR
d = 0b1010  # 10
e = 0b1100  # 12
f = d ^ e
print("xor", bin(f))

# Bitwise Not
g = 0b1010  # 10 (not operator uses 2's complement form and return -11)
h = ~g
print("not" , bin(h))

# Left Shift
i = 0b0101
j = i << 1
print("ls" , bin(j))

# Right Shift
k = 0b0101
l = k >> 1
print("rs" , bin(l))