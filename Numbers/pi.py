# **Find PI to the Nth Digit** -
# Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.
# https://en.wikipedia.org/wiki/Chudnovsky_algorithm
# https://github.com/microice333/Python-projects/blob/master/n_digit_pi.py

from decimal import *

def calculate_pi(n):
    getcontext().prec = n + 1
    C = 426880 * Decimal(10005).sqrt()
    K = 6
    M = 1
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
    pi = C / S
    return pi

print("Pi-Generator")
print("----------------")

while True:
    n = int(input("Please type number between 0-1000"))
    if n >= 0 and n <= 1000:
        break
print(calculate_pi(n))
