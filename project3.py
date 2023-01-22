# Random password generator
import random

length = eval(input("Enter the length of the password:"))
print("The length of the password is ", length)

s = "123456789abadefghijklABCmnopqrstCDFIJ10112uvwxyz!@#$%^&&*()"

password = "".join(random.sample(s, length))
print("Your password is", password)
