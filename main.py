"""
04 primes ozgur-ozdemir
"""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Verifie si un nombre est entier
    """
    if p < 2:
        return False
    for i in range(2, int(sqrt(p)) + 1 ):
        if p % i == 0:
            return False
    return True

#### Fonction principale

def main():

    # vos appels à la fonction secondaire ici
    """
    Affiches les nombre de 0 à 99
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
