import math


def readFile(name):
    file = open(name, 'r')
    data = file.read()
    file.close()

def convert(word):
    # printing original string
    print("Slowo startowe : " + str(word))

    # using join() + ord() + format()
    # Converting String to binary
    res = ''.join(format(ord(i), '08b') for i in word)

    # printing result
    print("Po konwersji : " + str(res))
    return str(res), len(res)

def init_hash():
    hashes = []
    hashes.append(str(hex(math.sqrt(2))).split(32)[0])
    print(hashes)

        
        
def prep(length, converted:str):
    converted += "1"
    multiplayer = 1 + length//512
    converted+=(multiplayer*512-64)*"0"
    binary_len = str(bin(length)).split("b")[1]
    converted+=binary_len
    print(converted)
    return converted




if __name__ == '__main__':
    #text = readFile("values.txt")
    text = "Hello World"
    converted, length = convert(text)
    print(length)
    prep(length, converted)
    init_hash()
