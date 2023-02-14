q = randint(3, 10)
flag_int = 323 #This is the wrong number. Find the correct one yourself!
my_prime = next_prime(ZZ.random_element(2^10, 2^14))
P.<x> = PolynomialRing(Zmod(my_prime^q), implementation='NTL')
poly = 0
for t in range(6):
    poly += ZZ.random_element(2^7, 2^(8))*x^t
poly -= poly(flag_int)

print("My polynomial: ", poly)
print("My prime: ", my_prime)