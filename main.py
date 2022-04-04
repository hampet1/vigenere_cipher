from vigenere_encryption import vigenere_encryptor
import sys


def read_file():
    try: # Open the input and store it in points list
        data = open(sys.argv[1], "r")
        data_str = data.readlines()
        plaintext = ""
        for line in data_str:
            plaintext += line[:-1]
        return plaintext
        if len(data) < 1:
            print("no text available")
            sys.exit()

    finally:
        # alway close a file
        data.close()

if __name__ == '__main__':
    file = read_file()
    PLAINTEXT = "".join(file.lower().split(" "))
    length_of_text = len(PLAINTEXT)
    key_input = str(input("please enter the key word: \n"))
    if len(key_input) > length_of_text:
        key_input = str(input("please enter the key word, the previous one was longer than the original text: \n"))
    key = key_input
    encrypt_text = vigenere_encryptor(PLAINTEXT, key)
    print(f"encrypted text is: {encrypt_text}\nthe encryption key is: {key}")
