from Crypto.Util.number import getPrime, bytes_to_long, getRandomRange;

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 3
m = n.bit_length() // (2 * e ** 2)

pad1 = getRandomRange(0, (1 << m))
pad2 = pad1 + (1 << m) - 69

flag = b"f1n4lly_s0m30n3_d1d_i7"
M = bytes_to_long(flag)

m1 = (M + pad1) % n
m2 = (M + pad2) % n
print(pad1)
print(pad2)

c1 = pow(m1, e, n)
c2 = pow(m2, e, n)

with open("msg.enc", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c1 = {c1}\n")
    f.write(f"c2 = {c2}")