# Python3 program Miller-Rabin primality test
import random 

# Check if inconclusive
def millerTest(d, n):
    
    # random number in [2..n-2], n > 4
    a = 2 + random.randint(1, n - 4)

    x = modPow(a, d, n)

    if (x == 1 or x == n - 1):
        return True

    # Keep squaring to find a modular division
    while (d != n - 1):
        x = (x * x) % n
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

# Modular exponentiation for (x ^ y) % n
def modPow(x, y, n):
    result = 1
    
    # Update x if it is more than or
    # equal to p
    x = x % n
    while (y > 0):
        # If odd
        if (y & 1):
            result = (result * x) % n

        y = y // 2
        x = (x * x) % n
    
    return result

# Miller rabin to check if not prime or inconclusive
def isPrime(n, k):
    # Special cases
    if (n == 1 or n == 4):
        return False
    if (n <= 3):
        return True

    # Find r such that n = 
    # 2^d * r + 1 for some r >= 1
    d = n - 1
    while (d % 2 == 0):
        d //= 2

    # Check k times
    for i in range(k):
        if (millerTest(d, n) == False):
            return False
    return True



# Program cycle
while True:
    try:
        userInput = (input("Enter a number to test its primality (Enter E to exit): "))
        userInput = int(userInput)

        if (userInput) <= 0:
            print("ERROR: please enter a positive integer \n")
            continue
    except:
        if userInput == "E":
            break

        print("ERROR: please enter a valid integer \n")
        continue
    
    k = 4   # iterations

    # Test primality with miller rabin
    if isPrime(userInput, k):
        print(userInput, "is inconclusive \n")
    else:
        print("Composite:", userInput, "is not prime! \n")
