import math
import sys
import random


def is_prime(n, k=500):
    """
    Miller-Rabin primality test.
    Returns True if n is probably prime, False otherwise.
    Increase the value of k for higher accuracy.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generatePQ(bits):
    """
    Generates a large prime number with the specified number of bits.
    """
    while True:
        # Generate a random number of specified bits
        candidate = random.getrandbits(bits)
        # Make sure it's odd and has the correct number of bits
        candidate |= (1 << bits - 1) | 1
        if is_prime(candidate):
            return candidate


def calculateE(f):
    e = random.randrange(1, f)
    while math.gcd(e, f) != 1:
        e = random.randrange(1, f)
    return e


def calculateD(e, f):
    return pow(e, -1, f)


def loadFile(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data


def euler(p, q):
    return (p - 1) * (q - 1)


def createKeys(p, q):
    print(p, q)
    n = p * q
    print(n.bit_length())
    f = euler(p, q)
    e = calculateE(f)
    d = calculateD(e, f)
    return (n, e, d)


def encrypt(message: str, e, n, values: dict):
    #merged_message = int(''.join(map(str, coded_message)))
    i = 0
    value = 0
    for char in message.lower():
        value += values.get(char) * (26 ** i)
        i += 1
    print(value)
    encrypted_message = pow(value, e, n)
    print("This is encrypted message:", encrypted_message)
    return encrypted_message


def decrypt(encrypted_message, d, n):
    answer = []
    decrypted_message = (pow(encrypted_message, d, n))
    print("This is decrypted message:", decrypted_message)
    for i in range(9, -1, -1):
        answer.append(decrypted_message // 26 ** i)
        decrypted_message = decrypted_message % 26 ** i
    answer.reverse()
    print(answer)
    return answer


def convertToString(answer, values: dict):
    result = ""
    for i in answer:
        result += values.get(i)
    print(result)

if __name__ == "__main__":
    sys.set_int_max_str_digits(2000000000)
    values = dict(zip("abcdefghijklmnopqrstuvwxyz", range(0, 26)))
    rev_values = dict(zip(range(0, 26), "abcdefghijklmnopqrstuvwxyz"))
    #message = loadFile("value.txt")
    message = "iksdexyzwz"
    p, q = generatePQ(100), generatePQ(100)
    n, e, d = createKeys(p, q)
    print("n, e, i d:", n, e, d)
    encrypted_message = encrypt(message, e, n, values)
    answer = decrypted_message = decrypt(encrypted_message, d, n)
    convertToString(answer, rev_values)
